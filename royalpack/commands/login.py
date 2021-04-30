import discord
import royalnet.royaltyping as t
import royalnet.engineer as engi
import sqlalchemy.orm as so
import royalpack.database as db
import royalpack.config as cfg
import royalnet_telethon.bullet.contents
import royalnet_discordpy
import royalpack.bolts as rb
import aiohttp
import asyncio
import logging
import arrow
import async_timeout

log = logging.getLogger(__name__)


@rb.capture_errors
@engi.use_database(db.lazy_session_class)
@engi.TeleportingConversation
async def login(*, _msg: engi.Message, _session: so.Session, _imp, **__):
    """
    Fai il login al tuo RYGaccount.
    """

    log.debug("Evaluating config...")
    config = cfg.lazy_config.evaluate()

    private = await enforce_private_message(msg=_msg)

    async with aiohttp.ClientSession() as http_session:

        dc = await device_code_request(
            http_session=http_session,
            client_id=config["auth.client.id"],
            device_url=config["auth.url.device"],
            scopes=["profile", "email", "openid"],
        )

        await prompt_login(
            channel=private,
            verification_url=dc['verification_uri_complete'],
            user_code=dc['user_code']
        )

        try:
            async with async_timeout.timeout(dc["expires_in"]):
                at = await device_code_exchange(
                    http_session=http_session,
                    client_id=config["auth.client.id"],
                    token_url=config["auth.url.token"],
                    device_code=dc["device_code"],
                    sleep_time=9
                )
        except asyncio.TimeoutError:
            await notify_expiration(
                channel=private
            )
            return

        ui = await get_user_info(
            http_session=http_session,
            userinfo_url=config["auth.url.userinfo"],
            token_type=at["token_type"],
            access_token=at["access_token"],
        )

    user = await register_user_generic(session=_session, user_info=ui)
    uas = await register_user_alias(session=_session, user_info=ui)

    log.debug(f"Committing session...")
    _session.commit()

    log.debug(f"Done, notifying the user...")
    await private.send_message(text=f"✅ Login riuscito! Sei loggato come {user.name}!")

    if isinstance(_imp, royalnet_telethon.TelethonPDAImplementation):
        sender = await _msg.sender
        tg = await register_user_telethon(session=_session, user_info=ui, telethon_user=sender._user)

        log.debug(f"Committing session...")
        _session.commit()

        log.debug(f"Done, notifying the user...")
        await private.send_message(text=f"↔️ Sincronizzazione con Telegram riuscita! Sei loggato come {tg.mention()}!")

    elif isinstance(_imp, royalnet_discordpy.DiscordpyPDAImplementation):
        sender = await _msg.sender
        ds = await register_user_discord(session=_session, user_info=ui, discord_user=sender._user)

        log.debug(f"Committing session...")
        _session.commit()

        log.debug(f"Done, notifying the user...")
        await private.send_message(text=f"↔️ Sincronizzazione con Discord riuscita! Sei loggato come <@{ds.id}>!")


async def enforce_private_message(msg: engi.Message) -> engi.Channel:
    """
    Get the private chat for an user and notify them of the switch.

    :param msg: The :class:`~.engi.Message` to reply to.
    :return: The private :class:`~.engi.Channel`.
    """

    log.debug("Sliding into DMs...")

    sender: engi.User = await msg.sender
    current: engi.Channel = await msg.channel
    private: engi.Channel = await sender.slide()
    if hash(current) != hash(private):
        await msg.reply(text="👤 Ti sto inviando un messaggio in chat privata contenente le istruzioni per il login!")
    return private


async def device_code_request(
        http_session: aiohttp.ClientSession,
        client_id: str,
        device_url: str,
        scopes: list[str],
) -> t.JSON:
    """
    Request a OAuth2 device code (which can be exchanged for an access token once the user has given us the
    authorization to do so).

    :param http_session: The :class:`aiohttp.ClientSession` to use.
    :param client_id: The OAuth2 Client ID.
    :param device_url: The URL where device codes can be obtained.
    :param scopes: A :class:`list` of scopes to require from the user.

    :return: The JSON response received from the Identity Provider.
    """

    log.debug("Requesting device code...")

    async with http_session.post(device_url, data={
        "client_id": client_id,
        "scope": " ".join(scopes),
    }) as request:
        return await request.json()


async def prompt_login(channel: engi.Channel, verification_url: str, user_code: str) -> None:
    """
    Ask the user to login.

    :param channel: The :class:`~.engi.Channel` to send the message in.
    :param verification_url: The URL where the user can approve / reject the token.
    :param user_code: Human-friendly view of the device code.
    """

    log.debug("Asking user to login...")

    await channel.send_message(
        text=f"🌍 Effettua il RYGlogin al seguente URL, poi premi Confirm:\n"
             f"{verification_url}\n"
             f"\n"
             f"\uE011(Codice: {user_code})\uE001"
    )


async def device_code_exchange(
        http_session: aiohttp.ClientSession,
        client_id: str,
        token_url: str,
        device_code: str,
        sleep_time: float,
):
    """
    Check if the user has authorized the device code, and try to exchange it for an access token.

    :return: The JSON response received from the Identity Provider.
    """

    log.debug("Starting validation process...")

    while True:
        log.debug(f"Sleeping for {sleep_time}s...")
        await asyncio.sleep(sleep_time)

        async with http_session.post(token_url, data={
            "client_id": client_id,
            "grant_type": "urn:ietf:params:oauth:grant-type:device_code",
            "device_code": device_code,
        }) as request:
            response = await request.json()
            if "error" in response:
                log.debug(f"Response returned error {response['error']!r}, retrying...")
                continue
            elif "access_token" in response:
                log.debug(f"Obtained access token!")
                return response
            else:
                log.error(f"Didn't get an access token, but didn't get an error either?!")
                continue


async def get_user_info(
        http_session: aiohttp.ClientSession,
        userinfo_url: str,
        token_type: str,
        access_token: str,
):
    """
    Get the userinfo of an user.

    :param http_session: The :class:`aiohttp.ClientSession` to use.
    :param userinfo_url: The URL where the user info is obtained.
    :param token_type: The type of the token returned by the Identity Provider (usually ``"Bearer"``)
    :param access_token: The access token to use.
    :return:
    """

    log.debug("Getting user info...")

    async with http_session.post(userinfo_url, headers={
        "Authorization": f"{token_type} {access_token}"
    }) as request:
        return await request.json()


async def notify_expiration(channel: engi.Channel) -> None:
    """
    Notify the user of the device code expiration.

    :param channel: The :class:`~.engi.Channel` to send the message in.
    """

    log.debug("Notifying the user of the expiration...")

    await channel.send_message(
        text=f"🕒 Il codice dispositivo è scaduto e il login è stato annullato. "
             f"Fai il login più in fretta la prossima volta! :)",
    )


async def register_user_generic(
        session: so.Session,
        user_info: dict[str, t.Any],
) -> db.User:
    """
    Sync the user info with the data inside the database.

    :param session: The :class:`~.so.Session` to use.
    :param user_info: The user_info obtained by the Identity Provider.
    :return: The created/updated :class:`.db.User`.
    """

    log.debug("Syncing generic user...")

    user = db.User(
        sub=user_info['sub'],
        last_update=arrow.now(),
        name=user_info['name'],
        nickname=user_info['nickname'],
        avatar=user_info['picture'],
        email=user_info['email'],
    )
    session.merge(user)

    return user


async def register_user_alias(
        session: so.Session,
        user_info: dict[str, t.Any],
):
    """
    .. todo:: Document this.
    """

    log.debug("Syncing user aliases...")

    uas = [
        db.UserAlias(
            user_fk=user_info["sub"],
            name=user_info["name"]
        ),
        db.UserAlias(
            user_fk=user_info["sub"],
            name=user_info["nickname"]
        ),
        db.UserAlias(
            user_fk=user_info["sub"],
            name=user_info["email"]
        ),
        db.UserAlias(
            user_fk=user_info["sub"],
            name=user_info["sub"]
        ),
    ]

    for ua in uas:
        session.merge(ua)

    return uas


async def register_user_telethon(
        session: so.Session,
        user_info: dict[str, t.Any],
        telethon_user,
) -> db.TelegramAccount:
    """
    Sync an user's Telegram account via a Telethon message.

    :param session: The :class:`~.so.Session` to use.
    :param user_info: The user_info obtained by the Identity Provider.
    :param telethon_user: The telethon user to base the user data on.
    :return: The created/updated :class:`~.db.TelegramAccount`
    """

    log.debug("Syncing telethon user...")

    tg = db.TelegramAccount(
        user_fk=user_info["sub"],
        id=telethon_user.id,
        first_name=telethon_user.first_name,
        last_name=telethon_user.last_name,
        username=telethon_user.username,
        avatar_url=None,  # TODO: avatars
    )
    session.merge(tg)
    return tg


async def register_user_discord(
        session: so.Session,
        user_info: dict[str, t.Any],
        discord_user: discord.User,
) -> db.DiscordAccount:
    """
    Sync an user's Discord account via a Discord.py message.

    :param session: The :class:`~.so.Session` to use.
    :param user_info: The user_info obtained by the Identity Provider.
    :param discord_user: The Discord.py user to base the user data on.
    :return: The created/updated :class:`~.db.DiscordAccount`
    """

    log.debug("Syncing telethon user...")

    ds = db.DiscordAccount(
        user_fk=user_info["sub"],
        id=discord_user.id,
        username=discord_user.name,
        discriminator=discord_user.discriminator,
        avatar_url=str(discord_user.avatar_url),
    )
    session.merge(ds)
    return ds


__all__ = ("login",)

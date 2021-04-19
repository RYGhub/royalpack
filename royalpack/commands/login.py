import royalnet.engineer as engi
import sqlalchemy.sql as ss
import sqlalchemy.orm as so
import royalpack.database as db
import royalpack.config as cfg
import royalnet_telethon
import royalnet_telethon.bullet.contents
import aiohttp
import asyncio
import logging
import arrow
import datetime

log = logging.getLogger(__name__)

# FIXME: Properly handle errors in this function!

@engi.use_database(db.lazy_session_class)
@engi.TeleportingConversation
async def login(*, _msg: engi.Message, _session: so.Session, _imp, **__):
    """
    Fai il login al tuo account Royalnet.
    """
    log.debug("Evaluating config...")
    config = cfg.lazy_config.evaluate()

    log.debug("Sliding into DMs...")
    sender: engi.User = await _msg.sender
    current: engi.Channel = await _msg.channel
    private: engi.Channel = await sender.slide()
    if hash(current) != hash(private):
        await _msg.reply(text="👤 Ti ho inviato un messaggio in chat privata contenente le istruzioni per il login!")

    async with aiohttp.ClientSession() as http_session:

        log.debug("Generating device code...")
        async with http_session.post(config["auth.url.device"], data={
            "client_id": config["auth.client.id"],
            "scope": "profile email openid",
            "prompt": "consent",
        }) as request:
            response = await request.json()
            start = arrow.now()

            log.debug("Asking user to login...")
            await private.send_message(
                text=f"🌍 Effettua il RYGlogin al seguente URL, poi premi Confirm:\n"
                     f"{response['verification_uri_complete']}\n"
                     f"\n"
                     f"(Codice: {response['user_code']})"
            )

        expiration = start + datetime.timedelta(seconds=response["expires_in"])
        while arrow.now() < expiration:
            log.debug("Sleeping for 10 seconds...")
            await asyncio.sleep(10)

            async with http_session.post(config["auth.url.token"], data={
                "client_id": config["auth.client.id"],
                "grant_type": "urn:ietf:params:oauth:grant-type:device_code",
                "device_code": response["device_code"],
            }) as request:
                response = await request.json()
                if "error" in response:
                    log.debug(f"Response returned error {response['error']!r}, retrying...")
                    continue
                elif "access_token" in response:
                    log.debug(f"Obtained access token...")
                    break
                else:
                    log.error(f"Didn't get an access token, but didn't get an error either?!")
                    continue
        else:
            log.debug("Login request expired.")
            await private.send_message(text="🕒 La tua richiesta di login è scaduta. "
                                            "Riinvia il comando per ricominciare!")
            return

        async with http_session.post(config["auth.url.userinfo"], headers={
            "Authorization": f"{response['token_type']} {response['access_token']}"
        }) as request:
            response = await request.json()

    log.debug("Checking if the user already exists...")
    user: db.User = _session.execute(
        ss.select(db.User).where(db.User.sub == response["sub"])
    ).scalar()

    log.debug("Creating user dict...")
    user_dict = {
        "sub": response['sub'],
        "last_update": arrow.now(),
        "name": response['name'],
        "nickname": response['nickname'],
        "avatar": response['picture'],
        "email": response['email'],
    }

    if user is None:
        log.info(f"Creating new user: {response['sub']}")
        user = db.User(**user_dict)
        _session.add(user)
    else:
        log.debug(f"Updating existing user: {response['sub']}")
        user.update(**user_dict)

    if isinstance(_imp, royalnet_telethon.TelethonPDAImplementation):
        log.debug("Found out I'm running on Telethon...")

        sender: royalnet_telethon.bullet.contents.TelegramUser

        log.debug("Checking if the TelegramAccount already exists...")
        tg: db.TelegramAccount = _session.execute(
            ss.select(db.TelegramAccount).where(db.TelegramAccount.id == sender._user.id)
        ).scalar()

        log.debug("Creating tg_dict...")
        tg_dict = {
            "user_fk": response["sub"],
            "id": sender._user.id,
            "first_name": sender._user.first_name,
            "last_name": sender._user.last_name,
            "username": sender._user.username,
            "avatar_url": None,  # TODO: avatars
        }

        if tg is None:
            log.info(f"Creating new TelegramAccount: {sender._user.id}")
            tg = db.TelegramAccount(**tg_dict)
            _session.add(tg)
        else:
            log.debug(f"Updating existing TelegramAccount: {sender._user.id}")
            tg.update(**tg_dict)

    log.debug(f"Committing session...")
    _session.commit()

    log.debug(f"Done, notifying the user...")
    await private.send_message(text=f"✅ Login riuscito! Sei loggato come {response['name']}!")


__all__ = ("login",)

import royalnet.royaltyping as t
import royalnet.engineer as engi
import royalnet_discordpy
import royalnet_discordpy.bullet.contents
import discord
import discord.http


activities = {
    "yt": 755600276941176913,
    "poker": 755827207812677713,
    "amogus": 773336526917861400,
    "fishing": 814288819477020702,
}


@engi.TeleportingConversation
async def hack(*, _imp: engi.PDAImplementation, _msg: engi.Message, activity: str, **__):
    """
    Hack!?

    `yt` - YouTube Together
    `amogus` - Betrayal
    """

    if not isinstance(_imp, royalnet_discordpy.DiscordpyPDAImplementation):
        await _msg.reply(text="⚠️ Puoi HACKERARE IL PIANETA solo da Discord.")
        return

    _user: engi.User = await _msg.sender
    user: t.Union[discord.User, discord.Member] = _user._user

    if user.voice is None:
        await _msg.reply(text="⚠️ Devi essere in chat vocale per HACKERARE IL PIANETA.")
        return

    channel: discord.VoiceChannel = user.voice.channel
    data = await channel._state.http.request(
        discord.http.Route('POST', '/channels/{channel_id}/invites', channel_id=channel.id),
        reason="Test",
        json={
            'max_age': 86400,
            'max_uses': 0,
            'target_application_id': activities[activity],
            'target_type': 2,
            'temporary': False,
            'validate': None
        }
    )
    invite: discord.Invite = discord.Invite.from_incomplete(data=data, state=channel._state)

    await _msg.reply(text=f"🎞 https://discord.com/invite/{invite.code}")


__all__ = ("hack",)

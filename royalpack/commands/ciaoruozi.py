import royalnet.engineer as engi
import royalnet_telethon as rt
import royalnet_telethon.bullet.contents as rtc


@engi.PartialCommand.new(syntax="")
async def ciaoruozi(*, _sentry: engi.Sentry, _msg: engi.Message, _imp, **__):
    """
    Saluta Ruozi, una creatura leggendaria che potrebbe esistere o non esistere in Royal Games.
    """

    if isinstance(_imp, rt.TelethonPDAImplementation):
        sender: rtc.TelegramUser = await _msg.sender
        # noinspection PyProtectedMember
        if sender._user.id == 112437036:
            await _msg.reply(text="👋 Ciao me!")

    await _msg.reply(text="👋 Ciao Ruozi!")


__all__ = ("ciaoruozi",)

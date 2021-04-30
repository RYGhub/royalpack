import royalnet.engineer as engi
import royalnet_telethon
import royalnet_telethon.bullet.contents
import royalpack.bolts as rb


@rb.capture_errors
@engi.TeleportingConversation
async def ciaoruozi(*, _msg: engi.Message, _imp, **__):
    """
    Saluta Ruozi, una creatura leggendaria che potrebbe esistere o non esistere in Royal Games.
    """

    if isinstance(_imp, royalnet_telethon.TelethonPDAImplementation):
        sender: royalnet_telethon.bullet.contents.TelegramUser = await _msg.sender
        # noinspection PyProtectedMember
        if sender._user.id == 112437036:
            await _msg.reply(text="👋 Ciao \uE01Bme\uE00B!")

    await _msg.reply(text="👋 Ciao Ruozi!")


__all__ = ("ciaoruozi",)

import royalnet.engineer as engi
import royalpack.bolts as rb


@rb.capture_errors
@engi.TeleportingConversation
async def color(*, _msg: engi.Message, **__):
    """
    Invia un colore in chat...?
    """

    await _msg.reply(
        text="\uE011I am sorry, unknown error occured during working with your request, Admin were notified\uE001"
    )


__all__ = ("color",)

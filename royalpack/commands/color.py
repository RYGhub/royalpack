import royalnet.engineer as engi


@engi.TeleportingConversation
async def color(*, _msg: engi.Message, **__):
    """
    Invia un colore in chat...?
    """

    await _msg.reply(
        text="I am sorry, unknown error occured during working with your request, Admin were notified"
    )


__all__ = ("color",)

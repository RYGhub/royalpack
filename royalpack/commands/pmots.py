import royalnet.engineer as engi


@engi.TeleportingConversation
async def pmots(*, _msg: engi.Message, **__):
    """
    Riprenditi da uno stomp colossale!

    https://t.me/c/1153723135/181784
    """
    await _msg.reply(text="👣 pmots pmots")


__all__ = ("pmots",)

import royalnet.engineer as engi


@engi.TeleportingConversation
async def ping(*, _msg: engi.Message, **__):
    """
    Gioca a ping pong con il bot. 🏓
    """
    await _msg.reply(text="🏓 Pong!")


__all__ = ("ping",)

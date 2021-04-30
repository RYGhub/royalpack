import royalnet.engineer as engi
import royalpack.bolts as rb


@rb.capture_errors
@engi.TeleportingConversation
async def ping(*, _msg: engi.Message, **__):
    """
    Gioca a ping pong con il bot. 🏓
    """
    await _msg.reply(text="🏓 Pong!")


__all__ = ("ping",)

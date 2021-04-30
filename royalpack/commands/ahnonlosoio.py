import royalnet.engineer as engi
import royalpack.bolts as rb


@rb.capture_errors
@engi.TeleportingConversation
async def ahnonlosoio(*, _msg: engi.Message, **__):
    """
    Ah, non lo so io!
    """
    await _msg.reply(text=r"¯\_(ツ)_/¯ Ah, non lo so io!")


__all__ = ("ahnonlosoio",)

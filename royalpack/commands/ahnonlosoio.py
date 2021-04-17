import royalnet.engineer as engi


@engi.TeleportingConversation
async def ahnonlosoio(*, _sentry: engi.Sentry, _msg: engi.Message, **__):
    """
    Ah, non lo so io!
    """
    await _msg.reply(text=r"¯\_(ツ)_/¯ Ah, non lo so io!")


__all__ = ("ahnonlosoio",)

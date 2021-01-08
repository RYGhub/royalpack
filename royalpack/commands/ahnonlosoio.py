import royalnet.engineer as engi


@engi.PartialCommand.new(syntax="")
def ahnonlosoio(*, _sentry: engi.Sentry, _msg: engi.Message, **__):
    """
    Ah, non lo so io!
    """
    await _msg.send_reply(text=r"¯\_(ツ)_/¯ Ah, non lo so io!")


__all__ = ("ahnonlosoio",)

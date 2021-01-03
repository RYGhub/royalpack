import royalnet.engineer as engi


@engi.PartialCommand.new(name="ahnonlosoio", syntax="")
def ahnonlosoio(_sentry: engi.Sentry, _msg: engi.Message, **__):
    """
    Ah, non lo so io!
    """
    await _msg.send_reply(r"¯\_(ツ)_/¯ Ah, non lo so io!")


__all__ = ("ahnonlosoio",)

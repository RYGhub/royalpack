import royalnet.engineer as engi


@engi.PartialCommand.new(syntax="")
async def color(*, _sentry: engi.Sentry, _msg: engi.Message, **__):
    """
    Invia un colore in chat...?
    """
    
    await _msg.send_reply(text="[i]I am sorry, unknown error occured during working with your request, Admin were notified[/i]")


__all__ = ("color",)

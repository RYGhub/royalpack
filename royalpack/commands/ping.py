import royalnet.engineer as engi


@engi.PartialCommand.new(syntax="")
async def ping(*, _sentry: engi.Sentry, _msg: engi.Message, **__):
    """
    A way to check if the bot is working: it will always reply to this command with "🏓 Pong!".
    """
    await _msg.send_reply(text="🏓 Pong!")


__all__ = ("ping",)

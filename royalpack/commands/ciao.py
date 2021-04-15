import royalnet.engineer as engi


@engi.PartialCommand.new(syntax="", lock=False)
async def ciao(*, _sentry: engi.Sentry, _msg: engi.Message, **__):
    await _msg.reply(text="👋 Ciao, chi sei?")

    answer: engi.MessageReceived = await _sentry.filter(engi.Type(engi.MessageReceived)).get()
    _msg: engi.Message = await answer.message
    _text: str = await _msg.text

    await _msg.reply(text=f"👋 Ciao {_text}! Come stai?")

    answer: engi.MessageReceived = await _sentry.filter(engi.Type(engi.MessageReceived)).get()
    _msg: engi.Message = await answer.message
    _text: str = await _msg.text

    if "mamma" in _text or "madre" in _text:
        await _msg.reply(text=f"😐 Ehi... Al massimo sono io quello che sta {_text}!")
    elif "male" in _text:
        await _msg.reply(text=f"☹️ Mi dispiace che tu stia {_text}... :(")
    else:
        await _msg.reply(text=f"🙂 Anche io sto {_text} :)")


__all__ = ("ciao",)

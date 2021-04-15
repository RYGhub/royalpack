import royalnet.engineer as engi


@engi.PartialCommand.new(syntax=r"")
async def help_cmd(*, _sentry: engi.Sentry, _imp: engi.PDAImplementation, _msg: engi.Message, **__):
    if not isinstance(_imp, engi.ConversationListImplementation):
        await _msg.reply(text="⚠️ Questa implementazione gestisce i comandi con un metodo sconosciuto.")

    commands = [command for command in _imp.conversations if isinstance(command, engi.FullCommand)]
    names = set([command.name() for command in commands])
    text = ["ℹ️ Comandi disponibili:"]
    for name in names:
        text.append(f"- {name}")
    text = "\n".join(text)

    await _msg.reply(text=text)


@engi.PartialCommand.new(syntax=r"(?P<cmd>\S+)")
async def help_single(*, _sentry: engi.Sentry, _imp: engi.PDAImplementation, _msg: engi.Message, cmd: str, **__):
    if not isinstance(_imp, engi.ConversationListImplementation):
        await _msg.reply(text="⚠️ Questa implementazione gestisce i comandi con un metodo sconosciuto.")

    commands = [
        command
        for command in _imp.conversations
        if isinstance(command, engi.FullCommand)
        and cmd in command.names
    ]

    text = [f"ℹ️ Sottocomandi di {cmd} disponibili:"]

    for command in commands:
        text.append("")
        text.append("")
        text.append(f"{command}")
        text.append(f"    {command.pattern.pattern}")
        text.append("")
        if ht := command.help():
            text.append(ht.strip())
        else:
            text.append("Questo comando non ha un help text.")

    text = "\n".join(text)

    await _msg.reply(text=text)


__all__ = (
    "help_cmd",
    "help_single",
)

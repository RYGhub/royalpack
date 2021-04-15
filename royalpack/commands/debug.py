import royalnet.engineer as engi
import royalnet_telethon as rt

newline = "\n"


@engi.PartialCommand.new(syntax="")
async def debug(*, _sentry: engi.Sentry, _msg: engi.Message, _pda: engi.PDA, **__):
    """
    Check the implementations currently running on the PDA.
    """
    await _msg.reply(text=f"""
🐛 Sottocomandi di debug disponibili:

- impls
- commands
    """)


@engi.PartialCommand.new(syntax=r"impls")
async def debug_impls(*, _sentry: engi.Sentry, _msg: engi.Message, _pda: engi.PDA, **__):
    await _msg.reply(text=f"""
🐛 Implementazioni attive sul PDA:

{newline.join([f'🔵 {implementation!r}' for implementation in _pda.implementations.values()])}
""")


@engi.PartialCommand.new(syntax=r"exts (?P<impl>\S+)")
async def debug_exts(*, _sentry: engi.Sentry, _msg: engi.Message, _pda: engi.PDA, impl: str, **__):
    await _msg.reply(text=f"""
🐛 Estensioni attive sull'implementazione {impl}:

{newline.join([f'🔵 {extension!r}' for extension in _pda.implementations[impl].extensions])}
""")


@engi.PartialCommand.new(syntax=r"convs (?P<impl>\S+)")
async def debug_convs(*, _sentry: engi.Sentry, _msg: engi.Message, _pda: engi.PDA, impl: str, **__):
    implementation = _pda.implementations[impl]

    if not isinstance(implementation, engi.ConversationListImplementation):
        await _msg.reply(text="⚠️ Questa implementazione gestisce le conversazioni con un metodo sconosciuto.")

    await _msg.reply(text=f"""
🐛 Conversazioni registrate sull'implementazione {impl}:

{newline.join([f'🔵 {command!r}' for command in implementation.conversations])}
""")


__all__ = (
    "debug",
    "debug_impls",
    "debug_exts",
    "debug_convs",
)

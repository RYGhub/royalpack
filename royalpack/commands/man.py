import royalnet.engineer as engi
import royalpack.bolts as rb


@rb.capture_errors
@engi.TeleportingConversation
async def man(*, _msg: engi.Message, _router: engi.Router, commandname: str, **__):
    """
    Visualizza aiuto per un comando.

    Non funziona ancora correttamente per i multicomandi, come /dog: https://github.com/Steffo99/royalnet/issues/11 !
    """

    # TODO: Change this when royalnet/#11 is fixed!

    if not (command := _router.by_name.get(commandname)):
        await _msg.reply(text="⚠️ Il comando che hai specificato non esiste.")
        return

    try:
        command = command.__getattribute__("bare_function")
    except AttributeError:
        pass

    msg = [
        f"ℹ️ Manuale di \uE011{commandname}\uE001:",
        f"{command.__doc__}",
    ]

    await _msg.reply(text="\n".join(msg))


__all__ = ("man",)

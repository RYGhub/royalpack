import royalnet.engineer as engi
import royalnet_telethon as rt
import pkg_resources


@engi.TeleportingConversation
async def version(*, _imp: engi.PDAImplementation, _msg: engi.Message, **__):
    """
    Controlla la versione attuale dei pacchetti di questo bot.
    """

    # noinspection PyListCreation
    msg = [
        f"ℹ️ \uE01BVersioni\uE00B",
    ]

    msg.append("")
    msg.append(f"- \uE01Croyalnet\uE00C \uE01B{pkg_resources.get_distribution('royalnet').version}\uE00B")

    if isinstance(_imp, rt.TelethonPDAImplementation):
        msg.append(f"- \uE01Croyalnet_telethon\uE00C \uE01B{pkg_resources.get_distribution('royalnet_telethon').version}\uE00B")

    msg.append(f"- \uE01Croyalpack\uE00C \uE01B{pkg_resources.get_distribution('royalpack').version}\uE00B")

    await _msg.reply(text="\n".join(msg))


__all__ = ("version",)

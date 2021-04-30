import royalnet.engineer as engi
import royalnet_telethon as rt
import royalnet_discordpy as rd
import pkg_resources
import royalpack.bolts as rb


@rb.capture_errors
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
    elif isinstance(_imp, rd.DiscordpyPDAImplementation):
        msg.append(f"- \uE01Croyalnet_discordpy\uE00C \uE01B{pkg_resources.get_distribution('royalnet_discordpy').version}\uE00B")

    msg.append(f"- \uE01Croyalpack\uE00C \uE01B{pkg_resources.get_distribution('royalpack').version}\uE00B")

    await _msg.reply(text="\n".join(msg))


__all__ = ("version",)

import random
import royalnet.engineer as engi


@engi.TeleportingConversation
async def rocoinflip(*, _sentry: engi.Sentry, _msg: engi.Message, teama: str, teamb: str, **__):
    """
    Scegli quale delle due squadre inizierà per prima.
    """
    flip = random.randrange(0, 2)
    if flip == 0:
        first = teama
        second = teamb
    else:
        first = teamb
        second = teama

    text = [
        f"❔ Risultati del coin flip:",
        f"",
        f"🔹 {first}",
        f"🔸 {second}",
    ]

    await _msg.reply(text="\n".join(text))


__all__ = ("rocoinflip",)

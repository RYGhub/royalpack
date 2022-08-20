import typing as t
import datetime
import random

import royalnet.engineer as engi

import royalpack.bolts as rb


@rb.capture_errors
@engi.TeleportingConversation
async def roll(*, _msg: engi.Message, qty: int, die: int, mod: t.Optional[int], **__):
    """
    Tira un dado nel formato di D&D: `1d20+1`, ad esempio.

    Non perfettamente casuale, **non usare per competizioni o altre cose serie**!
    """

    # modificatore supersegreto della fortuna. ooooh! questo è top secret!
    # "blame cate for this" --steffo

    # usa il giorno attuale come seed
    seed = hash(datetime.date.today())
    lrand = random.Random(x=seed)
    # la variazione massima del risultato deve essere di un sesto del tiro
    luck = lrand.triangular(low=-0.17, high=0.17, mode=0.0)

    # veniamo al dunque

    # resetta il seed
    drand = random.Random()

    # tiriamo i dadi richiesti!
    rolls = []
    for i in range(qty):
        # trova il risultato base del tiro
        result = drand.randint(1, die)

        # tira il valore di fortuna per vedere l'effetto sul dado
        result += (drand.random() * luck) * die

        # arrotonda il risultato
        result = round(result)

        # limita il risultato tra massimo e minimo per non destare sospetti
        result = min(result, die)
        result = max(result, 1)

        rolls.append(result)

    # decidi un'emoji da mostrare
    if luck > 0:
        emoji = "🔆"
    else:
        emoji = "🔅"

    # formuliamo una risposta da mostrare all'utente

    # usando una lista di stringhe che uniremo per inviare il messaggio
    # perchè? performance!
    answer = [
        f"{emoji} {qty}d{die}",
    ]

    if mod and mod != 0:
        answer.append(f"{mod:+}")

    answer.append(" = ")

    total = 0
    for index, result in enumerate(rolls):
        if index != 0:
            answer.append("+")
        answer.append(f"{result}")
        total += result

    answer.append(f" = \uE01B{total}\uE00B")

    await _msg.reply(text="".join(answer))


__all__ = (
    "roll",
)
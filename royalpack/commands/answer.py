import royalnet.engineer as engi
import royalpack.bolts as rb
import datetime
import random


ANSWERS = [
    # Cerchiamo di tenere bilanciate le tre colonne, o almeno le prime due.
    # Se avete un'idea ma metterebbe troppe opzioni in un'unica categoria, mettetela sotto commento.

    # risposte "sì": 19
    "🔵 Sì.",
    "🔵 Decisamente sì!",
    "🔵 Uhm, secondo me sì.",
    "🔵 Sì! Sì! SÌ!",
    "🔵 Yup.",
    "🔵 Direi proprio di sì.",
    "🔵 Assolutamente sì.",
    "🔵 Ma certo!",
    "🔵 Esatto!",
    "🔵 Senz'altro!",
    "🔵 Ovviamente.",
    "🔵 Questa domanda ha risposta affermativa.",
    "🔵 Hell yeah.",
    "🔵 YES! YES! YES!",
    "🔵 yusssssss",
    "🔵 Non vedo perchè no",
    "🔵 Ha senso, ha perfettamente senso, nulla da obiettare, ha senso.",
    "🔵 Yos!",
    "🔵 Sì, ma tienilo segreto...",

    # risposte "no": 19
    "❌ No.",
    "❌ Decisamente no!",
    "❌ Uhm, secondo me sì. No, aspetta, ci ho ripensato. È un no.",
    "❌ No, no, e ancora NO!",
    "❌ Nope.",
    "❌ Direi proprio di no.",
    "❌ Assolutamente no.",
    "❌ Certo che no!",
    "❌ Neanche per idea!",
    "❌ Neanche per sogno!",
    "❌ Niente affatto!",
    "❌ Questa domanda ha risposta negativa.",
    "❌ Hell no.",
    "❌ NO! NO! NO!",
    "❌ lolno",
    "❌ NEIN NEIN NEIN NEIN",
    "❌ Delet dis",
    "❌ Nopety nope!",
    "❌ No, ma tienilo segreto.",

    # risposte "boh": 19
    "❔ Boh.",
    "❔ E io che ne so?!",
    "❔ Non so proprio rispondere.",
    "❔ Non lo so...",
    "❔ Mi avvalgo della facoltà di non rispondere.",
    "❔ Non parlerò senza il mio avvocato!",
    "❔ Dunno.",
    "❔ Perché lo chiedi a me?",
    "❔ Ah, non lo so io!",
    r"❔ ¯\_(ツ)_/¯",
    "❔ No idea.",
    "❔ Dunno.",
    "❔ Boooooh!",
    "❔ Non ne ho la più pallida idea.",
    "❔ No comment.",
    "❔ maibi",
    "❔ maibi not",
    "❔ idk dude",
    "❔ Non mi è permesso condividere questa informazione.",
]


@rb.capture_errors
@engi.TeleportingConversation
async def answer(*, _msg: engi.Message, **__):
    """
    Fai una domanda al bot, che possa essere risposta con un sì o un no: lui ti risponderà!
    """

    h = hash(datetime.datetime.now())
    r = random.Random(x=h)

    message = r.sample(ANSWERS, 1)[0]

    await _msg.reply(text=message)


# Objects exported by this module
__all__ = (
    "answer",
)

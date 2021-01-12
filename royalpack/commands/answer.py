import royalnet.engineer as engi
import random
import daytime

@engi.PartialCommand.new(syntax="")
async def answer(*, _sentry: engi.Sentry, _msg: engi.Message, **__):
    """
    Fai una domanda al bot, che possa essere risposta con un sì o un no: lui ti risponderà!
    """
    
     _answers = [
        # Cerchiamo di tenere bilanciate le tre colonne, o almeno le prime due.
        # Se avete un'idea ma metterebbe troppe opzioni in un'unica categoria, mettetela sotto commento.

        # risposte "sì": 16
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
        "🔵 [url=https://www.youtube.com/watch?v=sq_Fm7qfRQk]YES! YES! YES![/url]",
        "🔵 yusssssss",
        "🔵 Non vedo perchè no",
        "🔵 Ha senso, ha perfettamente senso, nulla da obiettare, ha senso.",

        # risposte "no": 17
        "❌ No.",
        "❌ Decisamente no!",
        "❌ Uhm, secondo me sì. No, aspetta, ci ho ripensato. è un no.",
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
        "❌ [url=https://www.youtube.com/watch?v=fKEZFRcuEqw]NO! NO! NO![/url]",
        "❌ lolno",
        "❌ [url=https://www.youtube.com/watch?v=5lbGAzo9RrM]NEIN NEIN NEIN NEIN[/url]",
        "❌ Delet dis",
        
        # risposte "boh": 18
        "❔ Boh.",
        "❔ E io che ne so?!",
        "❔ Non so proprio rispondere.",
        "❔ Non lo so...",
        "❔ Mi avvalgo della facoltà di non rispondere.",
        "❔ Non parlerò senza il mio avvocato!",
        "❔ Dunno.",
        "❔ Perché lo chiedi a me?",
        "❔ Ah, non lo so io!",
        "❔ ¯\\_(ツ)_/¯",
        "❔ No idea.",
        "❔ Dunno.",
        "❔ Boooooh!",
        "❔ Non ne ho la più pallida idea.",
        "❔ No comment.",
        "❔ maibi",
        "❔ maibi not",
        "❔ idk dude",
    ]
    
    h = hash(datetime.datetime.now())

        r = random.Random(x=h)

        message = r.sample(self._answers, 1)[0]
    
    await _msg.send_reply(message)


__all__ = ("answer",)

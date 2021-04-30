import royalnet.engineer as engi
import random
import datetime
import royalpack.bolts as rb


# Tutte le fortunes qui devono essere positive :)
# O almeno neutrali...
_fortunes = [
    "😄 Oggi sarà una fantastica giornata!",
    "😌 Oggi sarà una giornata molto chill e rilassante.",
    "💰 Oggi sui tuoi alberi cresceranno più Stelline!",
    "🍎 Oggi un unicorno ti lascerà la sua Blessed Apple!",
    "📈 Oggi il tuo team in ranked sarà più amichevole e competente del solito!",
    "🏝 Oggi potrai raggiungere l'Isola Miraggio!",
    "🐱 Oggi vedrai più gatti del solito su Internet!",
    "🐶 Oggi vedrai più cani del solito su Internet!",
    "🐦 Oggi vedrai più uccelli del solito su Internet!",
    "🐌 Oggi incontrerai una chiocciola sperduta!",
    "🎁 Oggi i dispenser di regali in centro funzioneranno senza problemi!",
    "🥕 Oggi il tuo raccolto avrà qualità Iridium Star!",
    "🔴 Oggi troverai più oggetti di rarità rossa del solito!",
    "✨ Oggi farai molti più multicast!",
    "♦️ Oggi troverai una Leggendaria Dorata!",
    "⭐️ Oggi la stella della RYG ti sembrerà un pochino più dritta!",
    "⭐️ Oggi la stella della RYG ti sembrerà anche più storta del solito!",
    "💎 Oggi i tuoi avversari non riusciranno a deflettere i tuoi Emerald Splash!",
    "⬅️ Oggi le tue supercazzole prematureranno un po' più a sinistra!",
    "➡️ Oggi le tue supercazzole prematureranno un po' più a destra!",
    "🌅 Oggi sarà il giorno dopo ieri e il giorno prima di domani!",
    "🤖 Oggi il Royal Bot ti dirà qualcosa di molto utile!",
    "🏠 Oggi qualcuno si autoinviterà a casa tua!",
    "📵 Oggi passerai una bella giornata tranquilla senza che nessuno ti chiami!",
    "🕸 Oggi cadrai trappola di una ragnatela! \uE011O ti arriverà in faccia.\uE001",
    "🔮 Oggi chiederai a @royalgamesbot di dirti la tua /fortune!",
    "👽 Oggi incontrerai gli UFI!!!1!!uno!",
    "🦾 Oggi uno scienziato pazzo ti proporrà di sostituire il tuo braccio con un braccio-razzo meccanico!",
    "🕵️ Oggi una spia in incognito ti chiederà se hai mai visto the Emoji Movie!",
    "🍕 Oggi mangerai una margherita doppio pomodoro!",
    "🍰 Oggi mangerai una torta al gusto di torta!",
    "🥇 Oggi vincerai qualcosa!",
    "🏴‍☠️ Oggi salperai i sette mari con la tua ciurma pirata!",
    "🕒 Oggi sarà ieri, e domani sarà oggi!",
    "🔙 Oggi tornerai indietro nel tempo!",
    "🚨 Oggi suonerà l'allarme della Velvet Room!",
    "🏳️‍🌈 Oggi scoprirai l'esistenza di almeno un gender che non conoscevi!",
    "🥴 Oggi ti dimenticherai come ci si siede!",
    "👀 Oggi scoprirai di avere degli occhi!",
    "🏹 Oggi ti verrà voglia di installare Arch Linux, ma cambierai idea molto in fretta!",
    "🩲 Oggi annuncerai alla cv di essere in mutande!",
    "👟 Oggi tua madre ti regalerà delle scarpe da corsa!",
    "✨ Oggi troverai un Pokémon shiny!",
    "👏 Oggi sarai felice, lo saprai e batterai le mani!",
    "🦴 Oggi scoprirai di avere uno scheletro wholesome all'interno di te!",
    "💳 Oggi riuscirai a fornire i tre numerini della tua carta di credito a John Wick!",
    "🤔 Oggi smetterai finalmente di essere sus, in quanto sarai confermato dal villaggio!",
]


@rb.capture_errors
@engi.TeleportingConversation
async def fortune(*, _msg: engi.Message, **__):
    """
    Come sarà la giornata di oggi?
    """

    author = await _msg.sender

    r = random.Random(x=hash(author) + hash(datetime.date.today()))
    message = r.sample(_fortunes, 1)[0]

    await _msg.reply(text=message)


__all__ = ("fortune",)

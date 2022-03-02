import royalnet.engineer as engi
import royalpack.bolts as rb
import datetime
import random

WHO = [
    # A chi sarà diretto l'insulto
    "Dio",
    "Zio",
    "Gesù",
    "Cristo",
    "Maria",
    "Madonna",
    "Eva",
    "Adamo",
    "Rettore",
    "Steffo",
    "Bot",
    "Telegram",
    "Discord",
]
WHAT = [
    # l'aggettivo per descrivere il soggetto
    # Non deve essere per forza un insulto, anche qualche neutro è bene accetto e dà quel po' di random in più
    "santə",
    "grandissimə",
    "porcə",
    "cane",
    "capra",
    "maialə",
    "infame (per te solo le lame)",
    "grassə",
    "galleggiante",
    "tuamammicə",
    "marzianə",
    "canguro nella landa dei soffitti bassi",
    "scalzə nella valle dei chiodi",
    "tirchiə",
    "poliedricə",
    "palindromə",
    "pantagruelicə",
    "stellare",
    "novax",
    "intollerante al lattosio",
    "rygatonə",
    "puzzolente",
    "saturə",
    "saccente",
    "ciambella",
    "sfigmomanometro",
    "buonə",
    "boia",
    "[getting bored already]",
]


@rb.capture_errors
@engi.TeleportingConversation
async def diobot(*, _msg: engi.Message, **__):
    """
    Il bot è molto arrabbiato e vuole creare insulti coloriti!
    """

    message = "🤬 "+random.sample(WHO, 1)[0]
    for i in range(random.randint(1, 5)):
        message += " "
        message += random.sample(WHAT, 1)[0]
    message += "!"

    await _msg.reply(text=message)


# Objects exported by this module
__all__ = (
    "diobot",
)

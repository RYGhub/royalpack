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
    
    "aguzzinə",
    "alcolizzatə",
    "anticə",
    "aggressivə",
    "bestia",
    "boia",
    "bischerə",
    "bricconə",
    "brontolonə",
    "bruttə",
    "buonə",
    "buzzurrə",
    "canaglia",
    "cane",
    "canguro nella landa dei soffitti bassi",
    "capra",
    "ciambelliforme",
    "citrullə",
    "codardə",
    "complottista",
    "creazionista",
    "dannunzianə",
    "disonestə",
    "disordinatə",
    "egocentricə",
    "esattorə delle tasse",
    "fannullonə",
    "farabuttə",
    "gaglioffə",
    "galleggiante",
    "gaymer",
    "grandissimə",
    "grassə",
    "grossə",
    "ignobile",
    "ignorante",
    "imbroglionə",
    "impertinente",
    "incapace",
    "incivile",
    "infame (per te solo le lame)",
    "infettə",
    "insensatə",
    "internet explorer",
    "intollerante al lattosio",
    "lavativə",
    "lazzaronə",
    "lestofante",
    "lunaticə",
    "maialə",
    "mangiapane a tradimento",
    "manigoldə",
    "marranə",
    "marzianə",
    "mentecattə",
    "mascalzonə",
    "meschinə",
    "nanerottolə",
    "nichilista",
    "novax",
    "opulentə",
    "palindromə",
    "pantagruelicə",
    "pigrə",
    "pivellə",
    "poliedricə",
    "porcə",
    "pusillanime",
    "puzzolente",
    "puzzonə",
    "rygatə",
    "rygatonə",
    "rozzə",
    "saccente",
    "santə",
    "saturə",
    "scalzə nella valle dei chiodi",
    "sciachimista",
    "screanzatə",
    "sfericə",
    "sfigmomanometro",
    "sgarbatə",
    "stupidə",
    "stellare",
    "tamarrə",
    "terrapiattista",
    "tirchiə",
    "troglodita",
    "tuamammicə",
    "vecchiə",
    "vile",
    "villanə",
    "viscidə",
    "zoticə",
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

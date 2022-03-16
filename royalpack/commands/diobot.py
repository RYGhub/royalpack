import random

import royalnet.engineer as engi

import royalpack.bolts as rb

WHO = [
    # A chi sarà diretto l'insulto
    ["Dio", "o"],
    ["Zio", "o"],
    ["Gesù", "o"],
    ["Cristo", "o"],
    ["Maria", "a"],
    ["Madonna", "a"],
    ["Eva", "a"],
    ["Adamo", "o"],
    ["Rettore", "o"],
    ["Steffo", "o"],
    ["Bot", "o"],
    ["Telegram", "o"],
    ["Discord", "o"],
]
WHAT = [
    # l'aggettivo per descrivere il soggetto
    # Non deve essere per forza un insulto, anche qualche neutro è bene accetto e dà quel po' di random in più

    "aguzzin+",
    "alcolizzat+",
    "alt+",
    "antic+",
    "aggressiv+",
    "bass+",
    "bestia",
    "boia",
    "bischer+",
    "briccone",
    "brutt+",
    "buggat+",
    "buon+",
    "buzzurr+",
    "canaglia",
    "cane",
    "canguro nella landa dei soffitti bassi",
    "capra",
    "carnivor+"
    "ciambelliforme",
    "citrull+",
    "codard+",
    "complottista",
    "creazionista",
    "dalle ossa grosse",
    "dannunzian+",
    "disonest+",
    "disordinat+",
    "egocentric+",
    "esattore delle tasse",
    "espans+",
    "fannullon+",
    "farabutt+",
    "gaglioff+",
    "galleggiante",
    "gaymer",
    "grandissim+",
    "grass+",
    "gross+",
    "ignobile",
    "ignorante",
    "imbroglion+",
    "impertinente",
    "incapace",
    "incivile",
    "infame (per te solo le lame)",
    "infett+",
    "insensat+",
    "internet explorer",
    "intollerante al lattosio",
    "lavativ+",
    "lazzaron+",
    "lent+",
    "lestofante",
    "lunatic+",
    "maiale",
    "mangiapane a tradimento",
    "manigold+",
    "marran+",
    "marzian+",
    "mentecatt+",
    "mascalzone",
    "meschin+",
    "nanerottol+",
    "nichilista",
    "noios+",
    "novax",
    "opulent+",
    "palindrom+",
    "pantagruelic+",
    "pigr+",
    "pivell+",
    "poliedric+",
    "porc+",
    "pusillanime",
    "puzzolente",
    "puzzon+",
    "rygat+",
    "rygaton+",
    "rozz+",
    "saccente",
    "sant+",
    "satur+",
    "scalz+ nella valle dei chiodi",
    "sciachimista",
    "screanzat+",
    "sferic+",
    "sgarbat+",
    "stupid+",
    "stellare",
    "tamarr+",
    "tard+",
    "terrapiattista",
    "tirchi+",
    "troglodita",
    "tuamammic+",
    "vecchi+",
    "vegetarian+"
    "vile",
    "villan+",
    "viscid+",
    "zotic+",
]


@rb.capture_errors
@engi.TeleportingConversation
async def diobot(*, _msg: engi.Message, **__):
    """
    Il bot è molto arrabbiato e vuole creare insulti coloriti!
    """
    who = random.sample(WHO, 1)[0]
    message = "🤬 " + who[0]
    for i in range(random.randint(1, 5)):
        message += " "
        message += random.sample(WHAT, 1)[0].replace("+", who[1])
    message += "!"

    await _msg.reply(text=message)


# Objects exported by this module
__all__ = (
    "diobot",
)

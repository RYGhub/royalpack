import random

import royalnet.engineer as engi

import royalpack.bolts as rb

WHO = [
    # A chi sarà diretto l'insulto
    [1, "Dio"],
    [1, "Zio"],
    [1, "Gesù"],
    [1, "Cristo"],
    [2, "Maria"],
    [2, "Madonna"],
    [2, "Eva"],
    [1, "Adamo"],
    [1, "Rettore"],
    [1, "Steffo"],
    [1, "Bot"],
    [1, "Telegram"],
    [1, "Discord"],
    [3, "Rygatoni"],
    [3, "Moderatori"],
]
WHAT = [
    # l'aggettivo per descrivere il soggetto
    # Non deve essere per forza un insulto, anche qualche neutro è bene accetto e dà quel po' di random in più

    ["aguzzin+",        "o", "a", "i", "e"],
    ["alcolizzat+",     "o", "a", "i", "e"],
    ["alt+",            "o", "a", "i", "e"],
    ["antic+",          "o", "a", "hi", "he"],
    ["aggressiv+",      "o", "a", "i", "e"],
    ["bass+",           "o", "a", "i", "e"],
    ["besti+",          "a", "a", "e", "e"],
    ["boia",            "", "", "", ""],
    ["bischer+",        "o", "a", "i", "e"],
    ["briccon+",        "e", "a", "i", "e"],
    ["brontolon+",      "e", "a", "i", "e"],
    ["brutt+",          "o", "a", "i", "e"],
    ["buggat+",         "o", "a", "i", "e"],
    ["buon+",           "o", "a", "i", "e"],
    ["buzzurr+",        "o", "a", "i", "e"],
    ["canagli+",        "a", "a", "e", "e"],
    ["ca+",             "ne", "gna", "ni", "gne"],
    ["cangur+ nella landa dei soffitti bassi", "o", "a", "i", "e"],
    ["capr+",           "a", "a", "e", "e"],
    ["carnivor+",       "o", "a", "i", "e"],
    ["ciambelliform+",  "e", "e", "i", "i"],
    ["citrull+",        "o", "a", "i", "e"],
    ["codard+",         "o", "a", "i", "e"],
    ["complottist+",    "a", "a", "i", "e"],
    ["creazionist+",    "a", "a", "i", "e"],
    ["dalle ossa grosse", "", "", "", ""],
    ["dannunzian+",     "o", "a", "i", "e"],
    ["disonest+",       "o", "a", "i", "e"],
    ["disordinat+",     "o", "a", "i", "e"],
    ["egocentric+",     "o", "a", "i", "e"],
    ["esattor+ delle tasse", "e", "a", "i", "e"],
    ["espans+",         "o", "a", "i", "e"],
    ["fannullon+",      "e", "a", "i", "e"],
    ["farabutt+",       "o", "a", "i", "e"],
    ["gaglioff+",       "o", "a", "i", "e"],
    ["galleggiant+",    "e", "e", "i", "i"],
    ["gaymer",          "", "", "", ""],
    ["grandissim+",     "o", "a", "i", "e"],
    ["grass+",          "o", "a", "i", "e"],
    ["gross+",          "o", "a", "i", "e"],
    ["ignobil+",        "e", "e", "i", "i"],
    ["ignorant+",       "e", "e", "i", "i"],
    ["imbroglion+",     "e", "a", "i", "e"],
    ["impertinent+",    "e", "e", "i", "i"],
    ["incapac+",        "e", "e", "i", "i"],
    ["incivil+",        "e", "e", "i", "i"],
    ["infam+ (per te solo le lame)", "", "", "i", "i"],
    ["infett+",         "o", "a", "i", "e"],
    ["insensat+",       "o", "a", "i", "e"],
    ["internet explorer", "", "", "", ""],
    ["intollerant+ al lattosio", "e", "e", "i", "i"],
    ["lavativ+",        "o", "a", "i", "e"],
    ["lazzaron+",       "e", "a", "i", "e"],
    ["lent+",           "o", "a", "i", "e"],
    ["lestofant+",      "e", "e", "i", "i"],
    ["lunatic+",        "o", "a", "i", "he"],
    ["maial+",          "e", "a", "i", "e"],
    ["mangiapane a tradimento", "", "", "", ""],
    ["manigold+",       "o", "a", "i", "e"],
    ["marran+",         "o", "a", "i", "e"],
    ["marzian+",        "o", "a", "i", "e"],
    ["mentecatt+",      "o", "a", "i", "e"],
    ["mascalzon+",      "e", "a", "i", "e"],
    ["meschin+",        "o", "a", "i", "e"],
    ["nanerottol+",     "o", "a", "i", "e"],
    ["nichilist+",      "a", "a", "i", "e"],
    ["noios+",          "o", "a", "i", "e"],
    ["novax",           "", "", "", ""],
    ["opulent+",        "o", "a", "i", "e"],
    ["palindrom+",      "o", "a", "i", "e"],
    ["pantagruelic+",   "o", "a", "i", "he"],
    ["pigr+",           "o", "a", "i", "e"],
    ["pivell+",         "o", "a", "i", "e"],
    ["poliedric+",      "o", "a", "i", "he"],
    ["porc+",           "o", "a", "i", "he"],
    ["pusillanim+",     "e", "e", "i", "i"],
    ["puzzolent+",      "e", "e", "i", "i"],
    ["puzzon+",         "e", "a", "i", "e"],
    ["quadrat+",        "o", "a", "i", "e"],
    ["rygat+",          "o", "a", "i", "e"],
    ["rygaton+",        "e", "a", "i", "e"],
    ["rozz+",           "o", "a", "i", "e"],
    ["saccent+",        "e", "e", "i", "i"],
    ["sant+",           "o", "a", "i", "e"],
    ["satur+",          "o", "a", "i", "e"],
    ["scalz+ nella valle dei chiodi", "o", "a", "i", "e"],
    ["sciachimist+",    "a", "a", "i", "e"],
    ["screanzat+",      "o", "a", "i", "e"],
    ["sferic+",         "o", "a", "i", "e"],
    ["sgarbat+",        "o", "a", "i", "e"],
    ["stupid+",         "o", "a", "i", "e"],
    ["stellar+",        "e", "e", "i", "i"],
    ["tamarr+",         "o", "a", "i", "e"],
    ["tard+",           "o", "a", "i", "e"],
    ["terrapiattist+",  "a", "a", "i", "e"],
    ["tirchi+",         "o", "a", "i", "e"],
    ["troglodit+",      "a", "a", "i", "e"],
    ["tuamammic+",      "o", "a", "i", "he"],
    ["vecch+",          "io", "ia", "i", "ie"],
    ["vegan+",          "o", "a", "i", "e"],
    ["vegetarian+",     "o", "a", "i", "e"],
    ["vil+",            "e", "e", "i", "i"],
    ["villan+",         "o", "a", "i", "e"],
    ["viscid+",         "o", "a", "i", "e"],
    ["zotic+",          "o", "a", "i", "he"],
]


@rb.capture_errors
@engi.TeleportingConversation
async def diobot(*, _msg: engi.Message, **__):
    """
    Il bot è molto arrabbiato e vuole creare insulti coloriti!
    """
    who = random.sample(WHO, 1)[0]
    message = "🤬 " + who[1]
    for i in range(random.randint(1, 5)):
        what = random.sample(WHAT, 1)[0]
        what = what[0].replace("+", what[who[0]])
    
        message += " "
        message += what
    message += "!"

    await _msg.reply(text=message)


# Objects exported by this module
__all__ = (
    "diobot",
)

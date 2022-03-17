import random

import royalnet.engineer as engi

import royalpack.bolts as rb

from collections import namedTuple


# A chi sarà diretto l'insulto
WHO = namedTuple('WHO', ['Name', 'Gender']) 

# Gender:
# SM    Singolare Maschile
# SF    Singolare Femminile
# PM    Plurale Maschile
# PF    Plurale Femminile


# l'aggettivo per descrivere il soggetto
# Non deve essere per forza un insulto, anche qualche neutro è bene accetto e dà quel po' di random in più
WHAT = namedTuple('WHAT', ['Radix', 'SM', 'SF', 'PM', 'PF'])

WhoArray = [
    WHO("Dio",        "SM"),
    WHO("Zio",        "SM"),
    WHO("Gesù",       "SM"),
    WHO("Cristo",     "SM"),
    WHO("Maria",      "SF"),
    WHO("Madonna",    "SF"),
    WHO("Eva",        "SF"),
    WHO("Adamo",      "SM"),
    WHO("Rettore",    "SM"),
    WHO("Steffo",     "SM"),
    WHO("Bot",        "SM"),
    WHO("Telegram",   "SM"),
    WHO("Discord",    "SM"),
    WHO("Rygatoni",   "PM"),
    WHO("Moderatori", "PM"),
]

WhatArray = [
    WHAT("aguzzin+",                    "o",    "a",    "i",    "e"),
    WHAT("alcolizzat+",                 "o",    "a",    "i",    "e"),
    WHAT("alt+",                        "o",    "a",    "i",    "e"),
    WHAT("antic+",                      "o",    "a",    "hi",   "he"),
    WHAT("aggressiv+",                  "o",    "a",    "i",    "e"),
    WHAT("bass+",                       "o",    "a",    "i",    "e"),
    WHAT("besti+",                      "a",    "a",    "e",    "e"),
    WHAT("boia",                        "",     "",     "",     ""),
    WHAT("bischer+",                    "o",    "a",    "i",    "e"),
    WHAT("briccon+",                    "e",    "a",    "i",    "e"),
    WHAT("brontolon+",                  "e",    "a",    "i",    "e"),
    WHAT("brutt+",                      "o",    "a",    "i",    "e"),
    WHAT("buggat+",                     "o",    "a",    "i",    "e"),
    WHAT("buon+",                       "o",    "a",    "i",    "e"),
    WHAT("buzzurr+",                    "o",    "a",    "i",    "e"),
    WHAT("canagli+",                    "a",    "a",    "e",    "e"),
    WHAT("ca+",                         "ne",   "gna",  "ni",   "gne"),
    WHAT("cangur+ nella landa dei soffitti bassi",  "o",    "a",    "i",    "e"),
    WHAT("capr+",                       "a",    "a",    "e",    "e"),
    WHAT("carnivor+",                   "o",    "a",    "i",    "e"),
    WHAT("ciambelliform+",              "e",    "e",    "i",    "i"),
    WHAT("citrull+",                    "o",    "a",    "i",    "e"),
    WHAT("codard+",                     "o",    "a",    "i",    "e"),
    WHAT("complottist+",                "a",    "a",    "i",    "e"),
    WHAT("creazionist+",                "a",    "a",    "i",    "e"),
    WHAT("dalle ossa grosse",           "",     "",     "",     ""),
    WHAT("dannunzian+",                 "o",    "a",    "i",    "e"),
    WHAT("disonest+",                   "o",    "a",    "i",    "e"),
    WHAT("disordinat+",                 "o",    "a",    "i",    "e"),
    WHAT("egocentric+",                 "o",    "a",    "i",    "e"),
    WHAT("esatt+ delle tasse",          "ore",  "rice", "ori",  "rici"),
    WHAT("espans+",                     "o",    "a",    "i",    "e"),
    WHAT("fannullon+",                  "e",    "a",    "i",    "e"),
    WHAT("farabutt+",                   "o",    "a",    "i",    "e"),
    WHAT("gaglioff+",                   "o",    "a",    "i",    "e"),
    WHAT("galleggiant+",                "e",    "e",    "i",    "i"),
    WHAT("gaymer",                      "",     "",     "",     ""),
    WHAT("grandissim+",                 "o",    "a",    "i",    "e"),
    WHAT("grass+",                      "o",    "a",    "i",    "e"),
    WHAT("gross+",                      "o",    "a",    "i",    "e"),
    WHAT("ignobil+",                    "e",    "e",    "i",    "i"),
    WHAT("ignorant+",                   "e",    "e",    "i",    "i"),
    WHAT("imbroglion+",                 "e",    "a",    "i",    "e"),
    WHAT("impertinent+",                "e",    "e",    "i",    "i"),
    WHAT("incapac+",                    "e",    "e",    "i",    "i"),
    WHAT("incivil+",                    "e",    "e",    "i",    "i"),
    WHAT("infam+ (per te solo le lame)","e",    "e",    "i",    "i"),
    WHAT("infett+",                     "o",    "a",    "i",    "e"),
    WHAT("insensat+",                   "o",    "a",    "i",    "e"),
    WHAT("internet explorer",           "",     "",     "",     ""),
    WHAT("intollerant+ al lattosio",    "e",    "e",    "i",    "i"),
    WHAT("lavativ+",                    "o",    "a",    "i",    "e"),
    WHAT("lazzaron+",                   "e",    "a",    "i",    "e"),
    WHAT("lent+",                       "o",    "a",    "i",    "e"),
    WHAT("lestofant+",                  "e",    "e",    "i",    "i"),
    WHAT("lunatic+",                    "o",    "a",    "i",    "he"),
    WHAT("maial+",                      "e",    "a",    "i",    "e"),
    WHAT("mangiapane a tradimento",     "",     "",     "",     ""),
    WHAT("manigold+",                   "o",    "a",    "i",    "e"),
    WHAT("marran+",                     "o",    "a",    "i",    "e"),
    WHAT("marzian+",                    "o",    "a",    "i",    "e"),
    WHAT("mascalzon+",                  "e",    "a",    "i",    "e"),
    WHAT("mentecatt+",                  "o",    "a",    "i",    "e"),
    WHAT("meschin+",                    "o",    "a",    "i",    "e"),
    WHAT("nanerottol+",                 "o",    "a",    "i",    "e"),
    WHAT("nichilist+",                  "a",    "a",    "i",    "e"),
    WHAT("noios+",                      "o",    "a",    "i",    "e"),
    WHAT("novax",                       "",     "",     "",     ""),
    WHAT("opulent+",                    "o",    "a",    "i",    "e"),
    WHAT("palindrom+",                  "o",    "a",    "i",    "e"),
    WHAT("pantagruelic+",               "o",    "a",    "i",    "he"),
    WHAT("pigr+",                       "o",    "a",    "i",    "e"),
    WHAT("pivell+",                     "o",    "a",    "i",    "e"),
    WHAT("poliedric+",                  "o",    "a",    "i",    "he"),
    WHAT("porc+",                       "o",    "a",    "i",    "he"),
    WHAT("pusillanim+",                 "e",    "e",    "i",    "i"),
    WHAT("puzzolent+",                  "e",    "e",    "i",    "i"),
    WHAT("puzzon+",                     "e",    "a",    "i",    "e"),
    WHAT("quadrat+",                    "o",    "a",    "i",    "e"),
    WHAT("rygat+",                      "o",    "a",    "i",    "e"),
    WHAT("rygaton+",                    "e",    "a",    "i",    "e"),
    WHAT("rozz+",                       "o",    "a",    "i",    "e"),
    WHAT("saccent+",                    "e",    "e",    "i",    "i"),
    WHAT("sant+",                       "o",    "a",    "i",    "e"),
    WHAT("satur+",                      "o",    "a",    "i",    "e"),
    WHAT("scalz+ nella valle dei chiodi","o",   "a",    "i",    "e"),
    WHAT("sciachimist+",                "a",    "a",    "i",    "e"),
    WHAT("screanzat+",                  "o",    "a",    "i",    "e"),
    WHAT("sferic+",                     "o",    "a",    "i",    "e"),
    WHAT("sgarbat+",                    "o",    "a",    "i",    "e"),
    WHAT("stupid+",                     "o",    "a",    "i",    "e"),
    WHAT("stellar+",                    "e",    "e",    "i",    "i"),
    WHAT("tamarr+",                     "o",    "a",    "i",    "e"),
    WHAT("tard+",                       "o",    "a",    "i",    "e"),
    WHAT("terrapiattist+",              "a",    "a",    "i",    "e"),
    WHAT("tirchi+",                     "o",    "a",    "i",    "e"),
    WHAT("troglodit+",                  "a",    "a",    "i",    "e"),
    WHAT("tuamammic+",                  "o",    "a",    "i",    "he"),
    WHAT("vecch+",                      "io",   "ia",   "i",    "ie"),
    WHAT("vegan+",                      "o",    "a",    "i",    "e"),
    WHAT("vegetarian+",                 "o",    "a",    "i",    "e"),
    WHAT("vil+",                        "e",    "e",    "i",    "i"),
    WHAT("villan+",                     "o",    "a",    "i",    "e"),
    WHAT("viscid+",                     "o",    "a",    "i",    "e"),
    WHAT("zotic+",                      "o",    "a",    "i",    "he"),

]


@rb.capture_errors
@engi.TeleportingConversation
async def diobot(*, _msg: engi.Message, **__):
    """
    Il bot è molto arrabbiato e vuole creare insulti coloriti!
    """
    who = random.sample(WhoArray, 1)[0]
    message = "🤬 " + who.Name
    for i in range(random.randint(1, 5)):
        what = random.sample(WHAT, 1)[0]
        what = what.Radix.replace("+", getattr(what, who.gender))
    
        message += " "
        message += what
    message += "!"

    await _msg.reply(text=message)


# Objects exported by this module
__all__ = (
    "diobot",
)

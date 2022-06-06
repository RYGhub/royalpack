import random

import royalnet.engineer as engi

import royalpack.bolts as rb

from collections import namedtuple


# A chi sarà diretto l'insulto
Who = namedtuple('Who', ['name', 'gender']) 

# Gender:
# SM    Singolare Maschile
# SF    Singolare Femminile
# PM    Plurale Maschile
# PF    Plurale Femminile


# l'aggettivo per descrivere il soggetto
# Non deve essere per forza un insulto, anche qualche neutro è bene accetto e dà quel po' di random in più
What = namedtuple('What', ['radix', 'sm', 'sf', 'pm', 'pf'])

who_array = [
    Who("Dio",          "sm"),
    Who("Zio",          "sm"),
    Who("Gesù",         "sm"),
    Who("Cristo",       "sm"),
    Who("Adamo",        "sm"),
    Who("Rettore",      "sm"),
    Who("Steffo",       "sm"),
    Who("Bot",          "sm"),
    Who("Telegram",     "sm"),
    Who("Discord",      "sm"),
    Who("Linux",        "sm"),
    Who("Windows",      "sm"),
    Who("MacOS",        "sm"),
    Who("Evangelion",   "sm"),
    Who("Garfield Kart","sm"),
    Who("Governo",      "sm"),
    Who("Senatore",     "sm"),

    Who("Maria",        "sf"),
    Who("Madonna",      "sf"),
    Who("Eva",          "sf"),
    Who("Festà",        "sf"),
    Who("Corriera",     "sf"),
    Who("Insalata",     "sf"),

    Who("Rygatoni",     "pm"),
    Who("Moderatori",   "pm"),
    Who("Organizzatori","pm"),
    Who("Dotari",       "pm"),
    Who("Lollari",      "pm"),
    Who("Fiorygi",      "pm"),

    Who("Zanzare",      "pf"),
    Who("Verdure",      "pf"),
]

what_array = [
    What("aguzzin+",                    "o",    "a",    "i",    "e"),
    What("alcolizzat+",                 "o",    "a",    "i",    "e"),
    What("alt+",                        "o",    "a",    "i",    "e"),
    What("antic+",                      "o",    "a",    "hi",   "he"),
    What("aggressiv+",                  "o",    "a",    "i",    "e"),
    What("bass+",                       "o",    "a",    "i",    "e"),
    What("besti+",                      "a",    "a",    "e",    "e"),
    What("boia",                        "",     "",     "",     ""),
    What("bischer+",                    "o",    "a",    "i",    "e"),
    What("briccon+",                    "e",    "a",    "i",    "e"),
    What("brontolon+",                  "e",    "a",    "i",    "e"),
    What("brutt+",                      "o",    "a",    "i",    "e"),
    What("buggat+",                     "o",    "a",    "i",    "e"),
    What("buon+",                       "o",    "a",    "i",    "e"),
    What("buzzurr+",                    "o",    "a",    "i",    "e"),
    What("canagli+",                    "a",    "a",    "e",    "e"),
    What("ca+",                         "ne",   "gna",  "ni",   "gne"),
    What("cangur+ nella landa dei soffitti bassi",  "o",    "a",    "i",    "e"),
    What("capr+",                       "a",    "a",    "e",    "e"),
    What("carnivor+",                   "o",    "a",    "i",    "e"),
    What("ciambelliform+",              "e",    "e",    "i",    "i"),
    What("citrull+",                    "o",    "a",    "i",    "e"),
    What("codard+",                     "o",    "a",    "i",    "e"),
    What("complottist+",                "a",    "a",    "i",    "e"),
    What("creazionist+",                "a",    "a",    "i",    "e"),
    What("dalle ossa grosse",           "",     "",     "",     ""),
    What("dannunzian+",                 "o",    "a",    "i",    "e"),
    What("disonest+",                   "o",    "a",    "i",    "e"),
    What("disordinat+",                 "o",    "a",    "i",    "e"),
    What("egocentric+",                 "o",    "a",    "i",    "e"),
    What("esatt+ delle tasse",          "ore",  "rice", "ori",  "rici"),
    What("espans+",                     "o",    "a",    "i",    "e"),
    What("fannullon+",                  "e",    "a",    "i",    "e"),
    What("farabutt+",                   "o",    "a",    "i",    "e"),
    What("gaglioff+",                   "o",    "a",    "i",    "e"),
    What("galleggiant+",                "e",    "e",    "i",    "i"),
    What("gaymer",                      "",     "",     "",     ""),
    What("grandissim+",                 "o",    "a",    "i",    "e"),
    What("grass+",                      "o",    "a",    "i",    "e"),
    What("gross+",                      "o",    "a",    "i",    "e"),
    What("ignobil+",                    "e",    "e",    "i",    "i"),
    What("ignorant+",                   "e",    "e",    "i",    "i"),
    What("imbroglion+",                 "e",    "a",    "i",    "e"),
    What("impertinent+",                "e",    "e",    "i",    "i"),
    What("incapac+",                    "e",    "e",    "i",    "i"),
    What("incivil+",                    "e",    "e",    "i",    "i"),
    What("infam+ (per te solo le lame)","e",    "e",    "i",    "i"),
    What("infett+",                     "o",    "a",    "i",    "e"),
    What("insensat+",                   "o",    "a",    "i",    "e"),
    What("internet explorer",           "",     "",     "",     ""),
    What("intollerant+ al lattosio",    "e",    "e",    "i",    "i"),
    What("lavativ+",                    "o",    "a",    "i",    "e"),
    What("lazzaron+",                   "e",    "a",    "i",    "e"),
    What("lent+",                       "o",    "a",    "i",    "e"),
    What("lestofant+",                  "e",    "e",    "i",    "i"),
    What("lunatic+",                    "o",    "a",    "i",    "he"),
    What("maial+",                      "e",    "a",    "i",    "e"),
    What("mangiapane a tradimento",     "",     "",     "",     ""),
    What("manigold+",                   "o",    "a",    "i",    "e"),
    What("marran+",                     "o",    "a",    "i",    "e"),
    What("marzian+",                    "o",    "a",    "i",    "e"),
    What("mascalzon+",                  "e",    "a",    "i",    "e"),
    What("mentecatt+",                  "o",    "a",    "i",    "e"),
    What("meschin+",                    "o",    "a",    "i",    "e"),
    What("nanerottol+",                 "o",    "a",    "i",    "e"),
    What("nichilist+",                  "a",    "a",    "i",    "e"),
    What("noios+",                      "o",    "a",    "i",    "e"),
    What("novax",                       "",     "",     "",     ""),
    What("opulent+",                    "o",    "a",    "i",    "e"),
    What("palindrom+",                  "o",    "a",    "i",    "e"),
    What("pantagruelic+",               "o",    "a",    "i",    "he"),
    What("pigr+",                       "o",    "a",    "i",    "e"),
    What("pivell+",                     "o",    "a",    "i",    "e"),
    What("poliedric+",                  "o",    "a",    "i",    "he"),
    What("porc+",                       "o",    "a",    "i",    "he"),
    What("pusillanim+",                 "e",    "e",    "i",    "i"),
    What("puzzolent+",                  "e",    "e",    "i",    "i"),
    What("puzzon+",                     "e",    "a",    "i",    "e"),
    What("quadrat+",                    "o",    "a",    "i",    "e"),
    What("rygat+",                      "o",    "a",    "i",    "e"),
    What("rygaton+",                    "e",    "a",    "i",    "e"),
    What("rozz+",                       "o",    "a",    "i",    "e"),
    What("saccent+",                    "e",    "e",    "i",    "i"),
    What("sant+",                       "o",    "a",    "i",    "e"),
    What("satur+",                      "o",    "a",    "i",    "e"),
    What("scalz+ nella valle dei chiodi","o",   "a",    "i",    "e"),
    What("sciachimist+",                "a",    "a",    "i",    "e"),
    What("screanzat+",                  "o",    "a",    "i",    "e"),
    What("sferic+",                     "o",    "a",    "i",    "e"),
    What("sgarbat+",                    "o",    "a",    "i",    "e"),
    What("stupid+",                     "o",    "a",    "i",    "e"),
    What("stellar+",                    "e",    "e",    "i",    "i"),
    What("tamarr+",                     "o",    "a",    "i",    "e"),
    What("tard+",                       "o",    "a",    "i",    "e"),
    What("terrapiattist+",              "a",    "a",    "i",    "e"),
    What("tirchi+",                     "o",    "a",    "i",    "e"),
    What("troglodit+",                  "a",    "a",    "i",    "e"),
    What("tuamammic+",                  "o",    "a",    "i",    "he"),
    What("vecch+",                      "io",   "ia",   "i",    "ie"),
    What("vegan+",                      "o",    "a",    "i",    "e"),
    What("vegetarian+",                 "o",    "a",    "i",    "e"),
    What("vil+",                        "e",    "e",    "i",    "i"),
    What("villan+",                     "o",    "a",    "i",    "e"),
    What("viscid+",                     "o",    "a",    "i",    "e"),
    What("zotic+",                      "o",    "a",    "i",    "he"),
]


@rb.capture_errors
@engi.TeleportingConversation
async def diobot(*, _msg: engi.Message, **__):
    """
    Il bot è molto arrabbiato e vuole creare insulti coloriti!
    """
    who = random.sample(who_array, 1)[0]
    message = "🤬 " + who.name
    for i in range(random.randint(1, 5)):
        what = random.sample(what_array, 1)[0]
        what = what.radix.replace("+", getattr(what, who.gender))
        message += " "
        message += what
    message += "!"

    await _msg.reply(text=message)


# Objects exported by this module
__all__ = (
    "diobot",
)


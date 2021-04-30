import io

import aiohttp
import royalnet.engineer as engi
import royalpack.bolts as rb


@rb.capture_errors
@engi.TeleportingConversation
async def dog_any(*, _msg: engi.Message, **__):
    """
    Invia un doggo in chat! 🐶
    """
    async with aiohttp.ClientSession() as session:
        async with session.get("https://dog.ceo/api/breeds/image/random") as response:
            result = await response.json()
            url = result["message"]
        async with session.get(url) as response:
            img = await response.content.read()
    await _msg.reply(files=[io.BytesIO(img)])


_breeds = [
    "affenpinscher",
    "african",
    "airedale",
    "akita",
    "appenzeller",
    "australian/shepherd",
    "basenji",
    "beagle",
    "bluetick",
    "borzoi",
    "bouvier",
    "boxer",
    "brabancon",
    "briard",
    "buhund/norwegian",
    "bulldog/boston",
    "bulldog/english",
    "bulldog/french",
    "bullterrier/staffordshire",
    "cairn",
    "cattledog/australian",
    "chihuahua",
    "chow",
    "clumber",
    "cockapoo",
    "collie/border",
    "coonhound",
    "corgi/cardigan",
    "cotondetulear",
    "dachshund",
    "dalmatian",
    "dane/great",
    "deerhound/scottish",
    "dhole",
    "dingo",
    "doberman",
    "elkhound/norwegian",
    "entlebucher",
    "eskimo",
    "finnish/lapphund",
    "frise/bichon",
    "germanshepherd",
    "greyhound/italian",
    "groenendael",
    "havanese",
    "hound/afghan",
    "hound/basset",
    "hound/blood",
    "hound/english",
    "hound/ibizan",
    "hound/plott",
    "hound/walker",
    "husky",
    "keeshond",
    "kelpie",
    "komondor",
    "kuvasz",
    "labrador",
    "leonberg",
    "lhasa",
    "malamute",
    "malinois",
    "maltese",
    "mastiff/bull",
    "mastiff/english",
    "mastiff/tibetan",
    "mexicanhairless",
    "mix",
    "mountain/bernese",
    "mountain/swiss",
    "newfoundland",
    "otterhound",
    "ovcharka/caucasian",
    "papillon",
    "pekinese",
    "pembroke",
    "pinscher/miniature",
    "pitbull",
    "pointer/german",
    "pointer/germanlonghair",
    "pomeranian",
    "poodle/miniature",
    "poodle/standard",
    "poodle/toy",
    "pug",
    "puggle",
    "pyrenees",
    "redbone",
    "retriever/chesapeake",
    "retriever/curly",
    "retriever/flatcoated",
    "retriever/golden",
    "ridgeback/rhodesian",
    "rottweiler",
    "saluki",
    "samoyed",
    "schipperke",
    "schnauzer/giant",
    "schnauzer/miniature",
    "setter/english",
    "setter/gordon",
    "setter/irish",
    "sheepdog/english",
    "sheepdog/shetland",
    "shiba",
    "shihtzu",
    "spaniel/blenheim",
    "spaniel/brittany",
    "spaniel/cocker",
    "spaniel/irish",
    "spaniel/japanese",
    "spaniel/sussex",
    "spaniel/welsh",
    "springer/english",
    "stbernard",
    "terrier/american",
    "terrier/australian",
    "terrier/bedlington",
    "terrier/border",
    "terrier/dandie",
    "terrier/fox",
    "terrier/irish",
    "terrier/kerryblue",
    "terrier/lakeland",
    "terrier/norfolk",
    "terrier/norwich",
    "terrier/patterdale",
    "terrier/russell",
    "terrier/scottish",
    "terrier/sealyham",
    "terrier/silky",
    "terrier/tibetan",
    "terrier/toy",
    "terrier/westhighland",
    "terrier/wheaten",
    "terrier/yorkshire",
    "vizsla",
    "waterdog/spanish",
    "weimaraner",
    "whippet",
    "wolfhound/irish",
]


@engi.TeleportingConversation
async def dog_breed(*, _msg: engi.Message, breed: str, **__):
    """
    Invia un doggo di una razza specifica in chat! 🐶
    """
    breed = breed.lower()
    if breed not in _breeds:
        await _msg.reply(text="⚠️ La razza che hai specificato non esiste nel database.")

    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://dog.ceo/api/breed/{breed}/images/random") as response:
            result = await response.json()
            url = result["message"]
        async with session.get(url) as response:
            img = await response.content.read()
    await _msg.reply(files=[io.BytesIO(img)])


@engi.TeleportingConversation
async def dog_breedlist(*, _msg: engi.Message, **__):
    """
    Elenca tutte le razze di dogghi disponibili! 🐶
    """
    msg = [
        "🐶 \uE01BRazze disponibili:\uE00B",
        ", ".join(_breeds),
    ]

    await _msg.reply(text="\n".join(msg))


__all__ = ("dog_any", "dog_breed", "dog_breedlist")

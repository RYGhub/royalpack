import datetime
import random

import royalnet.engineer as engi

import royalpack.bolts as rb


@rb.capture_errors
@engi.TeleportingConversation
async def roll(*, _msg: engi.Message, qty: int, die: int, mod: int, **__):
    """
    Tira un dado nel formato di D&D: `1d20+1`, ad esempio.
    """

    # modificatore supersegreto della fortuna. Ooooh! Questo è Top Secret!
    # Steffo: hol up
    r = random.Random(x=hash(datetime.date.today()))
    luck = r.randrange(-100, 100)/100*die/3

    random.seed(datetime.datetime.now())

    # rolliamo i dadi richiesti
    roll = []
    for i in range(quantity):
        extracted = random.randint(1, die)

        result = int(round(extracted+luck, 0))
        result = min(result, die)
        result = max(result, 1)

        roll.append(result)

    # formuliamo una risposta da mostrare all'utente
    answer = f"🎲 {qty}d{die}{mod:+} = {roll}"
    if mod:
        answer +=" "
        if mod > 0:
            answer += "+"
        answer +=str(mod)
    
    answer += " = "+str(sum(roll)+mod)

    await _msg.reply(text=answer)



__all__ = ("roll",)
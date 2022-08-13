from email import message
import datetime
import random
import re

import royalnet.engineer as engi

import royalpack.bolts as rb


@rb.capture_errors
@engi.TeleportingConversation
async def roll(*, _msg: engi.Message, message: str, **__):
    """
    Tira un dado
    """

    if not re.match("[0-9]*d[0-9]+(\+[0-9])?(\-[0-9])?", message):
        await _msg.reply(text="❗️ Errore: la stringa deve rispettare il pattern [quantity]d[die][modifier]")

    
    # quantità di dadi
    quantity, die = message.split('d')
    if(message[0] =='d'):
        quantity = 1
    
    # modificatore
    if '+' in message or '-' in message:
        if '+' in message:
            die, modifier = die.split('+')
        else:
            die, modifier = die.split('-')
            modifier = '-'+ modifier
    else:
        modifier = 0    

    # rendiamo tutto un int, se non lo è già
    quantity = int(quantity)
    die = int(die)
    modifier = int(modifier)

    # modificatore supersegreto della fortuna. Ooooh! Questo è Top Secret!
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
    answer = "🎲 " + message + " = "
    answer += str(roll)
    if modifier:
        answer +=" "
        if modifier > 0:
            answer += "+"
        answer +=str(modifier)
    
    answer += " = "+str(sum(roll)+modifier)

    await _msg.reply(text=answer)



__all__ = ("roll",)
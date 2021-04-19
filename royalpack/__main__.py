import royalnet.engineer as engi
from royalnet.engineer import router
import royalnet.scrolls as sc
import royalnet_telethon as rt
import pathlib
import re
import coloredlogs

from . import commands
from .database import engine, base

coloredlogs.install(level="DEBUG", isatty=True)
config = sc.Scroll.from_file(namespace="ROYALPACK", file_path=pathlib.Path("royalpack.cfg.toml"))

engine_ = engine.lazy_engine.evaluate()
base.Base.metadata.create_all(engine_)

pda = engi.PDA(implementations=[
    rt.TelethonPDAImplementation(
        name="1",
        tg_api_id=config["telegram.api.id"],
        tg_api_hash=config["telegram.api.hash"],
        bot_username=config["telegram.bot.username"],
        bot_token=config["telegram.bot.token"],
    )
])

r = router.Router()


def register_telegram(conv, names, syntax=None):
    name_regex = rf"(?:{'|'.join(names)})"
    bot_regex = rf"(?:@{config['telegram.bot.username']})?"
    if syntax:
        syntax_regex = f" {syntax}"
    else:
        syntax_regex = ""
    regex = rf"^/{name_regex}{bot_regex}{syntax_regex}$"
    r.register_conversation(conv, names, [re.compile(regex)])


register_telegram(commands.ahnonlosoio, ["ahnonlosoio"])
register_telegram(commands.answer, ["answer"], r".+")
register_telegram(commands.cat, ["cat"])
register_telegram(commands.ciaoruozi, ["ciaoruozi"])
register_telegram(commands.color, ["color"])
register_telegram(commands.ping, ["ping"])
register_telegram(commands.ship, ["ship"], r"(?P<first>[A-Za-z]+)[\s+&]+(?P<second>[A-Za-z]+)")
register_telegram(commands.emojify, ["emojify"], r"(?P<message>.+)")
register_telegram(commands.dog_any, ["dog"])
register_telegram(commands.dog_breedlist, ["dog"], "(?:list|help|aiuto)")
register_telegram(commands.dog_breed, ["dog"], "(?P<breed>[A-Za-z/]+)")
register_telegram(commands.fortune, ["fortune"])
register_telegram(commands.pmots, ["pmots"])
register_telegram(commands.spell, ["spell"], "(?P<spellname>.+)")
register_telegram(commands.smecds, ["smecds"])
register_telegram(commands.man, ["man", "help"], "(?P<commandname>[A-Za-z]+)")
register_telegram(commands.login, ["login"])


pda.implementations["telethon.1"].register_conversation(r)


pda.run()

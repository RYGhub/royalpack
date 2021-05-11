import discord
import pkg_resources
import royalnet.engineer as engi
import royalnet.scrolls as sc
import royalnet_telethon as rt
import royalnet_discordpy as rd
import pathlib
import re
import coloredlogs
import sentry_sdk
import sentry_sdk.integrations.atexit
import sentry_sdk.integrations.dedupe
import sentry_sdk.integrations.modules
import sentry_sdk.integrations.threading
import logging

from . import commands
from .database import engine, base

coloredlogs.install(level="DEBUG" if __debug__ else "INFO", isatty=True)
config = sc.Scroll.from_file(namespace="ROYALPACK", file_path=pathlib.Path("royalpack.cfg.toml"))

if dsn := config.get("sentry.dsn", None):
    logging.info("Enabling Sentry...")
    sentry_sdk.init(
        dsn=dsn,
        debug=__debug__,
        release=pkg_resources.get_distribution("royalpack").version,
        environment="Development" if __debug__ else "Production",
        default_integrations=False,
        integrations=[
            sentry_sdk.integrations.atexit.AtexitIntegration(),
            sentry_sdk.integrations.dedupe.DedupeIntegration(),
            sentry_sdk.integrations.modules.ModulesIntegration(),
            sentry_sdk.integrations.threading.ThreadingIntegration(),
        ],
        traces_sample_rate=1.0
    )

engine_ = engine.lazy_engine.evaluate()
base.Base.metadata.create_all(engine_)

pda = engi.PDA(implementations=[
    rt.TelethonPDAImplementation(
        name="1",
        tg_api_id=config["telegram.api.id"],
        tg_api_hash=config["telegram.api.hash"],
        bot_username=config["telegram.bot.username"],
        bot_token=config["telegram.bot.token"],
    ),
    rd.DiscordpyPDAImplementation(
        name="2",
        bot_token=config["discord.bot.token"],
        intents=discord.Intents.all(),
    ),
])


def register_telegram(router, conv, names, syntax=None):
    name_regex = rf"(?:{'|'.join(names)})"
    bot_regex = rf"(?:@{config['telegram.bot.username']})?"
    if syntax:
        syntax_regex = rf"\s+{syntax}"
    else:
        syntax_regex = ""
    regex = rf"^/{name_regex}{bot_regex}{syntax_regex}$"
    router.register_conversation(conv, names, [re.compile(regex)])


def register_discord(router, conv, names, syntax=None):
    name_regex = rf"(?:{'|'.join(names)})"
    if syntax:
        syntax_regex = rf"\s+{syntax}"
    else:
        syntax_regex = ""
    prefix_regex = rf"{config['discord.bot.prefix']}"
    regex = rf"^{prefix_regex}{name_regex}{syntax_regex}$"
    router.register_conversation(conv, names, [re.compile(regex)])


tg_router = engi.Router()

register_telegram(tg_router, commands.ahnonlosoio, ["ahnonlosoio"])
register_telegram(tg_router, commands.answer, ["answer"], r".+")
register_telegram(tg_router, commands.cat, ["cat", "catto", "gatto", "nyaa", "nya"])
register_telegram(tg_router, commands.ciaoruozi, ["ciaoruozi"])
register_telegram(tg_router, commands.color, ["color"])
register_telegram(tg_router, commands.ping, ["ping"])
register_telegram(tg_router, commands.ship, ["ship"], r"(?P<first>[A-Za-z]+)[\s+&]+(?P<second>[A-Za-z]+)")
register_telegram(tg_router, commands.emojify, ["emojify"], r"(?P<message>.+)")
register_telegram(tg_router, commands.dog_any, ["dog", "doggo", "cane", "woof", "bau"])
register_telegram(tg_router, commands.dog_breedlist, ["dog", "doggo", "cane", "woof", "bau"], r"(?:list|help|aiuto)")
register_telegram(tg_router, commands.dog_breed, ["dog", "doggo", "cane", "woof", "bau"], r"(?P<breed>[A-Za-z/]+)")
register_telegram(tg_router, commands.fortune, ["fortune"])
register_telegram(tg_router, commands.pmots, ["pmots"])
register_telegram(tg_router, commands.spell, ["spell", "cast"], r"(?P<spellname>.+)")
register_telegram(tg_router, commands.smecds, ["smecds"])
register_telegram(tg_router, commands.man, ["man", "help"], r"(?P<commandname>[A-Za-z]+)")
register_telegram(tg_router, commands.login, ["login"])
register_telegram(tg_router, commands.whoami, ["whoami"])
register_telegram(tg_router, commands.fiorygi_balance_self, ["balance"])
register_telegram(tg_router, commands.fiorygi_balance_other, ["balance"], r"(?P<target>\S+)")
register_telegram(tg_router, commands.fiorygi_give, ["give"], r"(?P<target>\S+)\s+(?P<amount>[0-9]+)\s+(?P<reason>.+)")
register_telegram(tg_router, commands.fiorygi_magick, ["magick"], r"(?P<target>\S+)\s+(?P<amount>[0-9]+)\s+(?P<reason>.+)")
register_telegram(tg_router, commands.fiorygi_transactions_self, ["transactions"])
register_telegram(tg_router, commands.fiorygi_transactions_other, ["transactions"], r"(?P<target>\S+)")
register_telegram(tg_router, commands.fiorygi_dig, ["dig"], r"(?P<slug>[a-z0-9-]+)")
register_telegram(tg_router, commands.fiorygi_bury, ["bury"], r"(?P<slug>[a-z0-9-]+)\s+(?P<value>[0-9]+)(?:\s+(?P<message>.+))?")
register_telegram(tg_router, commands.version, ["version"])
register_telegram(tg_router, commands.cv, ["cv", "civù"])
register_telegram(tg_router, commands.rocoinflip, ["rocoinflip"], r'"(?P<teama>[^"]+)"\s+"(?P<teamb>[^"]+)"')

ds_router = engi.Router()

register_discord(ds_router, commands.ahnonlosoio, ["ahnonlosoio"])
register_discord(ds_router, commands.answer, ["answer"], r".+")
register_discord(ds_router, commands.cat, ["cat", "catto", "gatto", "nyaa", "nya"])
register_discord(ds_router, commands.ciaoruozi, ["ciaoruozi"])
register_discord(ds_router, commands.color, ["color"])
register_discord(ds_router, commands.ping, ["ping"])
register_discord(ds_router, commands.ship, ["ship"], r"(?P<first>[A-Za-z]+)[\s+&]+(?P<second>[A-Za-z]+)")
register_discord(ds_router, commands.emojify, ["emojify"], r"(?P<message>.+)")
register_discord(ds_router, commands.dog_any, ["dog", "doggo", "cane", "woof", "bau"])
register_discord(ds_router, commands.dog_breedlist, ["dog", "doggo", "cane", "woof", "bau"], r"(?:list|help|aiuto)")
register_discord(ds_router, commands.dog_breed, ["dog", "doggo", "cane", "woof", "bau"], r"(?P<breed>[A-Za-z/]+)")
register_discord(ds_router, commands.fortune, ["fortune"])
register_discord(ds_router, commands.pmots, ["pmots"])
register_discord(ds_router, commands.spell, ["spell", "cast"], r"(?P<spellname>.+)")
register_discord(ds_router, commands.smecds, ["smecds"])
register_discord(ds_router, commands.man, ["man", "help"], r"(?P<commandname>[A-Za-z]+)")
register_discord(ds_router, commands.login, ["login"])
register_discord(ds_router, commands.whoami, ["whoami"])
register_discord(ds_router, commands.fiorygi_balance_self, ["balance"])
register_discord(ds_router, commands.fiorygi_balance_other, ["balance"], r"(?P<target>\S+)")
register_discord(ds_router, commands.fiorygi_give, ["give"], r"(?P<target>\S+)\s+(?P<amount>[0-9]+)\s+(?P<reason>.+)")
register_discord(ds_router, commands.fiorygi_magick, ["magick"], r"(?P<target>\S+)\s+(?P<amount>[0-9]+)\s+(?P<reason>.+)")
register_discord(ds_router, commands.fiorygi_transactions_self, ["transactions"])
register_discord(ds_router, commands.fiorygi_transactions_other, ["transactions"], r"(?P<target>\S+)")
register_discord(ds_router, commands.fiorygi_dig, ["dig"], r"(?P<slug>[a-z0-9-]+)")
register_discord(ds_router, commands.fiorygi_bury, ["bury"], r"(?P<slug>[a-z0-9-]+)\s+(?P<value>[0-9]+)(?:\s+(?P<message>.+))?")
register_discord(ds_router, commands.version, ["version"])
register_discord(ds_router, commands.rocoinflip, ["rocoinflip"], r'"(?P<teama>[^"]+)"\s+"(?P<teamb>[^"]+)"')
register_discord(ds_router, commands.hack, ["hack"], r'(?P<activity>.+)')

pda.implementations["telethon.1"].register_conversation(tg_router)
pda.implementations["discordpy.2"].register_conversation(ds_router)


pda.run()

import royalnet.engineer as engi
import royalnet.scrolls as sc
import royalnet_telethon as rt
import pathlib
import asyncio
import logging

from . import commands

logging.basicConfig(level="DEBUG")

config = sc.Scroll.from_file(namespace="ROYALPACK", file_path=pathlib.Path("config.toml"))

pda = rt.TelethonPDA(
    tg_api_id=config["tapi.id"],
    tg_api_hash=config["tapi.hash"],
    bot_username=config["tapi.username"],
)

pda.register_partial(commands.ahnonlosoio, ["ahnonlosoio"])
pda.register_partial(commands.answer, ["answer"])
pda.register_partial(commands.cat, ["cat"])
pda.register_partial(commands.color, ["color"])
pda.register_partial(commands.ping, ["ping"])
pda.register_partial(commands.ship, ["ship"])


loop = asyncio.get_event_loop()
loop.run_until_complete(
    pda.run(
        bot_token=config["tapi.token"],
    )
)

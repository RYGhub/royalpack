import royalnet.engineer as engi
import royalnet.scrolls as sc
import royalnet_console as rc
import royalnet_telethon as rt
import pathlib
import coloredlogs

from . import commands
from .database import engine, base

coloredlogs.install(level="DEBUG", isatty=True)

config = sc.Scroll.from_file(namespace="ROYALPACK", file_path=pathlib.Path("royalpack.cfg.toml"))

engine_ = engine.lazy_engine.evaluate()
base.Base.metadata.create_all(engine_)

pda = engi.PDA(implementations=[
    # rc.ConsolePDAImplementation(
    #     name="1",
    #     extensions=[
    #         engi.SQLAlchemyExtension(engine=engine_),
    #     ]
    # ),
    rt.TelethonPDAImplementation(
        name="1",
        extensions=[
            engi.SQLAlchemyExtension(engine=engine_),
        ],
        tg_api_id=config["telegram.api.id"],
        tg_api_hash=config["telegram.api.hash"],
        bot_username=config["telegram.bot.username"],
        bot_token=config["telegram.bot.token"],
    )
])

pda.implementations["telethon.1"].register_partialcommand(commands.ahnonlosoio, ["ahnonlosoio"])
pda.implementations["telethon.1"].register_partialcommand(commands.answer, ["answer"])
pda.implementations["telethon.1"].register_partialcommand(commands.cat, ["cat"])
pda.implementations["telethon.1"].register_partialcommand(commands.color, ["color"])
pda.implementations["telethon.1"].register_partialcommand(commands.ping, ["ping"])
pda.implementations["telethon.1"].register_partialcommand(commands.ship, ["ship"])
pda.implementations["telethon.1"].register_partialcommand(commands.rage_show, ["rage"])
pda.implementations["telethon.1"].register_partialcommand(commands.rage_add, ["rage"])


pda.run()

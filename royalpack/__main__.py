import royalnet.engineer as engi
import royalnet.scrolls as sc
import royalnet_console as rc
import pathlib
import logging

from . import commands
from .database import engine, base

logging.basicConfig(level="DEBUG")

config = sc.Scroll.from_file(namespace="ROYALPACK", file_path=pathlib.Path("royalpack.cfg.toml"))

engine_ = engine.lazy_engine.evaluate()
base.Base.metadata.create_all(engine_)

pda = engi.PDA(implementations=[
    rc.ConsolePDAImplementation(name="1", extensions=[
        engi.SQLAlchemyExtension(engine=engine_)
    ])
])

pda.implementations["console.1"].register_partialcommand(commands.ahnonlosoio, ["ahnonlosoio"])
# pda.implementations["console.1"].register_partialcommand(commands.answer, ["answer"])
# pda.implementations["console.1"].register_partialcommand(commands.cat, ["cat"])
# pda.implementations["console.1"].register_partialcommand(commands.color, ["color"])
# pda.implementations["console.1"].register_partialcommand(commands.ping, ["ping"])
# pda.implementations["console.1"].register_partialcommand(commands.ship, ["ship"])
# pda.implementations["console.1"].register_partialcommand(commands.rage_show, ["rage"])
# pda.implementations["console.1"].register_partialcommand(commands.rage_add, ["rage"])


pda.run()

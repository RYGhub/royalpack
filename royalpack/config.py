import pathlib

import royalnet.lazy as l
import royalnet.scrolls as s

lazy_config = l.Lazy(lambda: s.Scroll.from_file("ROYALPACK", pathlib.Path("royalpack.cfg.toml")))

__all__ = (
    "lazy_config",
)

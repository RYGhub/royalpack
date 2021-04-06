import pathlib
import royalnet.scrolls as s
import royalnet.lazy as l


lazy_config = l.Lazy(lambda: s.Scroll.from_file("ROYALPACK", pathlib.Path("royalpack.cfg.toml")))


__all__ = (
    "lazy_config",
)

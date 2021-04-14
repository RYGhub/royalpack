import sqlalchemy.orm
import royalnet.lazy

from ..config import *

# noinspection PyUnresolvedReferences
from . import tables


lazy_engine = royalnet.lazy.Lazy(lambda c: sqlalchemy.create_engine(c["database.uri"]), c=lazy_config)
"""
The uninitialized sqlalchemy engine.
"""

__all__ = (
    "lazy_engine",
)

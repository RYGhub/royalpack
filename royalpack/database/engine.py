import sqlalchemy.orm
import royalnet.lazy

from ..config import *


lazy_engine = royalnet.lazy.Lazy(lambda c: sqlalchemy.create_engine(c["database.uri"]), c=lazy_config)
"""
The uninitialized sqlalchemy engine.
"""

lazy_session_class = royalnet.lazy.Lazy(lambda e: sqlalchemy.orm.sessionmaker(bind=e), e=lazy_engine)
"""
The uninitialized sqlalchemy session class.
"""

SessionType = sqlalchemy.orm.Session

__all__ = (
    "lazy_engine",
    "lazy_session_class",
    "SessionType",
)

"""

"""

from __future__ import annotations

import functools
import logging

import royalnet.engineer as engi
import sqlalchemy.orm as so

import royalpack.database as db

log = logging.getLogger(__name__)


def with_target():
    """
    .. todo:: Document this.
    """

    def decorator(f):
        @functools.wraps(f)
        async def decorated(_msg: engi.Message, _session: so.Session, target: str, **f_kwargs):
            user = db.UserAlias.find(session=_session, string=target)
            if user is None:
                await _msg.reply(text=f"⚠️ L'utente specificato non esiste.")
                return

            return await f(_msg=_msg, _session=_session, **f_kwargs, _target=user)

        return decorated

    return decorator


__all__ = (
    "with_target",
)

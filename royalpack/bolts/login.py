"""

"""

from __future__ import annotations

import functools
import logging

import royalnet.engineer as engi
import royalnet_discordpy
import royalnet_telethon
import sqlalchemy.orm as so
import sqlalchemy.sql as ss

import royalpack.database as db

log = logging.getLogger(__name__)


def use_ryglogin(allow_anonymous=False):
    """
    Decorator factory which allows a :class:`~royalnet.engineer.conversation.Conversation` to find out what RYGaccount
    user called a certain function.

    It requires the :func:`~royalnet.engineer.bolts.use_database` decorator.

    :param allow_anonymous: If users who are not logged in should be allowed to use the command, or should be displayed
                            an error instead.
    :return: The decorator to use to decorate the function.
    """

    def decorator(f):
        @functools.wraps(f)
        async def decorated(_session: so.Session, _imp: engi.PDAImplementation, _msg: engi.Message, **f_kwargs):

            if isinstance(_imp, royalnet_telethon.TelethonPDAImplementation):
                _sender = await _msg.sender
                supported = True
                account = _session.execute(
                    ss.select(db.TelegramAccount).where(db.TelegramAccount.id == _sender._user.id)
                ).scalar()

            elif isinstance(_imp, royalnet_discordpy.DiscordpyPDAImplementation):
                _sender = await _msg.sender
                supported = True
                account = _session.execute(
                    ss.select(db.DiscordAccount).where(db.DiscordAccount.id == _sender._user.id)
                ).scalar()

            else:
                supported = False
                account = None

            if account:
                user = account.user
            else:
                if allow_anonymous:
                    user = None
                else:
                    if supported:
                        await _msg.reply(text=f"⚠️ Non sei loggato al tuo RYGaccount! "
                                              f"Usa il comando login per effettuare la connessione.")
                    else:
                        await _msg.reply(text=f"⚠️ Il login non è disponibile su questa implementazione di Royalnet, "
                                              f"e questo comando non consente l'esecuzione anonima.")
                    return

            return await f(_session=_session, _imp=_imp, _msg=_msg, **f_kwargs, _account=account, _user=user)

        return decorated

    return decorator


__all__ = (
    "use_ryglogin",
)

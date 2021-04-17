import royalnet.engineer as engi
from ..database.tables import Rage
import sqlalchemy as s
import sqlalchemy.orm as so


@engi.TeleportingConversation
async def rage_show(*, _sentry: engi.Sentry, _msg: engi.Message, _session: so.Session, **__):
    """
    A-N-G-E-R-Y!
    Invia in chat qualcosa che ha fatto arrabbiare un membro anonimo della RYG.
    """

    rage = _session.execute(
        s.select(Rage).order_by(s.func.random())
    ).scalar()

    if rage is None:
        await _msg.reply(text=f"😐 Alla fine, non è che sei così arrabbiato...")
    else:
        await _msg.reply(text=f"😡 {rage.reason}")


@engi.TeleportingConversation
async def rage_add(*, _sentry: engi.Sentry, _msg: engi.Message, _session: so.Session, reason: str, **__):
    """
    A-N-G-E-R-Y!
    Aggiungi al database qualcosa che ti ha fatto arrabbiare tantissimo.
    """

    rage = Rage(reason=reason)
    _session.add(rage)
    _session.commit()

    count = _session.execute(
        s.select(s.func.count()).select_from(s.select(Rage).subquery())
    ).scalar()

    await _msg.reply(text=f"😡 G{'R' * count}!")


__all__ = (
    "rage_show",
    "rage_add",
)

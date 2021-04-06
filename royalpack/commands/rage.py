import royalnet.engineer as engi
from ..database.engine import lazy_Session
from ..database.tables import Rage
import sqlalchemy as s


@engi.PartialCommand.new(syntax="")
async def rage_show(*, _sentry: engi.Sentry, _msg: engi.Message, **__):
    """
    A-N-G-E-R-Y!
    Invia in chat qualcosa che ha fatto arrabbiare un membro anonimo della RYG.
    """

    Session = lazy_Session.evaluate()
    with Session(future=True) as session:

        rage = session.execute(
            s.select(Rage).order_by(s.func.random())
        ).scalar()

        if rage is None:
            await _msg.reply(text=f"😐 Alla fine, non è che sei così arrabbiato...")
        else:
            await _msg.reply(text=f"😡 {rage.reason}")


@engi.PartialCommand.new(syntax="(?P<reason>.+)")
async def rage_add(*, _sentry: engi.Sentry, _msg: engi.Message, reason: str, **__):
    """
    A-N-G-E-R-Y!
    Aggiungi al database qualcosa che ti ha fatto arrabbiare tantissimo.
    """
    Session = lazy_Session.evaluate()
    with Session(future=True) as session:

        rage = Rage(reason=reason)
        session.add(rage)
        session.commit()

        count = session.execute(
            s.select(s.func.count()).select_from(s.select(Rage).subquery())
        ).scalar()

        await _msg.reply(text=f"😡 G{'R' * count}!")


__all__ = (
    "rage_show",
    "rage_add",
)

import royalnet.royaltyping as t
import royalnet.engineer as engi
import royalpack.database as db
import royalpack.bolts as rb
import sqlalchemy.sql as ss
import functools
import arrow


@rb.capture_errors
@engi.use_database(db.lazy_session_class)
@rb.use_ryglogin(allow_anonymous=False)
@engi.TeleportingConversation
async def fiorygi_balance_self(*, _user: db.User, _msg: engi.Message, **__):
    """
    Visualizza il tuo portafoglio attuale di fiorygi.
    """

    await _msg.reply(text=f"💰 Attualmente, possiedi \uE01Bƒ {_user.fiorygi}\uE00B.")


@rb.capture_errors
@engi.use_database(db.lazy_session_class)
@rb.with_target()
@engi.TeleportingConversation
async def fiorygi_balance_other(*, _target: db.User, _session: db.SessionType, _msg: engi.Message, **__):
    """
    Visualizza il portafoglio di fiorygi di un altro membro.
    """

    await _msg.reply(text=f"💰 {_target} possiede \uE01Bƒ {_target.fiorygi}\uE00B.")


def render(transaction: db.Transaction, user: db.User):
    row = []

    if transaction.plus == user:
        is_plus = True
        other = transaction.minus
    else:
        is_plus = False
        other = transaction.plus

    if transaction.amount != 0:
        row.append(f"{'➕' if is_plus else '➖'} \uE01Bƒ {transaction.amount}\uE00B")

    if other is not None:
        row.append(f"\uE011{'da' if is_plus else 'a'} {other}\uE001")

    if transaction.reason:
        row.append(f"{transaction.reason}")

    return " - ".join(row)


@rb.capture_errors
@engi.use_database(db.lazy_session_class)
@rb.use_ryglogin(allow_anonymous=False)
@engi.TeleportingConversation
async def fiorygi_transactions_self(*, _session: db.SessionType, _user: db.User, _msg: engi.Message, **__):
    """
    Visualizza le ultime 10 transazioni del tuo portafoglio.
    """

    transactions = _session.execute(
        ss.select(
            db.Transaction
        ).where(
            ss.or_(
                db.Transaction.minus == _user,
                db.Transaction.plus == _user,
            )
        ).order_by(
            db.Transaction.timestamp.desc()
        ).limit(
            10
        )
    ).scalars()

    msg = map(functools.partial(render, user=_user), transactions)

    await _msg.reply(text="\n\n".join(msg))


@rb.capture_errors
@engi.use_database(db.lazy_session_class)
@rb.with_target()
@engi.TeleportingConversation
async def fiorygi_transactions_other(*, _session: db.SessionType, _target: db.User, _msg: engi.Message, **__):
    """
    Visualizza le ultime 10 transazioni del portafoglio di un membro.
    """

    transactions = _session.execute(
        ss.select(
            db.Transaction
        ).where(
            ss.or_(
                db.Transaction.minus == _target,
                db.Transaction.plus == _target,
            )
        ).order_by(
            db.Transaction.timestamp.desc()
        ).limit(
            10
        )
    ).scalars()

    msg = map(functools.partial(render, user=_target), transactions)

    await _msg.reply(text="\n\n".join(msg))


@rb.capture_errors
@engi.use_database(db.lazy_session_class)
@rb.use_ryglogin(allow_anonymous=False)
@rb.with_target()
@engi.TeleportingConversation
async def fiorygi_give(
        *,
        _user: db.User,
        _target: db.User,
        _msg: engi.Message,
        _session: db.SessionType,
        amount: int,
        reason: str,
        **__
):
    """
    Dai dei fiorygi a un altro membro.
    """

    if amount <= 0:
        await _msg.reply(text=f"⚠️ Puoi trasferire solo numeri interi positivi di fiorygi.")
        return

    if _user.fiorygi < amount:
        await _msg.reply(text=f"⚠️ Non hai sufficienti fiorygi per effettuare il trasferimento.")
        return

    if _user == _target:
        await _msg.reply(text=f"⚠️ Non puoi dare fiorygi a te stesso!")
        return

    trans = db.Transaction(
        minus=_user,
        plus=_target,
        amount=amount,
        reason=reason,
    )
    _session.add(trans)

    _user.fiorygi -= amount
    _target.fiorygi += amount

    _session.commit()

    await _msg.reply(text=f"💸 Hai trasferito \uE01Bƒ {amount}\uE00B a {_target}.")


@rb.capture_errors
@engi.use_database(db.lazy_session_class)
@rb.use_ryglogin(allow_anonymous=False)
@rb.with_target()
@engi.TeleportingConversation
async def fiorygi_magick(
        *,
        _user: db.User,
        _target: db.User,
        _msg: engi.Message,
        _session: db.SessionType,
        amount: int,
        reason: str,
        **__
):
    """
    Modifica il portafoglio di fiorygi di un membro.
    """

    if _user.sub != "auth0|5ed2debf7308300c1ea230c3":
        await _msg.reply(text=f"⚠️ Non sei autorizzato ad eseguire questo comando.")
        return

    if amount >= 0:
        trans = db.Transaction(
            minus=None,
            plus=_target,
            amount=amount,
            reason=reason,
        )
    else:
        trans = db.Transaction(
            minus=_target,
            plus=None,
            amount=amount,
            reason=reason,
        )

    _session.add(trans)

    _target.fiorygi += amount

    _session.commit()

    await _msg.reply(text=f"🏦 Hai modificato il portafoglio di {_target} di \uE01Bƒ {amount}\uE00B.")


@rb.capture_errors
@engi.use_database(db.lazy_session_class)
@rb.use_ryglogin(allow_anonymous=False)
@engi.TeleportingConversation
async def fiorygi_dig(
        *,
        _user: db.User,
        _session: db.SessionType,
        _msg: engi.Message,
        slug: str,
        **__
):
    """
    Cerca un tesoro con un dato nome.
    """

    treasure: t.Optional[db.Treasure] = _session.execute(
        ss.select(
            db.Treasure
        ).where(
            db.Treasure.slug == slug
        )
    ).scalar()

    if treasure is None:
        await _msg.reply(text=f"🏝 Non hai trovato nulla.")
        return

    if treasure.finder is not None:
        await _msg.reply(text=f"🏝 Quel tesoro è già stato trovato da {treasure.finder}.")
        return

    treasure.finder = _user
    treasure.find_time = arrow.now()

    trans = db.Transaction(
        minus=None,
        plus=_user,
        amount=treasure.value,
        reason=f"""🏖 Ritrovamento del tesoro `{treasure.slug}`""",
    )
    _session.add(trans)
    _user.fiorygi += treasure.value

    _session.commit()

    if treasure.message:
        await _msg.reply(text=f'🏖 Hai trovato un tesoro nascosto dal valore di \uE01Bƒ {treasure.value}\uE00B '
                              f'con il seguente messaggio:\n\n"{treasure.message}"')
    else:
        await _msg.reply(text=f"🏖 Hai trovato un tesoro nascosto dal valore di \uE01Bƒ {treasure.value}\uE00B!")


@rb.capture_errors
@engi.use_database(db.lazy_session_class)
@rb.use_ryglogin(allow_anonymous=False)
@engi.TeleportingConversation
async def fiorygi_bury(
        *,
        _user: db.User,
        _session: db.SessionType,
        _msg: engi.Message,
        slug: str,
        value: int,
        message: t.Optional[str],
        **__
):
    """
    Nascondi un tesoro con un dato nome.
    """

    treasure: t.Optional[db.Treasure] = _session.execute(
        ss.select(
            db.Treasure
        ).where(
            db.Treasure.slug == slug
        )
    ).scalar()

    if treasure is not None:
        if treasure.finder is not None:
            await _msg.reply(text=f"🏝 Un tesoro con quel nome è già stato trovato da {treasure.finder}.")
        else:
            await _msg.reply(text=f"🏖 Un tesoro con quel nome esiste già, "
                                  f"\uE01Bma non è ancora stato trovato da nessuno\uE00B!")
        return

    if value <= 0:
        await _msg.reply(text=f"⚠️ Il valore del tesoro deve essere intera positiva.")
        return

    if _user.fiorygi < value:
        await _msg.reply(text=f"⚠️ Non hai abbastanza fiorygi da nascondere.")
        return

    treasure = db.Treasure(
        slug=slug,
        creator=_user,
        creation_time=arrow.now(),
        value=value,
        message=message,
    )
    _session.add(treasure)

    trans = db.Transaction(
        minus=_user,
        plus=None,
        amount=treasure.value,
        reason=f"""🏖 Occultamento di un tesoro""",
    )
    _session.add(trans)
    _user.fiorygi -= value

    _session.commit()

    if treasure.message:
        await _msg.reply(text=f'🏖 Hai nascosto un tesoro dal valore di \uE01Bƒ {treasure.value}\uE00B '
                              f'con il seguente messaggio:\n"{treasure.message}"')
    else:
        await _msg.reply(text=f'🏖 Hai nascosto un tesoro dal valore di \uE01Bƒ {treasure.value}\uE00B.')


__all__ = (
    "fiorygi_balance_self",
    "fiorygi_balance_other",
    "fiorygi_give",
    "fiorygi_magick",
    "fiorygi_transactions_self",
    "fiorygi_transactions_other",
    "fiorygi_dig",
    "fiorygi_bury",
)

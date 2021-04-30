import royalnet.engineer as engi
import royalpack.database as db
import royalpack.bolts as rb


@rb.capture_errors
@engi.use_database(db.lazy_session_class)
@rb.use_ryglogin(allow_anonymous=True)
@engi.TeleportingConversation
async def whoami(*, _msg: engi.Message, _user: db.User, **__):
    """
    Scopri con che RYGaccount sei loggato.
    """

    if _user:
        await _msg.reply(text=f"☀️ Sei loggato come \uE01B{_user.name}\uE00B!")
    else:
        await _msg.reply(text="☁️ Non hai effettuato il login.")


__all__ = ("whoami",)

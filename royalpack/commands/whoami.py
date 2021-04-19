import royalnet.engineer as engi
import royalpack.database as db
import royalpack.bolts as rb


@engi.use_database(db.lazy_session_class)
@rb.use_ryglogin(allow_anonymous=True)
@engi.TeleportingConversation
async def whoami(*, _msg: engi.Message, _account, **__):
    """
    Scopri con che account sei loggato.
    """

    # TODO: improve output
    if _account:
        await _msg.reply(text=f"☀️ {_account}")
    else:
        await _msg.reply(text="☁️ Non sei loggato.")


__all__ = ("whoami",)

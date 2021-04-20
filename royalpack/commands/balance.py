import royalnet.engineer as engi
import royalpack.database as rd
import royalpack.bolts as rb


@engi.use_database(rd.lazy_session_class)
@rb.use_ryglogin(allow_anonymous=False)
@engi.TeleportingConversation
async def balance(*, _sentry: engi.Sentry, _msg: engi.Message, _user: rd.User, **__):
    """
    Visualizza il tuo portafoglio di fiorygi.
    """
    await _msg.reply(text=f"💰 Al momento, possiedi \uE01Bƒ {_user.fiorygi}\uE00B.")


__all__ = ("balance",)

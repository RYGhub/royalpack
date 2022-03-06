import royalnet.engineer as engi
import sqlalchemy.orm as so
import sqlalchemy.sql as ss

import royalpack.bolts as rb
import royalpack.database as db

expected = [
    "mrdima",
    "malbyx",
    "tullest",
    "steffo",
    "ichicoro",
    "nemesis",
    "sherryuzumaki",
    "fritz",
    "proto",
    "mallllco",
    "adry",
    "gattopardo",
    "viktya",
    "cookie",
    "deadmeme",
    "fre",
    "paltri",
    "alleander",
    "pesca",
    "kappa",
    "gimbaro",
    "sensei",
    "xzefyr",
    "maxbubblegum",
    "joj",
    "fultz",
    "tobiuan",
    "life",
    "matteo",
    "flaming",
    "wrath",
    "cosimo",
    "frank",
    "weirdie",
    "anacleto",
    "truebobby",
    "igor",
]


def telegram_emoji(b: bool) -> str:
    return "🔵" if b else "⚪️"


def discord_emoji(b: bool) -> str:
    return "🟣" if b else "⚪️"


@rb.capture_errors
@engi.use_database(db.lazy_session_class)
@engi.TeleportingConversation
async def loginprogress(*, _msg: engi.Message, _session: so.Session, **__):
    """
    Mostra l'elenco di membri RYG che non hanno ancora fatto il /login su RYGbot!
    """

    def _has_telegram_account(member: str) -> bool:
        accounts = _session.execute(
            ss.select(ss.func.count()).select_from(db.TelegramAccount).join(db.User).where(db.User.name == member)
        ).scalar()
        return accounts > 0

    def _has_discord_account(member: str) -> bool:
        accounts = _session.execute(
            ss.select(ss.func.count()).select_from(db.DiscordAccount).join(db.User).where(db.User.name == member)
        ).scalar()
        return accounts > 0

    telegram = list(map(_has_telegram_account, expected))
    discord = list(map(_has_discord_account, expected))

    def _render_line(index: int) -> str:
        def _telegram_emoji() -> str:
            return telegram_emoji(telegram[index])

        def _discord_emoji() -> str:
            return discord_emoji(discord[index])

        def _member_name() -> str:
            return expected[index]

        return f"{_telegram_emoji()}{_discord_emoji()} {_member_name()}"

    message = "\n".join(map(_render_line, range(len(expected))))
    await _msg.reply(text=message)


__all__ = ("loginprogress",)

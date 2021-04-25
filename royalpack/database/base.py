from __future__ import annotations
import typing as t
import sqlalchemy as s
import sqlalchemy.sql as ss
import sqlalchemy.orm as so
import sqlalchemy.ext.declarative as sed
import sqlalchemy_utils as su
import royalnet.alchemist as ra
import colour


Base: sed.declarative_base = sed.declarative_base()


user_title_association = s.Table(
    "user_title_association",
    Base.metadata,
    s.Column("user_fk", s.String, s.ForeignKey("users.sub")),
    s.Column("title_fk", su.UUIDType, s.ForeignKey("titles.uuid"))
)


class User(Base, ra.ColRepr, ra.Updatable):
    """
    An user, as returned by Auth0.
    """
    __tablename__ = "users"

    sub = s.Column(s.String, primary_key=True)
    last_update = s.Column(su.ArrowType, nullable=False)

    name = s.Column(s.String, nullable=False)
    nickname = s.Column(s.String, nullable=False)
    avatar = s.Column(s.String, nullable=False)
    email = s.Column(s.String, nullable=False)

    bio = s.Column(s.Text, nullable=False, default="")
    color = s.Column(su.ColorType, nullable=False, default=colour.Color("#a0ccff"))
    title_fk = s.Column(su.UUIDType, s.ForeignKey("titles.uuid"))
    fiorygi = s.Column(s.Integer, nullable=False, default=0)

    def __str__(self):
        return self.name


class UserAlias(Base, ra.ColRepr, ra.Updatable):
    """
    An alias for an User.
    """
    __tablename__ = "user_aliases"

    user_fk = s.Column(s.String, s.ForeignKey("users.sub"), primary_key=True)
    user = so.relationship("User", backref="aliases")

    name = s.Column(s.String, nullable=False, primary_key=True)

    @so.validates("name")
    def convert_lower(self, key, value: str) -> str:
        return value.lower()

    @classmethod
    def find(cls, session: so.Session, string: str) -> t.Optional[User]:
        ua = session.execute(
            ss.select(cls).where(cls.name == string)
        ).scalar()
        return ua.user if ua else None

    def __str__(self):
        return self.name


class TelegramAccount(Base, ra.ColRepr, ra.Updatable):
    """
    A Telegram account.
    """
    __tablename__ = "accounts_telegram"

    user_fk = s.Column(s.String, s.ForeignKey("users.sub"), nullable=False)
    user = so.relationship("User", backref="telegram_accounts")

    id = s.Column(s.BigInteger, primary_key=True)
    first_name = s.Column(s.String, nullable=False)
    last_name = s.Column(s.String)
    username = s.Column(s.String)
    avatar_url = s.Column(su.URLType)

    def name(self) -> str:
        if self.username is not None:
            return f"{self.username}"
        elif self.last_name is not None:
            return f"{self.first_name} {self.last_name}"
        else:
            return f"{self.first_name}"

    def mention(self) -> str:
        if self.username is not None:
            return f"@{self.username}"
        else:
            return f"[{self.name}](tg://user?id={self.tg_id})"

    def __str__(self):
        return self.name()


class DiscordAccount(Base, ra.ColRepr, ra.Updatable):
    """
    A Discord account.
    """
    __tablename__ = "accounts_discord"

    user_fk = s.Column(s.String, s.ForeignKey("users.sub"), nullable=False)
    user = so.relationship("User", backref="discord_accounts")

    id = s.Column(s.BigInteger, primary_key=True)
    username = s.Column(s.String, nullable=False)
    discriminator = s.Column(s.SmallInteger, nullable=False)
    avatar_url = s.Column(su.URLType)

    def name(self) -> str:
        return f"{self.username}#{self.discriminator}"

    def __str__(self):
        return self.name()


class SteamAccount(Base, ra.ColRepr, ra.Updatable):
    """
    A Steam account.
    """
    __tablename__ = "accounts_steam"

    user_fk = s.Column(s.String, s.ForeignKey("users.sub"), nullable=False)
    user = so.relationship("User", backref="steam_accounts")

    steamid = s.Column(s.BigInteger, primary_key=True)
    persona_name = s.Column(s.String, nullable=False)
    avatar_url = s.Column(su.URLType)

    # TODO: make steamid return steam.steamid.SteamID objects

    def __str__(self):
        return self.persona_name


class OsuAccount(Base, ra.ColRepr, ra.Updatable):
    """
    An osu! account.
    """
    __tablename__ = "accounts_osu"

    user_fk = s.Column(s.String, s.ForeignKey("users.sub"), nullable=False)
    user = so.relationship("User", backref="osu_accounts")

    id = s.Column(s.BigInteger, primary_key=True)
    username = s.Column(s.String)
    avatar_url = s.Column(su.URLType)

    def __str__(self):
        return self.username


class LeagueAccount(Base, ra.ColRepr, ra.Updatable):
    """
    A League of Legends account.
    """
    __tablename__ = "accounts_league"

    user_fk = s.Column(s.String, s.ForeignKey("users.sub"), nullable=False)
    user = so.relationship("User", backref="league_accounts")

    region = s.Column(s.String, nullable=False)
    puuid = s.Column(s.String, primary_key=True)
    summoner_name = s.Column(s.String, nullable=False)
    avatar_id = s.Column(s.Integer, nullable=False)

    def __str__(self):
        return self.summoner_name


class Title(Base, ra.ColRepr, ra.Updatable):
    """
    Title available for users to unlock.
    """
    __tablename__ = "titles"

    uuid = s.Column(su.UUIDType, primary_key=True)

    name = s.Column(s.String, nullable=False)
    visible = s.Column(s.Boolean, nullable=False)
    locked_description = s.Column(s.Text, nullable=False)
    unlocked_description = s.Column(s.Text, nullable=False)

    unlocked_by = so.relationship("User", secondary=user_title_association, backref="unlocked_titles")

    def __str__(self):
        return self.name


class DiarioGroup(Base, ra.ColRepr, ra.Updatable):
    """
    Group of Diario entries.
    """
    __tablename__ = "diario_groups"

    id = s.Column(s.Integer, primary_key=True)

    saved_by_fk = s.Column(s.String, s.ForeignKey("users.sub"), nullable=False)
    saved_by = so.relationship("User", backref="diario_groups_saved")

    context = s.Column(s.Text)


class DiarioLine(Base, ra.ColRepr, ra.Updatable):
    """
    Single Diario quote.
    """
    __tablename__ = "diario_lines"

    id = s.Column(s.Integer, primary_key=True)

    diario_group_fk = s.Column(s.Integer, s.ForeignKey("diario_groups.id"), nullable=False)
    diario_group = so.relationship("DiarioGroup", backref="lines")

    text = s.Column(s.Text)
    media_url = s.Column(su.URLType)
    timestamp = s.Column(su.ArrowType)
    spoiler = s.Column(s.String)
    quoted_str = s.Column(s.String)
    quoted_user_fk = s.Column(s.String, s.ForeignKey("users.sub"))
    quoted_user = so.relationship("DiarioGroup", backref="diario_quoted_in")


class Transaction(Base, ra.ColRepr, ra.Updatable):
    """
    Single fiorygi transaction.
    """
    __tablename__ = "fiorygi_transactions"

    id = s.Column(s.Integer, primary_key=True)

    minus_fk = s.Column(s.String, s.ForeignKey("users.sub"))
    minus = so.relationship("User", foreign_keys=(minus_fk,), backref="transactions_minus")

    plus_fk = s.Column(s.String, s.ForeignKey("users.sub"))
    plus = so.relationship("User", foreign_keys=(plus_fk,), backref="transactions_plus")

    amount = s.Column(s.Integer, nullable=False)
    reason = s.Column(s.Text)
    timestamp = s.Column(su.ArrowType)


class Treasure(Base, ra.ColRepr, ra.Updatable):
    """
    A treasure code which rewards fiorygi.
    """
    __tablename__ = "fiorygi_treasures"

    slug = s.Column(s.String, primary_key=True)

    creator_fk = s.Column(s.String, s.ForeignKey("users.sub"))
    creator = so.relationship("User", foreign_keys=(creator_fk,))
    creation_time = s.Column(su.ArrowType, nullable=False)

    finder_fk = s.Column(s.String, s.ForeignKey("users.sub"))
    finder = so.relationship("User", foreign_keys=(finder_fk,))
    find_time = s.Column(su.ArrowType)

    value = s.Column(s.Integer, nullable=False)
    message = s.Column(s.Text)

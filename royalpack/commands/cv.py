import royalnet.royaltyping as t
import royalnet.engineer as engi
import royalnet_discordpy as rd
import royalpack.bolts as rb
import discord
import discord.channel
import itertools


@rb.capture_errors
@engi.TeleportingConversation
async def cv(*, _msg: engi.Message, _pda: engi.PDA, **__):
    """
    Visualizza chi è connesso in chat vocale!
    """
    imp = _pda.implementations["discordpy.2"]
    assert isinstance(imp, rd.DiscordpyPDAImplementation)
    await imp.client.wait_until_ready()

    guild: discord.Guild = imp.client.get_guild(176353500710699008)

    message = []

    members_by_vc = get_members_by_voice_channel(guild=guild)

    for channel in get_interesting_channels(guild=guild):
        members_in_channel = members_by_vc.get(channel, [])
        if len(members_in_channel) == 0:
            continue

        message.append(build_channel_string(channel=channel))
        message.append("")

        for member in members_in_channel:
            message.append(build_member_string(member=member))

        message.append("")
        message.append("")

    if len(message) == 0:
        message.append("☁️ \uE011Non c'è nessuno in chat vocale.\uE001")

    await _msg.reply(text="\n".join(message))


def get_interesting_channels(guild: discord.Guild) -> list[discord.channel.VocalGuildChannel]:
    # noinspection PyTypeChecker
    return list(filter(lambda c: isinstance(c, discord.channel.VocalGuildChannel), guild.channels))


def get_voice_channel(member: t.Union[discord.Member, discord.User]) -> t.Optional[discord.channel.VocalGuildChannel]:
    if not member.voice:
        return None
    return member.voice.channel


def key_is_position(member: t.Union[discord.Member, discord.User]) -> int:
    if not member.voice:
        return 0
    return -member.voice.channel.position


def get_members_by_voice_channel(guild: discord.Guild):
    members = sorted(guild.members, key=key_is_position)
    groups = itertools.groupby(members, key=get_voice_channel)
    result = {}
    for group in groups:
        result[group[0]] = list(group[1])
    return result


def build_channel_string(channel: discord.channel.VocalGuildChannel) -> str:
    if isinstance(channel, discord.VoiceChannel):
        emoji = "🎙"
    elif isinstance(channel, discord.StageChannel):
        emoji = "📡"
    else:
        emoji = "❔"

    name = channel.name

    return f"\uE01B{emoji} {name}\uE00B"


def build_member_string(member: t.Union[discord.Member, discord.User]) -> str:
    _status: t.Union[discord.Status, str] = member.status
    if _status == discord.Status.online:
        status = "🔵"
    elif _status == discord.Status.dnd:
        status = "🔴"
    elif _status == discord.Status.idle:
        status = "⚫️"
    elif _status == discord.Status.offline:
        status = "⚪️"
    else:
        status = "❔"

    _voice: discord.VoiceState = member.voice
    if not _voice:
        voice = ""
    elif _voice.requested_to_speak_at:
        voice = "👋"
    elif _voice.self_deaf:
        voice = "🔇"
    elif _voice.self_mute:
        voice = "🔈"
    elif _voice.deaf:
        voice = "⛔️"
    elif _voice.mute:
        voice = "⛔️"
    elif _voice.self_stream:
        voice = "🖥"
    elif _voice.self_video:
        voice = "📹"
    else:
        voice = "🔊"

    if member.nick:
        name = member.nick
    else:
        name = member.name

    return "\n".join([
        f"{status}{voice} \uE012{name}\uE002",
        *map(
            lambda activity: build_activity_string(activity=activity),
            filter(
                lambda activity: activity.name, member.activities
            )
        )
    ])


def build_activity_string(activity: discord.Activity) -> str:
    if activity.type == discord.ActivityType.custom:
        text = f"\uE011{activity.name}\uE001"
    elif activity.type == discord.ActivityType.streaming:
        text = f"{activity.url}"
        breakpoint()
    else:
        text = f"{activity.name}"

    try:
        if activity.type == discord.ActivityType.listening:
            # noinspection PyUnresolvedReferences
            extra = f"({', '.join(activity.artists)} - {activity.album})"
        elif activity.state and activity.details:
            extra = f"({activity.state} | {activity.details})"
        elif activity.state:
            extra = f"({activity.state})"
        elif activity.details:
            extra = f"({activity.details})"
        else:
            extra = ""
    except AttributeError:
        extra = ""

    return f"- {text} {extra}"


__all__ = ("cv",)

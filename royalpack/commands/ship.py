import logging
import re
import royalpack.bolts as rb

import royalnet.engineer as engi

log = logging.getLogger(__name__)


@rb.capture_errors
@engi.TeleportingConversation
async def ship(*, _msg: engi.Message, first: str, second: str, **__):
    """
    Shippa insieme due persone! 💞
    """
    log.info(f"Shipping: {first!r} + {second!r}")

    # Convert the names to lowercase
    first = first.lower()
    second = second.lower()

    log.debug(f"Lowercased: {first!r} + {second!r}")

    # Decide the number of groups to keep
    first_groups = len(first) // 5
    second_groups = len(second) // 5

    log.debug(f"Keeping first:{first} second:{second} groups")

    # Try to get a match
    first_match = re.search(rf"^(?:[^aeiou]*[aeiou]){{,{first_groups}}}", first)
    second_match = re.search(rf"(?:[^aeiou\s]*[aeiou]){{,{second_groups}}}[a-z]?$", second)

    log.debug(f"Matches: {first_match!r} + {second_match!r}")

    # Get the matched characters if the matches were successful, or cut the names in half if they weren't
    first_crop = first_match.group(0) if first_match else first[:(len(first) // 2)]
    second_crop = second_match.group(0) if second_match else second[(len(second) // 2):]

    log.debug(f"Cropped: {first_crop!r} + {second_crop!r}")

    # Combine the two parts
    combined = f"{first_crop}{second_crop}"

    log.info(f"Combined: {combined!r}")

    # Send the message to the chat
    log.debug(f"Sending ship to the chat...")
    await _msg.reply(
        text=f"💞 {first.capitalize()} + {second.capitalize()} = \uE01B{combined.capitalize()}\uE00B"
    )


# Objects exported by this module
__all__ = (
    "ship",
)

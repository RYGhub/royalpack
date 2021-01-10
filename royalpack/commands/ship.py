# Special imports
from __future__ import annotations
import royalnet.royaltyping as t

# External imports
import royalnet.engineer as engi
import logging
import re

# Internal imports
# from . import something

# Special global objects
log = logging.getLogger(__name__)


# Code
@engi.PartialCommand.new(syntax=r"(?P<first>[A-Za-z]+)[\s+&]+(?P<second>[A-Za-z]+)")
async def ship(*, _sentry: engi.Sentry, _msg: engi.Message, first: str, second: str, **__):
    """
    Ship two names together! 💞
    """
    log.info(f"Shipping: {first!r} + {second!r}")

    # Convert the names to lowercase
    first = first.lower()
    second = second.lower()

    log.debug(f"Lowercased: {first!r} + {second!r}")

    # Get all letters until the first vowel, included
    first_match = re.search(r"^[A-Za-z][^aeiouAEIOU]*[aeiouAEIOU]?", first)
    # Get all letters from the second to last vowel, excluded
    second_match = re.search(r"[^aeiouAEIOU]*[aeiouAEIOU]?[A-Za-z]$", second)

    log.debug(f"Matches: {first_match!r} + {second_match!r}")

    # Get the matched characters if the matches were successful, or cut the names in half if they weren't
    first = first_match.group(0) if first_match else first[:(len(first) // 2)]
    second = second_match.group(0) if second_match else second[(len(second) // 2):]

    log.debug(f"Cropped: {first!r} + {second!r}")

    # Combine the two parts
    combined = f"{first}{second}"

    log.info(f"Combined: {combined!r}")

    # Send the message to the chat
    log.debug(f"Sending ship to the chat...")
    await _msg.send_reply(
        text=f"💞 {first.capitalize()} + {second.capitalize()} = {combined.capitalize()}"
    )


# Objects exported by this module
__all__ = (
    "ship",
)

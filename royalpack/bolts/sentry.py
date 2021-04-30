"""

"""

from __future__ import annotations

import functools
import logging
import sentry_sdk

log = logging.getLogger(__name__)


def capture_errors(f):
    @functools.wraps(f)
    async def decorated(**f_kwargs):
        try:
            return await f(**f_kwargs)
        except Exception as e:
            log.error(f"Captured error: {e!r}")
            if sentry_sdk.Hub.current is not None:
                sentry_sdk.capture_exception(error=e)

    return decorated


__all__ = (
    "capture_errors",
)

import re

from backend.constants import ALLOW_ORIGIN_HOSTS, ALLOW_ORIGIN_REGEX

if ALLOW_ORIGIN_REGEX is not None:
    ALLOW_ORIGIN_REGEX = re.compile(ALLOW_ORIGIN_REGEX)


def verify_host(origin: str) -> bool:
    """Verify whether the given origin is allowed."""
    if ALLOW_ORIGIN_REGEX is not None and ALLOW_ORIGIN_REGEX.fullmatch(origin):
        return True

    return origin in ALLOW_ORIGIN_HOSTS

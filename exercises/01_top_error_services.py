"""
01 - Warm-up: top error services  (target: 10 minutes)

The warm-up from your prep session. Write it however comes naturally first,
then see if you can get the body down to ~5 lines.

Idioms to reach for: str.split, collections.Counter, sorted(..., key=...)
"""

from _harness import check, main


def top_error_services(lines: list[str], k: int = 3) -> list[tuple[str, int]]:
    """Return the k services with the most ERROR lines as (service, count), most frequent first.

    Each line looks like "2026-10-06 ERROR auth-service timeout":
      date, level, service, then an optional free-text message (may contain spaces).

    Rules:
      - Count only lines whose level is exactly "ERROR" (case-sensitive).
      - Skip blank or malformed lines (fewer than 3 fields).
      - Break ties alphabetically by service name.
      - If fewer than k services have errors, return what you have.
    """
    raise NotImplementedError


# ---------------------------------------------------------------- tests

LOG = [
    "2026-10-06 ERROR auth-service timeout",
    "2026-10-06 INFO auth-service ok",
    "2026-10-06 ERROR db connection refused",
    "2026-10-06 ERROR auth-service timeout",
    "2026-10-06 ERROR cache miss storm",
    "2026-10-06 ERROR db deadlock",
    "2026-10-06 ERROR auth-service bad token",
    "2026-10-06 WARN cache slow",
    "2026-10-06 ERROR api 500",
]


def test_basic():
    check(top_error_services(LOG), [("auth-service", 3), ("db", 2), ("api", 1)])


def test_custom_k():
    check(top_error_services(LOG, k=1), [("auth-service", 3)])


def test_ties_alphabetical():
    check(top_error_services(LOG, k=10),
          [("auth-service", 3), ("db", 2), ("api", 1), ("cache", 1)])


def test_malformed_lines_skipped():
    lines = ["", "   ", "2026-10-06 ERROR", "2026-10-06 ERROR svc"]
    check(top_error_services(lines), [("svc", 1)])


def test_level_is_case_sensitive():
    check(top_error_services(["2026-10-06 error svc boom"]), [])


def test_empty():
    check(top_error_services([]), [])


if __name__ == "__main__":
    main(globals())

"""
16 - Mock interview  (45 minutes total, no docs, no autocomplete)

Treat this like the real thing:
  - Set a timer. Read each problem, ask yourself the clarifying questions an
    interviewer would expect, and say your approach + complexity out loud first.
  - Write your own extra edge-case tests before running the provided ones.
  - Afterwards, paste your solutions to Claude for a review as an interviewer would.
"""

from _harness import check, main


def merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Merge overlapping (or touching) closed intervals; return them sorted by start.
    [(1,3),(8,10),(2,6),(15,18)] -> [(1,6),(8,10),(15,18)]
    """
    raise NotImplementedError


def min_meeting_rooms(meetings: list[tuple[int, int]]) -> int:
    """Half-open meetings [start, end). Minimum rooms so no two overlapping meetings share one."""
    raise NotImplementedError


class RateLimiter:
    """Sliding-window limiter: allow(user, t) returns True if the user has made fewer than
    `limit` allowed requests in the window (t - window, t], and records the request if so.
    Timestamps per user are non-decreasing. Rejected requests don't count."""

    def __init__(self, limit: int, window: float):
        raise NotImplementedError

    def allow(self, user: str, t: float) -> bool:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_merge_intervals():
    check(merge_intervals([(1, 3), (8, 10), (2, 6), (15, 18)]), [(1, 6), (8, 10), (15, 18)])
    check(merge_intervals([(1, 4), (4, 5)]), [(1, 5)])
    check(merge_intervals([(1, 10), (2, 3)]), [(1, 10)])
    check(merge_intervals([]), [])


def test_min_meeting_rooms():
    check(min_meeting_rooms([(0, 30), (5, 10), (15, 20)]), 2)
    check(min_meeting_rooms([(7, 10), (2, 4)]), 1)
    check(min_meeting_rooms([(1, 5), (5, 10)]), 1)
    check(min_meeting_rooms([]), 0)


def test_rate_limiter():
    rl = RateLimiter(limit=2, window=10)
    got = [rl.allow("a", t) for t in (0, 1, 2, 10, 11, 12)]
    check(got, [True, True, False, True, True, False])
    check(rl.allow("b", 2), True, "users are independent")


if __name__ == "__main__":
    main(globals())

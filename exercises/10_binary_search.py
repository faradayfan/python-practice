"""
10 - Binary search  (target: 25 minutes)

Write these by hand (no bisect) - interviewers like to see you get the
boundaries right. Pick one loop shape (e.g. half-open [lo, hi)) and stick to it.
"""

from _harness import check, main


def search_insert(nums: list[int], target: int) -> int:
    """Index of target in sorted nums, or where it would be inserted to keep it sorted."""
    raise NotImplementedError


def first_true(lo: int, hi: int, pred) -> int:
    """pred is False...False True...True over [lo, hi). Return the first x where pred(x) is True, or hi."""
    raise NotImplementedError


def int_sqrt(n: int) -> int:
    """Floor of the square root of n >= 0, without math.sqrt / math.isqrt / ** 0.5."""
    raise NotImplementedError


def search_rotated(nums: list[int], target: int) -> int:
    """nums is a sorted list of distinct ints rotated at some pivot. Index of target or -1, O(log n)."""
    raise NotImplementedError


def min_ship_capacity(weights: list[int], days: int) -> int:
    """Packages ship in order; each day a ship carries consecutive packages up to its capacity.
    Smallest capacity that ships everything within `days`. (Binary search on the answer.)
    """
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_search_insert():
    check([search_insert([1, 3, 5, 6], t) for t in (5, 2, 7, 0)], [2, 1, 4, 0])
    check(search_insert([], 3), 0)


def test_first_true():
    check(first_true(0, 100, lambda x: x * x >= 50), 8)
    check(first_true(0, 10, lambda x: False), 10)


def test_int_sqrt():
    check([int_sqrt(n) for n in (0, 1, 8, 9, 10**12 + 1)], [0, 1, 2, 3, 10**6])


def test_search_rotated():
    nums = [4, 5, 6, 7, 0, 1, 2]
    check(search_rotated(nums, 0), 4)
    check(search_rotated(nums, 4), 0)
    check(search_rotated(nums, 3), -1)
    check(search_rotated([1], 1), 0)


def test_min_ship_capacity():
    check(min_ship_capacity([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5), 15)
    check(min_ship_capacity([3, 2, 2, 4, 1, 4], 3), 6)


if __name__ == "__main__":
    main(globals())

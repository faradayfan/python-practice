"""
06 - itertools, functools, bisect  (target: 20 minutes)

Idioms to reach for: itertools.combinations / product / chain.from_iterable /
accumulate, functools.lru_cache (or functools.cache), bisect.bisect_left /
bisect_right
"""

from _harness import check, main


def pairs_summing_to(nums: list[int], target: int) -> list[tuple[int, int]]:
    """Unique value pairs (a, b) with a <= b drawn from different positions, summing to target.
    Return them sorted. ([1, 2, 3, 4, 3], 6) -> [(2, 4), (3, 3)]
    """
    raise NotImplementedError


def flatten_once(nested: list[list]) -> list:
    """[[1, 2], [3], []] -> [1, 2, 3]"""
    raise NotImplementedError


def running_totals(nums: list[int]) -> list[int]:
    """[1, 2, 3, 4] -> [1, 3, 6, 10]"""
    raise NotImplementedError


def all_codes(alphabet: str, length: int) -> list[str]:
    """Every string of the given length over the alphabet, in lexicographic order.
    ("ab", 2) -> ["aa", "ab", "ba", "bb"]
    """
    raise NotImplementedError


def grid_paths(rows: int, cols: int) -> int:
    """Number of paths from top-left to bottom-right moving only right or down.
    Write it recursively and memoize with a decorator. grid_paths(18, 18) must be instant.
    """
    raise NotImplementedError


def letter_grade(score: int) -> str:
    """<60 F, 60-69 D, 70-79 C, 80-89 B, 90+ A. Use bisect, not an if-chain."""
    raise NotImplementedError


def count_in_range(sorted_nums: list[int], lo: int, hi: int) -> int:
    """How many values v satisfy lo <= v <= hi? O(log n)."""
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_pairs_summing_to():
    check(pairs_summing_to([1, 2, 3, 4, 3], 6), [(2, 4), (3, 3)])
    check(pairs_summing_to([3], 6), [], "a single 3 can't pair with itself")


def test_flatten_once():
    check(flatten_once([[1, 2], [3], []]), [1, 2, 3])


def test_running_totals():
    check(running_totals([1, 2, 3, 4]), [1, 3, 6, 10])


def test_all_codes():
    check(all_codes("ab", 2), ["aa", "ab", "ba", "bb"])
    check(len(all_codes("0123456789", 3)), 1000)


def test_grid_paths():
    check(grid_paths(2, 2), 2)
    check(grid_paths(3, 7), 28)
    check(grid_paths(18, 18), 2333606220)


def test_letter_grade():
    got = [letter_grade(s) for s in (0, 59, 60, 75, 89, 90, 100)]
    check(got, ["F", "F", "D", "C", "B", "A", "A"])


def test_count_in_range():
    nums = [1, 3, 3, 3, 5, 8, 13]
    check(count_in_range(nums, 3, 8), 5)
    check(count_in_range(nums, 9, 12), 0)
    check(count_in_range([], 0, 10), 0)


if __name__ == "__main__":
    main(globals())

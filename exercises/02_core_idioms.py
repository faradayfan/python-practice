"""
02 - Core idioms  (target: 15 minutes for all)

Each of these should be 1-3 lines of idiomatic Python. If you find yourself
writing `for i in range(len(xs))` or building a list with .append in a loop,
there's a more Pythonic way.

Idioms to reach for: comprehensions, slicing, zip, enumerate, star-unpacking,
dict.fromkeys, zip(*rows)
"""

from _harness import check, main


def squares_of_evens(nums: list[int]) -> list[int]:
    """[1, 2, 3, 4] -> [4, 16]"""
    raise NotImplementedError


def invert_dict(d: dict) -> dict:
    """Swap keys and values (values are guaranteed unique). {"a": 1} -> {1: "a"}"""
    raise NotImplementedError


def pairwise_diffs(nums: list[int]) -> list[int]:
    """Differences between neighbours. [1, 4, 9, 16] -> [3, 5, 7]"""
    raise NotImplementedError


def chunk(seq: list, n: int) -> list[list]:
    """Split into chunks of size n; the last may be shorter. ([1..7], 3) -> [[1,2,3],[4,5,6],[7]]"""
    raise NotImplementedError


def head_tail(seq: list) -> tuple:
    """Return (first, rest). Empty input -> (None, []).  Hint: first, *rest = ..."""
    raise NotImplementedError


def rotate_right(lst: list, k: int) -> list:
    """Return a new list rotated right by k. k may exceed len(lst). ([1,2,3,4,5], 2) -> [4,5,1,2,3]"""
    raise NotImplementedError


def positions(seq: list, value) -> list[int]:
    """Indices where seq[i] == value. (["a","b","a"], "a") -> [0, 2]"""
    raise NotImplementedError


def transpose(matrix: list[list]) -> list[list]:
    """[[1,2,3],[4,5,6]] -> [[1,4],[2,5],[3,6]]"""
    raise NotImplementedError


def dedupe(seq: list) -> list:
    """Remove duplicates, keeping first-seen order. [3,1,3,2,1] -> [3,1,2]"""
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_squares_of_evens():
    check(squares_of_evens([1, 2, 3, 4]), [4, 16])
    check(squares_of_evens([]), [])


def test_invert_dict():
    check(invert_dict({"a": 1, "b": 2}), {1: "a", 2: "b"})


def test_pairwise_diffs():
    check(pairwise_diffs([1, 4, 9, 16]), [3, 5, 7])
    check(pairwise_diffs([5]), [])
    check(pairwise_diffs([]), [])


def test_chunk():
    check(chunk([1, 2, 3, 4, 5, 6, 7], 3), [[1, 2, 3], [4, 5, 6], [7]])
    check(chunk([], 3), [])


def test_head_tail():
    check(head_tail([1, 2, 3]), (1, [2, 3]))
    check(head_tail([1]), (1, []))
    check(head_tail([]), (None, []))


def test_rotate_right():
    check(rotate_right([1, 2, 3, 4, 5], 2), [4, 5, 1, 2, 3])
    check(rotate_right([1, 2, 3], 7), [3, 1, 2])
    check(rotate_right([], 3), [])
    original = [1, 2, 3]
    rotate_right(original, 1)
    check(original, [1, 2, 3], "input must not be mutated")


def test_positions():
    check(positions(["a", "b", "a"], "a"), [0, 2])
    check(positions([1, 2], 9), [])


def test_transpose():
    check(transpose([[1, 2, 3], [4, 5, 6]]), [[1, 4], [2, 5], [3, 6]])


def test_dedupe():
    check(dedupe([3, 1, 3, 2, 1]), [3, 1, 2])


if __name__ == "__main__":
    main(globals())

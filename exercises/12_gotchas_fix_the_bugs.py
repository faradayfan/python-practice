"""
12 - Python gotchas: fix the bugs  (target: 20 minutes)

Unlike the other files, these functions are already written, and each has a
classic Python bug. Every test fails right now. For each one:
  1. Predict what the buggy code actually returns before running it.
  2. Fix it with the smallest idiomatic change.
  3. Be ready to explain the bug in one sentence - interviewers ask.
"""

import copy  # noqa: F401  (you may need this)

from _harness import check, main


def add_tag(tag, tags=[]):
    """Return tags with tag appended; with no list given, start a fresh one."""
    tags.append(tag)
    return tags


def make_multipliers():
    """Return four functions: multiply by 0, 1, 2, 3."""
    return [lambda x: x * i for i in range(4)]


def make_grid(rows, cols):
    """rows x cols grid of zeros, each row independent."""
    return [[0] * cols] * rows


def without_evens(nums):
    """Return a new list without even numbers. Must not modify nums."""
    for n in nums:
        if n % 2 == 0:
            nums.remove(n)
    return nums


def snapshot(config):
    """Return a copy of config that is unaffected by later changes to config."""
    return config.copy()


def same_value(a, b):
    """True if a and b are equal."""
    return a is b


def average(nums):
    """Mean of nums as a float; 0.0 for an empty list."""
    return sum(nums) // len(nums)


def make_counter():
    """Return a function that returns 1, 2, 3, ... on successive calls."""
    count = 0

    def increment():
        count += 1
        return count

    return increment


# ---------------------------------------------------------------- tests

def test_mutable_default():
    check(add_tag("a"), ["a"])
    check(add_tag("b"), ["b"])


def test_late_binding_closure():
    check([f(10) for f in make_multipliers()], [0, 10, 20, 30])


def test_aliased_rows():
    grid = make_grid(3, 2)
    grid[0][0] = 1
    check(grid, [[1, 0], [0, 0], [0, 0]])


def test_mutating_while_iterating():
    nums = [2, 4, 6, 1, 8, 3]
    check(without_evens(nums), [1, 3])
    check(nums, [2, 4, 6, 1, 8, 3], "input must be unchanged")


def test_shallow_copy():
    config = {"db": {"host": "localhost"}, "debug": False}
    saved = snapshot(config)
    config["db"]["host"] = "prod.example.com"
    check(saved["db"]["host"], "localhost")


def test_identity_vs_equality():
    check(same_value(1000, int("1000")), True)
    check(same_value([1], [1]), True)


def test_integer_division():
    check(average([2, 3]), 2.5)
    check(average([]), 0.0)


def test_closure_rebinding():
    counter = make_counter()
    check([counter(), counter(), counter()], [1, 2, 3])


if __name__ == "__main__":
    main(globals())

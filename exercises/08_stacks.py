"""
08 - Stacks  (target: 25 minutes)

A Python list is your stack: append / pop / stack[-1].
Watch out in eval_rpn: Python's // floors toward negative infinity, not zero.
"""

from _harness import check, main


def is_balanced(s: str) -> bool:
    """Brackets ()[]{} are properly nested and closed. Other characters are ignored."""
    raise NotImplementedError


def eval_rpn(tokens: list[str]) -> int:
    """Evaluate reverse Polish notation with + - * /. Division truncates toward zero (like Go).
    ["4", "13", "5", "/", "+"] -> 6
    """
    raise NotImplementedError


def daily_temperatures(temps: list[int]) -> list[int]:
    """For each day, how many days until a warmer temperature (0 if never). O(n) monotonic stack."""
    raise NotImplementedError


def simplify_path(path: str) -> str:
    """Canonical Unix path. "/a/./b/../../c/" -> "/c",  "/../" -> "/",  "/home//foo/" -> "/home/foo" """
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_is_balanced():
    check(is_balanced("{[()()]}"), True)
    check(is_balanced("f(x[1]) + {y}"), True)
    check(is_balanced("([)]"), False)
    check(is_balanced("(("), False)
    check(is_balanced(")"), False)
    check(is_balanced(""), True)


def test_eval_rpn():
    check(eval_rpn(["2", "1", "+", "3", "*"]), 9)
    check(eval_rpn(["4", "13", "5", "/", "+"]), 6)
    check(eval_rpn(["7", "-2", "/"]), -3, "truncate toward zero")


def test_daily_temperatures():
    check(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]), [1, 1, 4, 2, 1, 1, 0, 0])


def test_simplify_path():
    check(simplify_path("/a/./b/../../c/"), "/c")
    check(simplify_path("/../"), "/")
    check(simplify_path("/home//foo/"), "/home/foo")


if __name__ == "__main__":
    main(globals())

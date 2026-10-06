"""
03 - Sorting and strings  (target: 20 minutes)

Idioms to reach for: sorted(key=lambda ...) with tuple keys and negation,
sort stability, str methods (isalnum, lower, join, ljust), f-string format
specs, itertools.groupby
"""

from _harness import check, main


def sort_employees(employees: list[dict]) -> list[dict]:
    """Return a new list sorted by dept ascending, then salary descending, then name ascending.

    Each employee: {"name": str, "dept": str, "salary": int}
    """
    raise NotImplementedError


def longest_words(text: str, n: int) -> list[str]:
    """The n longest whitespace-separated words, longest first.
    Words of equal length keep their original order (hint: sorting is stable).
    """
    raise NotImplementedError


def is_palindrome(s: str) -> bool:
    """Consider only letters/digits, case-insensitive.
    "A man, a plan, a canal: Panama" -> True
    """
    raise NotImplementedError


def compress(s: str) -> str:
    """Run-length encode; runs of length 1 have no count. "aaabccdddd" -> "a3bc2d4" """
    raise NotImplementedError


def format_report(rows: list[tuple[str, float]]) -> str:
    """Render an aligned table, one line per row, joined by newlines:
      - name left-aligned, padded to the width of the longest name
      - then " | "
      - then the value right-aligned in width 8 with 2 decimal places

    [("cpu", 0.5), ("memory", 12.346)] ->
        "cpu    |     0.50\\n"
        "memory |    12.35"
    """
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_sort_employees():
    staff = [
        {"name": "dan", "dept": "eng", "salary": 100},
        {"name": "amy", "dept": "ops", "salary": 90},
        {"name": "bob", "dept": "eng", "salary": 120},
        {"name": "cat", "dept": "eng", "salary": 100},
    ]
    got = [e["name"] for e in sort_employees(staff)]
    check(got, ["bob", "cat", "dan", "amy"])
    check(staff[0]["name"], "dan", "input must not be reordered")


def test_longest_words():
    check(longest_words("the quick brown fox jumped", 3), ["jumped", "quick", "brown"])
    check(longest_words("a bb cc d", 2), ["bb", "cc"])


def test_is_palindrome():
    check(is_palindrome("A man, a plan, a canal: Panama"), True)
    check(is_palindrome("race a car"), False)
    check(is_palindrome(""), True)


def test_compress():
    check(compress("aaabccdddd"), "a3bc2d4")
    check(compress("abc"), "abc")
    check(compress(""), "")


def test_format_report():
    expected = "cpu    |     0.50\nmemory |    12.35"
    check(format_report([("cpu", 0.5), ("memory", 12.346)]), expected)


if __name__ == "__main__":
    main(globals())

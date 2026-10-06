"""
11 - Dynamic programming  (target: 40 minutes)

Try each twice: top-down (recursion + @functools.cache) and bottom-up (a list).
Say the recurrence out loud before you write code.
"""

from _harness import check, main


def coin_change(coins: list[int], amount: int) -> int:
    """Fewest coins summing to amount (unlimited supply of each), or -1."""
    raise NotImplementedError


def house_robber(nums: list[int]) -> int:
    """Max sum of non-adjacent elements."""
    raise NotImplementedError


def lcs_length(a: str, b: str) -> int:
    """Length of the longest common subsequence."""
    raise NotImplementedError


def word_break(s: str, words: list[str]) -> bool:
    """Can s be segmented into a sequence of (reusable) dictionary words?"""
    raise NotImplementedError


def lis_length(nums: list[int]) -> int:
    """Length of the longest strictly increasing subsequence. O(n^2) is fine; O(n log n) is a bonus."""
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_coin_change():
    check(coin_change([1, 2, 5], 11), 3)
    check(coin_change([2], 3), -1)
    check(coin_change([1], 0), 0)
    check(coin_change([186, 419, 83, 408], 6249), 20)


def test_house_robber():
    check(house_robber([2, 7, 9, 3, 1]), 12)
    check(house_robber([]), 0)


def test_lcs_length():
    check(lcs_length("abcde", "ace"), 3)
    check(lcs_length("abc", "def"), 0)


def test_word_break():
    check(word_break("leetcode", ["leet", "code"]), True)
    check(word_break("applepenapple", ["apple", "pen"]), True)
    check(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]), False)


def test_lis_length():
    check(lis_length([10, 9, 2, 5, 3, 7, 101, 18]), 4)
    check(lis_length([7, 7, 7]), 1)
    check(lis_length([]), 0)


if __name__ == "__main__":
    main(globals())

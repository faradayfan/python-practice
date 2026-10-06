"""
07 - Two pointers and sliding window  (target: 30 minutes)

State the time/space complexity out loud for each one before coding.
All of these have O(n) solutions.
"""

from _harness import check, main


def two_sum_sorted(nums: list[int], target: int) -> tuple[int, int] | None:
    """nums is sorted ascending. Return indices (i, j), i < j, with nums[i] + nums[j] == target, or None."""
    raise NotImplementedError


def dedupe_sorted_in_place(nums: list[int]) -> int:
    """Remove duplicates from a sorted list IN PLACE so the first k slots hold the unique values.
    Return k. Don't allocate another list.
    """
    raise NotImplementedError


def max_water(heights: list[int]) -> int:
    """Container with most water: max over i<j of (j - i) * min(heights[i], heights[j])."""
    raise NotImplementedError


def longest_unique_substring(s: str) -> int:
    """Length of the longest substring with no repeated characters. "abcabcbb" -> 3"""
    raise NotImplementedError


def max_window_sum(nums: list[int], k: int) -> int:
    """Largest sum of any k consecutive elements (len(nums) >= k >= 1)."""
    raise NotImplementedError


def min_subarray_len(target: int, nums: list[int]) -> int:
    """nums are positive. Length of the shortest contiguous subarray with sum >= target, or 0."""
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_two_sum_sorted():
    check(two_sum_sorted([2, 7, 11, 15], 9), (0, 1))
    check(two_sum_sorted([1, 3, 4, 6, 9], 10), (0, 4))
    check(two_sum_sorted([1, 2], 7), None)


def test_dedupe_sorted_in_place():
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = dedupe_sorted_in_place(nums)
    check(k, 5)
    check(nums[:k], [0, 1, 2, 3, 4])
    check(dedupe_sorted_in_place([]), 0)


def test_max_water():
    check(max_water([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)
    check(max_water([1, 1]), 1)


def test_longest_unique_substring():
    check(longest_unique_substring("abcabcbb"), 3)
    check(longest_unique_substring("bbbbb"), 1)
    check(longest_unique_substring("pwwkew"), 3)
    check(longest_unique_substring("abba"), 2)
    check(longest_unique_substring(""), 0)


def test_max_window_sum():
    check(max_window_sum([2, 1, 5, 1, 3, 2], 3), 9)
    check(max_window_sum([-1, -2, -3], 2), -3)


def test_min_subarray_len():
    check(min_subarray_len(7, [2, 3, 1, 2, 4, 3]), 2)
    check(min_subarray_len(100, [1, 2, 3]), 0)


if __name__ == "__main__":
    main(globals())

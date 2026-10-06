"""
04 - collections: Counter and defaultdict  (target: 20 minutes)

Idioms to reach for: Counter (most_common, subtraction, comparison),
defaultdict(list) / defaultdict(set), tuple(sorted(word)) as a dict key
"""

from _harness import check, main


def group_anagrams(words: list[str]) -> list[list[str]]:
    """Group words that are anagrams of each other. Group order doesn't matter.
    ["eat","tea","tan","ate","nat","bat"] -> [["eat","tea","ate"],["tan","nat"],["bat"]]
    """
    raise NotImplementedError


def first_unique_char(s: str) -> int:
    """Index of the first character that appears exactly once, or -1."""
    raise NotImplementedError


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """The k most frequent values, by frequency desc, ties broken by smaller value first."""
    raise NotImplementedError


def can_build(note: str, magazine: str) -> bool:
    """Can `note` be written using letters cut from `magazine` (each letter used once)?"""
    raise NotImplementedError


def inverted_index(docs: dict[str, str]) -> dict[str, set[str]]:
    """Map each lowercased word to the set of doc ids containing it.
    {"d1": "Hello world", "d2": "hello there"} -> {"hello": {"d1","d2"}, "world": {"d1"}, "there": {"d2"}}
    """
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_group_anagrams():
    got = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    normalized = sorted(sorted(g) for g in got)
    check(normalized, [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]])
    check(group_anagrams([]), [])


def test_first_unique_char():
    check(first_unique_char("leetcode"), 0)
    check(first_unique_char("loveleetcode"), 2)
    check(first_unique_char("aabb"), -1)


def test_top_k_frequent():
    check(top_k_frequent([1, 1, 1, 2, 2, 3], 2), [1, 2])
    check(top_k_frequent([4, 4, 2, 2, 3], 2), [2, 4])


def test_can_build():
    check(can_build("aa", "aab"), True)
    check(can_build("aa", "ab"), False)
    check(can_build("", "x"), True)


def test_inverted_index():
    got = inverted_index({"d1": "Hello world", "d2": "hello there"})
    check(got, {"hello": {"d1", "d2"}, "world": {"d1"}, "there": {"d2"}})
    check(type(got), dict, "return a plain dict (dict(my_defaultdict) is fine)")


if __name__ == "__main__":
    main(globals())

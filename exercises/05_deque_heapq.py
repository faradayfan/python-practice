"""
05 - collections.deque and heapq  (target: 25 minutes)

Idioms to reach for: deque(maxlen=...), appendleft/popleft, heapq.heappush/
heappop, heapq.nsmallest/nlargest with key=, heapq.merge, min-heap of negatives
to simulate a max-heap.
"""

from _harness import check, main


def sliding_window_max(nums: list[int], k: int) -> list[int]:
    """Max of each window of size k. Aim for O(n) with a deque of indices.
    ([1,3,-1,-3,5,3,6,7], 3) -> [3,3,5,5,6,7]
    """
    raise NotImplementedError


def k_closest(points: list[tuple[int, int]], k: int) -> list[tuple[int, int]]:
    """The k points closest to the origin, closest first."""
    raise NotImplementedError


def merge_sorted(lists: list[list[int]]) -> list[int]:
    """Merge already-sorted lists into one sorted list."""
    raise NotImplementedError


def kth_largest(nums: list[int], k: int) -> int:
    """Aim for O(n log k): keep a min-heap of size k."""
    raise NotImplementedError


class RecentCounter:
    """ping(t) records a request at time t (ms, strictly increasing) and returns
    how many requests happened in the inclusive window [t - 3000, t]."""

    def __init__(self):
        raise NotImplementedError

    def ping(self, t: int) -> int:
        raise NotImplementedError


def running_median(stream: list[int]) -> list[float]:
    """STRETCH: median after each element arrives, using two heaps.
    [5, 15, 1, 3] -> [5.0, 10.0, 5.0, 4.0]
    """
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_sliding_window_max():
    check(sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7])
    check(sliding_window_max([4, 2], 1), [4, 2])


def test_k_closest():
    check(k_closest([(1, 3), (-2, 2), (5, 8), (0, 1)], 2), [(0, 1), (-2, 2)])


def test_merge_sorted():
    check(merge_sorted([[1, 4, 5], [1, 3, 4], [2, 6]]), [1, 1, 2, 3, 4, 4, 5, 6])
    check(merge_sorted([[], [1]]), [1])


def test_kth_largest():
    check(kth_largest([3, 2, 1, 5, 6, 4], 2), 5)
    check(kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)


def test_recent_counter():
    rc = RecentCounter()
    check([rc.ping(t) for t in (1, 100, 3001, 3002)], [1, 2, 3, 3])


def test_running_median():
    check(running_median([5, 15, 1, 3]), [5.0, 10.0, 5.0, 4.0])
    check(running_median([2, 2, 2]), [2.0, 2.0, 2.0])


if __name__ == "__main__":
    main(globals())

"""
09 - Graphs: BFS, DFS, topological sort  (target: 35 minutes)

Idioms to reach for: deque for BFS queues, a `seen` set, defaultdict(list)
adjacency lists, (row, col) tuples as keys, a DIRS = [(0,1),(1,0),(0,-1),(-1,0)]
constant, bounds checks with `0 <= r < rows`.
"""

from _harness import check, main


def num_islands(grid: list[str]) -> int:
    """Count 4-directionally connected groups of '1' in a grid of '1'/'0' strings."""
    raise NotImplementedError


def shortest_path(grid: list[str], start: tuple[int, int], end: tuple[int, int]) -> int:
    """Fewest 4-directional steps from start to end; '#' is a wall, '.' is open. -1 if unreachable."""
    raise NotImplementedError


def course_order(n: int, prereqs: list[tuple[int, int]]) -> list[int]:
    """Courses 0..n-1; (a, b) means b must be taken before a.
    Return any valid order, or [] if impossible (cycle).
    """
    raise NotImplementedError


def count_components(n: int, edges: list[tuple[int, int]]) -> int:
    """Number of connected components in an undirected graph with nodes 0..n-1."""
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_num_islands():
    grid = [
        "11000",
        "11000",
        "00100",
        "00011",
    ]
    check(num_islands(grid), 3)
    check(num_islands([]), 0)


def test_shortest_path():
    grid = [
        "....#",
        ".##.#",
        "...#.",
        "#....",
    ]
    check(shortest_path(grid, (0, 0), (3, 4)), 7)
    check(shortest_path(grid, (0, 0), (0, 0)), 0)
    check(shortest_path([".#."], (0, 0), (0, 2)), -1)


def _valid_order(n, prereqs, order):
    pos = {c: i for i, c in enumerate(order)}
    return sorted(order) == list(range(n)) and all(pos[b] < pos[a] for a, b in prereqs)


def test_course_order():
    prereqs = [(1, 0), (2, 0), (3, 1), (3, 2)]
    order = course_order(4, prereqs)
    check(_valid_order(4, prereqs, order), True, f"invalid order {order}")
    check(course_order(2, [(0, 1), (1, 0)]), [])
    check(sorted(course_order(3, [])), [0, 1, 2])


def test_count_components():
    check(count_components(5, [(0, 1), (1, 2), (3, 4)]), 2)
    check(count_components(3, []), 3)


if __name__ == "__main__":
    main(globals())

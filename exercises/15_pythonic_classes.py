"""
15 - Pythonic classes, generators, context managers, decorators  (target: 35 minutes)

The Python features with no direct Go equivalent - expect at least one
follow-up question touching these.

Idioms to reach for: @dataclass, dunder methods (__add__, __abs__, __iter__),
collections.OrderedDict (move_to_end, popitem(last=False)), yield,
itertools.islice, __enter__/__exit__ or @contextlib.contextmanager,
time.perf_counter, functools.wraps
"""

from _harness import check, main


# Make Vector a @dataclass with float fields x and y, supporting:
#   v + w, v - w, v * 3 (scalar), abs(v) (length), and unpacking: x, y = v
class Vector:
    pass


class LRUCache:
    """get(key) -> value or -1; put(key, value). Evicts the least recently used
    key when over capacity. Both operations O(1)."""

    def __init__(self, capacity: int):
        raise NotImplementedError

    def get(self, key):
        raise NotImplementedError

    def put(self, key, value) -> None:
        raise NotImplementedError


def batched(iterable, size: int):
    """Generator yielding lists of up to `size` items. Must work on infinite iterators.
    (Write it yourself - don't use itertools.batched.)
    """
    raise NotImplementedError


class Timer:
    """with Timer() as t: ...  then t.elapsed holds the seconds taken (float).
    Exceptions inside the block must propagate, and elapsed must still be set."""


def retry(times: int):
    """Decorator factory: call the function up to `times` attempts total, returning the
    first successful result; if every attempt raises, re-raise the last exception.
    The wrapped function must keep its __name__.
    """
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_vector():
    v, w = Vector(3, 4), Vector(1, 2)
    check(v + w, Vector(4, 6))
    check(v - w, Vector(2, 2))
    check(v * 2, Vector(6, 8))
    check(abs(v), 5.0)
    x, y = v
    check((x, y), (3, 4))
    check(repr(w), "Vector(x=1, y=2)")


def test_lru_cache():
    c = LRUCache(2)
    c.put(1, "a")
    c.put(2, "b")
    check(c.get(1), "a")
    c.put(3, "c")           # evicts 2 (1 was just used)
    check(c.get(2), -1)
    c.put(1, "A")           # update refreshes recency
    c.put(4, "d")           # evicts 3
    check([c.get(k) for k in (1, 3, 4)], ["A", -1, "d"])


def test_batched():
    import itertools
    check(list(batched(range(7), 3)), [[0, 1, 2], [3, 4, 5], [6]])
    check(list(batched([], 3)), [])
    first_two = list(itertools.islice(batched(itertools.count(), 2), 2))
    check(first_two, [[0, 1], [2, 3]])


def test_timer():
    import time
    with Timer() as t:
        time.sleep(0.01)
    check(0.01 <= t.elapsed < 1, True, f"elapsed={t.elapsed}")
    t2 = Timer()
    try:
        with t2:
            raise KeyError("boom")
    except KeyError:
        pass
    else:
        raise AssertionError("exception was swallowed")
    check(t2.elapsed >= 0, True)


def test_retry():
    calls = []

    @retry(times=3)
    def flaky():
        calls.append(1)
        if len(calls) < 3:
            raise ConnectionError("try again")
        return "ok"

    check(flaky(), "ok")
    check(len(calls), 3)
    check(flaky.__name__, "flaky")

    @retry(times=2)
    def always_fails():
        raise ValueError("nope")

    try:
        always_fails()
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError to be re-raised")


if __name__ == "__main__":
    main(globals())

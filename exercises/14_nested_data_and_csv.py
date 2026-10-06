"""
14 - Practical: nested dicts, config, CSV  (target: 30 minutes)

Idioms to reach for: recursion over dicts, isinstance, dict.items(),
dict.setdefault, {**a, **b}, csv.DictReader over io.StringIO, try/except ValueError
"""

from _harness import check, main


def flatten(d: dict, sep: str = ".") -> dict:
    """{"a": {"b": 1, "c": {"d": 2}}, "e": 3} -> {"a.b": 1, "a.c.d": 2, "e": 3}"""
    raise NotImplementedError


def unflatten(d: dict, sep: str = ".") -> dict:
    """Inverse of flatten."""
    raise NotImplementedError


def deep_merge(base: dict, override: dict) -> dict:
    """Return a NEW dict: keys from both; where both values are dicts, merge recursively,
    otherwise override wins. Neither input may be mutated.
    """
    raise NotImplementedError


def get_path(data, path: str, default=None):
    """Follow a dotted path through dicts and lists (numeric parts index lists).
    get_path({"a": [{"b": 5}]}, "a.0.b") -> 5. Missing anything -> default.
    """
    raise NotImplementedError


def summarize_sales(csv_text: str) -> dict[str, dict]:
    """CSV with header region,product,amount. Return {region: {"total": float, "count": int}}.
    Skip rows whose amount isn't a valid number.
    """
    raise NotImplementedError


# ---------------------------------------------------------------- tests

NESTED = {"a": {"b": 1, "c": {"d": 2}}, "e": 3}
FLAT = {"a.b": 1, "a.c.d": 2, "e": 3}


def test_flatten():
    check(flatten(NESTED), FLAT)
    check(flatten({}), {})
    check(flatten({"x": {"y": 1}}, sep="/"), {"x/y": 1})


def test_unflatten():
    check(unflatten(FLAT), NESTED)


def test_deep_merge():
    base = {"db": {"host": "localhost", "port": 5432}, "debug": False}
    override = {"db": {"host": "prod"}, "debug": True, "workers": 4}
    merged = deep_merge(base, override)
    check(merged, {"db": {"host": "prod", "port": 5432}, "debug": True, "workers": 4})
    check(base["db"]["host"], "localhost", "base must not be mutated")
    merged["db"]["port"] = 1
    check(base["db"]["port"], 5432, "result must not share nested dicts with base")


def test_get_path():
    data = {"a": [{"b": 5}], "c": {"d": None}}
    check(get_path(data, "a.0.b"), 5)
    check(get_path(data, "a.3.b", "missing"), "missing")
    check(get_path(data, "c.d", "missing"), None, "an explicit None is a real value")
    check(get_path(data, "a.x", "missing"), "missing")


def test_summarize_sales():
    text = (
        "region,product,amount\n"
        "west,widget,10.50\n"
        "east,gadget,4\n"
        "west,gizmo,not-a-number\n"
        "west,widget,2.25\n"
    )
    check(summarize_sales(text), {
        "west": {"total": 12.75, "count": 2},
        "east": {"total": 4.0, "count": 1},
    })


if __name__ == "__main__":
    main(globals())

"""Tiny test runner so exercises need nothing beyond the standard library.

Run any exercise directly:  python3 exercises/01_top_error_services.py
Every function named test_* in the file is run in definition order.
"""

import sys
import traceback


def check(got, expected, label=""):
    if got != expected:
        prefix = f"{label}: " if label else ""
        raise AssertionError(f"{prefix}expected {expected!r}, got {got!r}")


def run(namespace):
    tests = [(n, f) for n, f in namespace.items() if n.startswith("test_") and callable(f)]
    passed = failed = todo = 0
    for name, fn in tests:
        try:
            fn()
        except NotImplementedError:
            todo += 1
            print(f"  TODO  {name}")
        except Exception as exc:
            failed += 1
            print(f"  FAIL  {name}")
            frames = traceback.extract_tb(exc.__traceback__)
            frame = next((f for f in reversed(frames) if f.name != "check"), frames[-1])
            print(f"        line {frame.lineno}: {frame.line}")
            print(f"        {type(exc).__name__}: {exc}")
        else:
            passed += 1
            print(f"  ok    {name}")
    print(f"RESULT passed={passed} failed={failed} todo={todo} total={len(tests)}")
    return 0 if passed == len(tests) else 1


def main(namespace):
    sys.exit(run(namespace))

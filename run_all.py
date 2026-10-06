"""Progress overview across all exercises.

    python3 run_all.py          # summary table
    python3 run_all.py 05       # full output for exercises whose name starts with 05
"""

import re
import subprocess
import sys
from pathlib import Path

EXERCISES = Path(__file__).parent / "exercises"
RESULT = re.compile(r"RESULT passed=(\d+) failed=(\d+) todo=(\d+) total=(\d+)")


def main():
    prefix = sys.argv[1] if len(sys.argv) > 1 else ""
    files = sorted(p for p in EXERCISES.glob("[0-9]*.py") if p.name.startswith(prefix))
    if prefix:
        for path in files:
            print(f"== {path.name}")
            subprocess.run([sys.executable, path])
        return

    print(f"{'exercise':<34}{'pass':>6}{'fail':>6}{'todo':>6}")
    total_pass = total = 0
    for path in files:
        out = subprocess.run([sys.executable, path], capture_output=True, text=True).stdout
        m = RESULT.search(out)
        if not m:
            print(f"{path.stem:<34}  (crashed - run it directly to see why)")
            continue
        p, f, t, n = map(int, m.groups())
        mark = "  done" if p == n else ""
        print(f"{path.stem:<34}{p:>6}{f:>6}{t:>6}{mark}")
        total_pass += p
        total += n
    print(f"\n{total_pass}/{total} tests passing")


if __name__ == "__main__":
    main()

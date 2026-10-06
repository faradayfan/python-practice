# Python interview practice

A workbook for getting Python fluent under time pressure. Each file in
`exercises/` has a problem statement, function stubs to fill in, and built-in
tests. You only need Python 3.10 or newer, with no packages to install.

```sh
python3 exercises/01_top_error_services.py   # run one exercise's tests
python3 run_all.py                           # progress table across everything
python3 run_all.py 05                        # full output for exercise 05
```

Test status: `TODO` means the stub hasn't been written yet, `FAIL` shows the
failing line and the expected and actual values, and `ok` means the test passed.

## Order of work

| # | File | Focus | Target |
|---|------|-------|--------|
| 01 | top_error_services | The warm-up from the prep session | 10 min |
| 02 | core_idioms | Comprehensions, slicing, zip, unpacking | 15 min |
| 03 | sorting_and_strings | `key=` sorting, stability, f-string formatting, groupby | 20 min |
| 04 | counter_defaultdict | `Counter`, `defaultdict` | 20 min |
| 05 | deque_heapq | `deque`, `heapq`, two-heap median | 25 min |
| 06 | itertools_functools_bisect | `combinations`, `product`, `accumulate`, `cache`, `bisect` | 20 min |
| 07 | two_pointers_sliding_window | O(n) array patterns | 30 min |
| 08 | stacks | Brackets, RPN, monotonic stack | 25 min |
| 09 | graphs_bfs_dfs | Grids, BFS shortest path, topological sort | 35 min |
| 10 | binary_search | Hand-written bounds, search on the answer | 25 min |
| 11 | dynamic_programming | Top-down and bottom-up | 40 min |
| 12 | gotchas_fix_the_bugs | **Already written but buggy.** Fix the classic traps | 20 min |
| 13 | log_parsing | Regex, datetime, and percentiles (SRE-style) | 35 min |
| 14 | nested_data_and_csv | Flatten, merge, path lookup, csv | 30 min |
| 15 | pythonic_classes | dataclass, dunders, LRU, generators, context managers, decorators | 35 min |
| 16 | mock_interview | 45 minutes, timed, with no outside help | 45 min |

If the role is platform or SRE, move 13 and 14 up right after 06.

## How to practise

1. **Time yourself** against the target. Going over is fine, but write down by how much.
2. **Talk out loud**: state your approach and its complexity before you code.
3. **Get it passing, then make it idiomatic.** Once the tests are green, ask
   yourself whether a Python developer would write it this way. Watch for
   `range(len(...))`, manual counting dicts, and index juggling that `zip` or
   `enumerate` would handle.
4. **Get a review.** Paste your solution to Claude and ask for an
   interviewer-style review that covers correctness, idiom, and what an
   interviewer would think.
5. **Redo it cold.** A few days later, delete your solution and solve it
   again. Fluency comes from repetition.

A note on files 12 and 15: file 12 starts with every test failing because
the code is deliberately buggy. In file 15, the `Vector` and `Timer` stubs
show as `FAIL` rather than `TODO` until you write them.

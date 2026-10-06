"""
13 - Practical: access-log analysis  (target: 35 minutes)

The kind of task platform/SRE interviews favour. Each line looks like:

  10.0.0.1 - - [06/Oct/2026:10:00:01 +0000] "GET /api/users?page=2 HTTP/1.1" 200 512 0.123

  ip, two dashes, [timestamp], "METHOD PATH PROTOCOL", status, bytes, latency seconds

Idioms to reach for: re (named groups, re.fullmatch / compiled patterns),
datetime.strptime / strftime, math.ceil, Counter, defaultdict(list),
heapq.nlargest. Build on parse_line in the later functions.
"""

from _harness import check, main


def parse_line(line: str) -> dict | None:
    """Return {"ip", "time" (datetime, tz-aware), "method", "path", "status" (int),
    "bytes" (int), "latency" (float)}, or None if the line doesn't match the format.
    "path" excludes any query string.
    """
    raise NotImplementedError


def status_classes(lines: list[str]) -> dict[str, int]:
    """Count valid lines by status class: {"2xx": 3, "5xx": 1}. Only classes present."""
    raise NotImplementedError


def p95_latency_by_path(lines: list[str]) -> dict[str, float]:
    """95th percentile latency per path using nearest-rank:
    sort the latencies, take the element at index ceil(0.95 * n) - 1.
    """
    raise NotImplementedError


def requests_per_minute(lines: list[str]) -> dict[str, int]:
    """Count requests per minute, keyed "YYYY-MM-DD HH:MM" in UTC."""
    raise NotImplementedError


def slowest(lines: list[str], n: int) -> list[tuple[float, str]]:
    """The n slowest requests as (latency, path), slowest first."""
    raise NotImplementedError


# ---------------------------------------------------------------- tests

LOG = [
    '10.0.0.1 - - [06/Oct/2026:10:00:01 +0000] "GET /api/users?page=2 HTTP/1.1" 200 512 0.120',
    '10.0.0.2 - - [06/Oct/2026:10:00:30 +0000] "POST /api/login HTTP/1.1" 401 64 0.050',
    '10.0.0.1 - - [06/Oct/2026:10:00:59 +0000] "GET /api/users HTTP/1.1" 200 2048 0.300',
    'garbage line that should be ignored',
    '10.0.0.3 - - [06/Oct/2026:10:01:05 +0000] "GET /api/orders HTTP/1.1" 500 0 1.500',
    '10.0.0.3 - - [06/Oct/2026:12:01:15 +0200] "GET /api/users HTTP/1.1" 204 0 0.200',
]


def test_parse_line():
    rec = parse_line(LOG[0])
    check(rec["ip"], "10.0.0.1")
    check(rec["method"], "GET")
    check(rec["path"], "/api/users")
    check(rec["status"], 200)
    check(rec["bytes"], 512)
    check(rec["latency"], 0.12)
    check(rec["time"].isoformat(), "2026-10-06T10:00:01+00:00")
    check(parse_line(LOG[3]), None)
    check(parse_line(""), None)


def test_status_classes():
    check(status_classes(LOG), {"2xx": 3, "4xx": 1, "5xx": 1})


def test_p95_latency_by_path():
    check(p95_latency_by_path(LOG), {
        "/api/users": 0.3, "/api/login": 0.05, "/api/orders": 1.5,
    })
    many = [f'1.1.1.1 - - [06/Oct/2026:10:00:00 +0000] "GET /x HTTP/1.1" 200 1 {i}.0'
            for i in range(1, 21)]
    check(p95_latency_by_path(many), {"/x": 19.0})


def test_requests_per_minute():
    check(requests_per_minute(LOG), {"2026-10-06 10:00": 3, "2026-10-06 10:01": 2})


def test_slowest():
    check(slowest(LOG, 2), [(1.5, "/api/orders"), (0.3, "/api/users")])


if __name__ == "__main__":
    main(globals())

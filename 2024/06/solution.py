#!/usr/bin/env python3
#      --- Day 6: Guard Gallivant ---
#   https://adventofcode.com/2024/day/6

from time import perf_counter

Point = tuple[int, int]


def profiler(method):
    def wrapper_method(*arg, **kw):
        t = perf_counter()
        ret = method(*arg, **kw)
        t = perf_counter() - t
        print("Method " + method.__name__ + " took : " + "{:2.9f}".format(t) + " sec")
        return ret

    return wrapper_method


@profiler
def part1(start: Point, obstacles: set[Point]) -> int:
    x, y = start
    maxx = max(x for x, _ in obstacles)
    maxy = max(y for _, y in obstacles)
    path: set[Point] = {start}
    dx, dy = 0, -1
    while True:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx > maxx or ny < 0 or ny > maxy:
            break
        if (nx, ny) in obstacles:
            dx, dy = -dy, dx
            continue
        x, y = nx, ny
        path.add((x, y))
    return len(path)


@profiler
def part2(start: Point, obstacles: set[Point], dist: list[list[int]]) -> int:
    x, y = start
    maxx = max(x for x, y in obstacles)
    maxy = max(y for x, y in obstacles)
    added: set[Point] = set()
    path: set[Point] = set()
    dx, dy = 0, -1
    while True:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx > maxx or ny < 0 or ny > maxy:
            break
        if (nx, ny) in obstacles:
            dx, dy = -dy, dx
            continue
        x, y = nx, ny
        path.add((x, y))

    for p in path:
        if p in added:
            continue
        x, y = start
        dx, dy = 0, -1
        newpath: set[tuple[int, int, int, int]] = {(x, y, dx, dy)}
        newobstacles = obstacles | {p}
        while True:
            if x != p[0] and y != p[1]:
                # Ray marching
                k = dist[y][x]
                while k:
                    x += k * dx
                    y += k * dy
                    k = dist[y][x]
            nx, ny = x + dx, y + dy
            if nx < 0 or nx > maxx or ny < 0 or ny > maxy:
                break
            if (nx, ny) in newobstacles:
                dx, dy = -dy, dx
                continue
            if (nx, ny, dx, dy) in newpath:
                added.add(p)
                break
            x, y = nx, ny
            newpath.add((x, y, dx, dy))

    return len(added)


def parse(input_data: str) -> tuple[Point, set[Point], list[list[int]]]:
    lines = input_data.splitlines()
    obstacles: set[Point] = set()
    start: Point = (0, 0)
    dist: list[list[int]] = []
    W, H = len(lines[0]), len(lines)
    for y, line in enumerate(lines):
        dline: list[int] = []
        dist.append(dline)
        for x, c in enumerate(line):
            if c == "#":
                obstacles.add((x, y))
            if c == "^":
                start = (x, y)
            dline.append(min(x, abs(W - 1 - x), y, abs(H - 1 - y)))
    assert x == y
    for y in range(H):
        for x in range(H):
            for k in range(H):
                if (k, y) in obstacles:
                    dist[y][x] = min(dist[y][x], abs(k - x) - 1)
                if (x, k) in obstacles:
                    dist[y][x] = min(dist[y][x], abs(k - y) - 1)
    return start, obstacles, dist


def main(input_data: str):
    start, obstacles, dist = parse(input_data)
    print("P1: ", part1(start, obstacles))
    print("P2: ", part2(start, obstacles, dist))


if __name__ == "__main__":
    from pathlib import Path

    main(open(Path(__file__).parent / "input").read().strip())

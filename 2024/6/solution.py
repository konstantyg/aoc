#!/usr/bin/env python3
#      --- Day 6: Guard Gallivant ---
#   https://adventofcode.com/2024/day/6


def part1(start, obstacles):
    x, y = start
    maxx = max(x for x, y in obstacles)
    maxy = max(y for x, y in obstacles)
    path = set()
    dx, dy = 0, -1
    while x >= 0 and x <= maxx and y >= 0 and y <= maxy:
        if (x, y) in obstacles:
            x, y = x - dx, y - dy
            dx, dy = -dy, dx
        path.add((x, y))
        x, y = x + dx, y + dy
    return len(path)


def part2(start, obstacles):
    x, y = start
    maxx = max(x for x, y in obstacles)
    maxy = max(y for x, y in obstacles)
    added = set()
    path = set()
    dx, dy = 0, -1
    while x >= 0 and x <= maxx and y >= 0 and y <= maxy:
        if (x, y) in obstacles:
            x, y = x - dx, y - dy
            dx, dy = -dy, dx
        path.add((x, y))
        x, y = x + dx, y + dy
    path = path - {start}

    for ox, oy in path:
        if (ox, oy) in added:
            continue
        x, y = start
        dx, dy = 0, -1
        newpath = set()
        newobstacles = obstacles | {(ox, oy)}
        while x >= 0 and x <= maxx and y >= 0 and y <= maxy:
            if (x, y) in newobstacles:
                x, y = x - dx, y - dy
                dx, dy = -dy, dx
            if (x, y, dx, dy) in newpath:
                added.add((ox, oy))
                break
            newpath.add((x, y, dx, dy))
            x, y = x + dx, y + dy

    return len(added)


def parse(input_data: str):
    obstacles = set()
    start = (0, 0)
    for y, line in enumerate(input_data.splitlines()):
        for x, c in enumerate(line):
            if c == "#":
                obstacles.add((x, y))
            if c == "^":
                start = (x, y)
    return start, obstacles


def main(input_data: str):
    start, obstacles = parse(input_data)
    print("P1: ", part1(start, obstacles))
    print("P2: ", part2(start, obstacles))


if __name__ == "__main__":
    from pathlib import Path

    main(open(Path(__file__).parent / "input").read().strip())

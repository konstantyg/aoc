#!/usr/bin/env python3
#   --- Day 8: Resonant Collinearity ---
#   https://adventofcode.com/2024/day/8


from itertools import combinations

Point = tuple[int, int]


def part1(data: dict[str, list[Point]], size: Point) -> int:
    max_x, max_y = size
    s: set[Point] = set()
    for c, points in data.items():
        for p1, p2 in combinations(points, 2):
            x1, y1 = p1
            x2, y2 = p2
            dx, dy = x2 - x1, y2 - y1
            s.add((x1 - dx, y1 - dy))
            s.add((x2 + dx, y2 + dy))
    s = {(x, y) for x, y in s if 0 <= x < max_x and 0 <= y < max_y}

    return len(s)


def part2(data: dict[str, list[Point]], size: Point) -> int:
    max_x, max_y = size
    s: set[Point] = set()
    for c, points in data.items():
        s |= set(points)
        for p1, p2 in combinations(points, 2):
            x1, y1 = p1
            x2, y2 = p2
            dx, dy = x2 - x1, y2 - y1
            while 0 <= x1 - dx < max_x and 0 <= y1 - dy < max_y:
                s.add((x1 - dx, y1 - dy))
                x1 -= dx
                y1 -= dy
            x1, y1 = p1
            x2, y2 = p2
            while 0 <= x2 + dx < max_x and 0 <= y2 + dy < max_y:
                s.add((x2 + dx, y2 + dy))
                x2 += dx
                y2 += dy
    return len(s)


def parse(input_data: str) -> tuple[dict[str, list[Point]], Point]:
    data: dict[str, list[Point]] = {}
    for y, line in enumerate(input_data.splitlines()):
        for x, c in enumerate(line):
            if c == ".":
                continue
            if c not in data:
                data[c] = []
            data[c].append((x, y))
    return (data, (x + 1, y + 1))


def main(input_data: str):
    data, size = parse(input_data)
    print("P1: ", part1(data, size))
    print("P2: ", part2(data, size))


if __name__ == "__main__":
    from pathlib import Path

    main(open(Path(__file__).parent / "input").read().strip())

#!/usr/bin/env python3
#   --- Day 8: Resonant Collinearity ---
#   https://adventofcode.com/2024/day/8


from itertools import permutations

Point = tuple[int, int]


def part1(data: dict[str, list[Point]], size: Point) -> int:
    max_x, max_y = size
    s: set[Point] = set()
    for c, points in data.items():
        for (x1, y1), (x2, y2) in permutations(points, 2):
            s.add((2 * x1 - x2, 2 * y1 - y2))
    s = {(x, y) for x, y in s if 0 <= x < max_x and 0 <= y < max_y}
    return len(s)


def part2(data: dict[str, list[Point]], size: Point) -> int:
    max_x, max_y = size
    s: set[Point] = set()
    for c, points in data.items():
        s |= set(points)
        for (x1, y1), (x2, y2) in permutations(points, 2):
            dx, dy = x2 - x1, y2 - y1
            while 0 <= (x1 := x1 - dx) < max_x and 0 <= (y1 := y1 - dy) < max_y:
                s.add((x1, y1))
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

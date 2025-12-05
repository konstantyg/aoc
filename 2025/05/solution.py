#!/usr/bin/env python3
#         --- Day 5: Cafeteria ---
#   https://adventofcode.com/2025/day/5


def part1(data: tuple[list[tuple[int, int]], list[int]]) -> int:
    s: int = 0
    ranges, ingredients = data
    for i in ingredients:
        for x, y in ranges:
            if x <= i <= y:
                s += 1
                break
    return s


def part2(data: tuple[list[tuple[int, int]], list[int]]) -> int:
    ranges, _ = data
    sorted_ranges = sorted(ranges)
    merged = []
    for x, y in sorted_ranges:
        if merged and x <= merged[-1][1] + 1:
            # Overlapping or adjacent
            merged[-1] = (merged[-1][0], max(merged[-1][1], y))
        else:
            # Non-overlapping - add as new range
            merged.append((x, y))

    return sum(y - x + 1 for x, y in merged)


def parse(input_data: str) -> tuple[list[tuple[int, int]], list[int]]:
    ranges = []
    ingredients = []
    part1 = True
    for line in input_data.splitlines():
        if line.strip() == "":
            part1 = False
            continue
        if part1:
            x, y = map(int, line.strip().split("-"))
            ranges.append((x, y))
        else:
            ingredients.append(int(line.strip()))

    return ranges, ingredients


def main(input_data: str):
    data = parse(input_data)
    return part1(data), part2(data)


def test_solution():
    example_input = """3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""
    assert main(example_input) == (3, 14), "Invalid solution for the example input"


if __name__ == "__main__":
    from pathlib import Path

    r1, r2 = main(open(Path(__file__).parent / "input").read().strip())
    print(f"P1: {r1}  P2: {r2}")

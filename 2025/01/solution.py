#!/usr/bin/env python3
#      --- Day 1: Secret Entrance ---
#   https://adventofcode.com/2025/day/1


def part1(data: list[int]) -> int:
    s: int = 50
    c: int = 0
    for v in data:
        s += v
        s = s % 100
        if s == 0:
            c += 1
    return c


def part2(data: list[int]) -> int:
    c: int = 0
    s: int = 50
    for v in data:
        prev0: bool = s == 0
        s += v
        if s == 0:
            c += 1
        elif s >= 100:
            c += s // 100
        elif s < 0:
            c += s // -100
            if not prev0:
                c += 1
        s %= 100

    return c


def parse(input_data: str) -> list[int]:
    sequence = []
    for line in input_data.splitlines():
        sign = line[0]
        value = int(line[1:])
        sequence.append(value if sign == "R" else -value)

    return sequence


def main(input_data: str):
    data = parse(input_data)
    return part1(data), part2(data)


def test_solution():
    example_input = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""
    assert main(example_input) == (3, 6), "Invalid solution for the example input"


if __name__ == "__main__":
    from pathlib import Path

    r1, r2 = main(open(Path(__file__).parent / "input").read().strip())
    print(f"P1: {r1}  P2: {r2}")

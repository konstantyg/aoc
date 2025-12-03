#!/usr/bin/env python3
#           --- Day 3: Lobby ---                              
#   https://adventofcode.com/2025/day/3   

from itertools import combinations


def part1(data: list[tuple[int, int]]) -> int:
    s: int = 0
    for l in data:
        m = 0
        for x, y in combinations(l, 2):
            m = max(m, (10 * x) + y)
        s += m
    return s


def part2(data: list[tuple[int, int]]) -> int:
    s: int = 0
    for inp in data:
        ret = 0
        len_inp = len(inp)
        start_chunk = 0
        for i in range(11, -1, -1):
            chunk = inp[start_chunk : len_inp - i]
            max_val = max(chunk)
            ret = (10 * ret) + max_val
            start_chunk += chunk.index(max_val) + 1
        s += ret
    return s


def parse(input_data: str) -> list[list[int]]:
    sequence = []
    for line in input_data.splitlines():
        sequence.append(list(map(int, line.strip())))

    return sequence


def main(input_data: str):
    data = parse(input_data)
    return part1(data), part2(data)


def test_solution():
    example_input = """987654321111111
811111111111119
234234234234278
818181911112111
"""
    assert main(example_input) == (357, 3121910778619), "Invalid solution for the example input"


if __name__ == "__main__":
    from pathlib import Path

    r1, r2 = main(open(Path(__file__).parent / "input").read().strip())
    print(f"P1: {r1}  P2: {r2}")

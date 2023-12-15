#!/usr/bin/env python3

from itertools import pairwise

def find_next(data: list[int]) -> int:
    """Find the next number in the sequence"""
    l = [b-a for a, b in pairwise(data)]
    if set(l) == {0}:
        return  data[0]
    return data[-1] + find_next(l)

def part1(data: list[list[int]]) -> int:
    return sum(find_next(x) for x in data)


def part2(data: list[list[int]]) -> int:
    return sum(find_next(x[::-1]) for x in data)


def parse(input_data: str) -> list[list[int]]:
    return [list(map(int, line.split()))for line in input_data.splitlines()]

def main(input_data: str):
    data = parse(input_data)
    return part1(data), part2(data)


if __name__ == "__main__":
    from libs.run import run

    run(main)

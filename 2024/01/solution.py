#!/usr/bin/env python3
#   --- Day 1: Historian Hysteria ---
#  https://adventofcode.com/2024/day/1

from collections import Counter
from typing import TypeVar
import pytest

InputType = tuple[list[int], list[int]]

def part1(data: InputType):
    s = 0
    for l, r in zip(sorted(data[0]), sorted(data[1])):
        s += abs(l - r)
    return s


def part2(data: InputType):
    c2c = Counter(data[1])
    return sum((e * c2c[e] for e in data[0]))


def parse(input_data: str) -> InputType:
    l1, l2 = [], []
    for line in input_data.splitlines():
        a, b = map(int, line.split())
        l1.append(a)
        l2.append(b)
    return (l1, l2)


def main(input_data: str):
    data = parse(input_data)
    print("P1: ", part1(data))
    print("P2: ", part2(data))

def test_solution():
    pass

if __name__ == "__main__":
    main(open("input").read().strip())

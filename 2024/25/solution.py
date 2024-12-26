#!/usr/bin/env python3
#      --- Day 25: Code Chronicle ---
#   https://adventofcode.com/2024/day/25

from itertools import combinations


def process(locks, keys) -> int:
    s = 0
    for lock in locks:
        for key in keys:
            if any(k + l > 7 for k, l in zip(key, lock)):
                continue
            s += 1
    return s


def parse(input_data: str):
    locks = []
    keys = []
    for group in input_data.split("\n\n"):
        group = group.splitlines()
        c = [c.count("#") for c in zip(*group[::-1])]
        if set(group[0]) == {"#"}:
            locks.append(c)

        else:
            keys.append(c)
    return locks, keys


def by_cmp(input_data: str) -> int:
    return sum(
        not any(x == y == "#" for x, y in zip(a, b))
        for a, b in combinations(input_data.split("\n\n"), 2)
    )


def main(input_data: str):
    locks, keys = parse(input_data)
    p1 = process(locks, keys)
    print("P1: ", p1)
    print("P1: ", by_cmp(input_data))


if __name__ == "__main__":
    from pathlib import Path

    main(open(Path(__file__).parent / "input").read().strip())

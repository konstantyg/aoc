#!/usr/bin/env python3

import re
from functools import cache

h = re.compile(r"([#]+)")


@cache
def find_comb(p: str, c: tuple[int, ...]) -> int:
    if len(p) == 0:
        if len(c) == 0:
            return 1
        return 0

    curr = p[0]
    if curr == "#":
        if len(c) == 0 or len(p) < c[0]:
            return 0

        if "." in p[0 : c[0]]:
            return 0

        if p[c[0] :].startswith("#"):
            return 0

        if len(p) > c[0]:
            if p[c[0]] == "?":
                return find_comb(p[c[0] + 1 :].lstrip("."), c[1:])

        return find_comb(p[c[0] :].lstrip("."), c[1:])
    elif curr == ".":
        return find_comb(p.lstrip("."), c)
    elif curr == "?":
        return find_comb("#" + p[1:], c) + find_comb(p[1:].lstrip("."), c)
    assert False  # should not happen


def part1(data: list[tuple[str, tuple[int, ...]]]) -> int:
    return sum(find_comb(p, c) for p, c in data)


def part2(data: list[tuple[str, tuple[int, ...]]]) -> int:
    return sum(find_comb("?".join([p] * 5), c * 5) for p, c in data)


def parse(input_data: str):
    data: list[tuple[str, tuple[int, ...]]] = []
    for line in input_data.splitlines():
        p, c = line.split(" ")
        c = tuple(map(int, c.split(",")))
        data.append((p, c))
    return data


def main(input_data: str):
    data = parse(input_data)
    return part1(data), part2(data)


if __name__ == "__main__":
    from libs.run import run

    run(main)

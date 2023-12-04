#!/usr/bin/env python3

from dataclasses import dataclass
import re
from collections import deque


def part1(data: list[tuple[int, int]]):
    s = 0
    for _, wins in data:
        if wins:
            s += 1 << wins - 1
    return s


def part2(data: list[tuple[int, int]]):
    counts = {x[0]: 1 for x in data}
    for game, wins in data:
        if wins:
            for q in range(game, game + wins):
                counts[q + 1] += counts[game]

    return sum(counts.values())


def parse(input_data: str):
    data: list[tuple[int, int]] = []
    re_num = re.compile(r"\d+")
    for line in input_data.splitlines():
        g, d = line.split(":")
        game = int(g[4:])
        n, w = d.split("|")
        nums = set(map(int, re_num.findall(n)))
        winning = set(map(int, re_num.findall(w)))
        data.append((game, len(nums & winning)))
    return data


def main(input_data: str):
    data = parse(input_data)
    return part1(data), part2(data)


if __name__ == "__main__":
    from libs.run import run

    run(main)

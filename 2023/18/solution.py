#!/usr/bin/env python3

from itertools import pairwise
from typing import TypeAlias


Inst: TypeAlias = tuple[str, int]
Point: TypeAlias = tuple[int, int]


steps = {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}


def area(instructions: list[Inst]) -> int:
    x = 1000000
    y = 1000000

    points: list[Point] = [(x, y)]
    outside = 0
    for d, s in instructions:
        dx, dy = steps[d]
        x += dx * s
        y += dy * s
        outside += s
        points.append((x, y))

    area2 = 0
    for (p1x, p1y), (p2x, p2y) in pairwise(points):
        area2 += p1x * p2y - p2x * p1y
    return (abs(area2) + outside) // 2 + 1


def part1(instructions: list[tuple[Inst, Inst]]) -> int:
    return area([i for i, _ in instructions])


def part2(instructions: list[tuple[Inst, Inst]]) -> int:
    return area([i for _, i in instructions])


def parse(input_data: str) -> list[tuple[Inst, Inst]]:
    instructions = []
    dirs = {"0": "R", "1": "D", "2": "L", "3": "U"}
    for line in input_data.splitlines():
        (d, s, h) = line.split()
        instructions.append(((d, int(s)), (dirs[h[-2]], int(h[2:-2], base=16))))
    return instructions


def main(input_data: str):
    nodes = parse(input_data)
    return part1(nodes), part2(nodes)


if __name__ == "__main__":
    from libs.run import run

    run(main)

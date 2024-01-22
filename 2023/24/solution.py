#!/usr/bin/env python3

from dataclasses import dataclass
from itertools import combinations
from typing import TypeAlias
import re


@dataclass
class Stone:
    x: int
    y: int
    z: int
    vx: int
    vy: int
    vz: int


def intersect(a: Stone, b: Stone, minv: int, maxv: int) -> bool:
    den = a.vx * b.vy - b.vx * a.vy
    if den == 0:
        return False
    q1 = a.x * (a.y + a.vy) - a.y * (a.x + a.vx)
    q2 = b.x * (b.y + b.vy) - b.y * (b.x + b.vx)
    x = (b.vx * q1 - a.vx * q2) / -den
    y = (b.vy * q1 - a.vy * q2) / -den
    if minv <= x <= maxv and minv <= y <= maxv:
        if a.vx < 0 and x > a.x:
            return False
        if a.vx > 0 and x < a.x:
            return False
        if a.vy < 0 and y > a.y:
            return False
        if a.vy > 0 and y < a.y:
            return False

        if b.vx < 0 and x > b.x:
            return False
        if b.vx > 0 and x < b.x:
            return False
        if b.vy < 0 and y > b.y:
            return False
        if b.vy > 0 and y < b.y:
            return False

        return True
    return False


def part1(stones: list[Stone]) -> int:
    r = 0
    for a, b in combinations(stones, 2):
        if intersect(a, b, 200000000000000, 400000000000000):
            # if intersect(a,b,7,27):
            r += 1
    return r


def part2(stones: list[Stone]) -> int:
    import z3

    x, y, z, vx, vy, vz = z3.Ints("x y z vx vy vz")
    ts = [z3.Int("t" + str(i)) for i in range(len(stones))]

    solver = z3.Solver()
    for i, s in enumerate(stones):
        solver.add(s.x + s.vx * ts[i] == x + vx * ts[i])
        solver.add(s.y + s.vy * ts[i] == y + vy * ts[i])
        solver.add(s.z + s.vz * ts[i] == z + vz * ts[i])
    solver.check()
    model = solver.model()
    result = model.evaluate(x + y + z)
    return result.as_long()


def parse(input_data: str) -> list[Stone]:
    d = re.compile(r"(-?\d+)")
    s = [Stone(*map(int, d.findall(l))) for l in input_data.splitlines()]
    return s


def main(input_data: str):
    stones = parse(input_data)
    return part1(stones), part2(stones)


if __name__ == "__main__":
    from libs.run import run

    run(main)

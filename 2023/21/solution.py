#!/usr/bin/env python3

from typing import TypeAlias


Inst: TypeAlias = tuple[str, int]
Point: TypeAlias = tuple[int, int]


steps = ((1, 0), (0, 1), (-1, 0), (0, -1))


def get_next(garden, mx, my, pos):
    x, y = pos
    for dx, dy in steps:
        if 0 <= x + dx < mx and 0 <= y + dy < my:
            npos = (x + dx, y + dy)
            if npos not in garden:
                yield npos


def get_next2(garden, mx, my, pos):
    x, y = pos
    for dx, dy in steps:
        nx = x + dx
        ny = y + dy
        if (nx % mx, ny % my) not in garden:
            yield (nx, ny)


def part1(garden, mxy, start) -> int:
    mx, my = mxy
    p = set([start])
    for step in range(64):
        np = set()
        for pos in p:
            for npos in get_next(garden, mx, my, pos):
                np.add(npos)
        p = np
    return len(p)


def find_prime_facs(n):
    list_of_factors = []
    i = 2
    while n > 1:
        if n % i == 0:
            list_of_factors.append(i)
            n = n / i
            i = i - 1
        i += 1
    return list_of_factors


def part2(garden, mxy, start) -> int:
    mx, my = mxy
    p = set([start])
    ns = 26501365
    primes = set(find_prime_facs(ns))
    steps = {}
    for step in range(1, ns + 1):
        np = set()
        for pos in p:
            for npos in get_next2(garden, mx, my, pos):
                np.add(npos)
        p = np
        if step % mx == ns % mx:
            steps[step // mx] = len(p)
        if len(steps) == 3:
            break
    else:
        return len(p)
    y0 = steps[0]
    y1 = steps[1]
    y2 = steps[2]
    a = (y2 + y0 - 2 * y1) / 2
    b = y1 - y0 - a
    c = y0
    n = ns // mx
    return int(a * n**2 + b * n + c)


def parse(input_data: str):
    garden = set()
    dirs = {"0": "R", "1": "D", "2": "L", "3": "U"}
    start = (0, 0)
    for y, line in enumerate(input_data.splitlines()):
        for x, c in enumerate(line):
            if c == "#":
                garden.add((x, y))
            elif c == "S":
                start = (x, y)
    mxy = (x + 1, y + 1)
    return garden, mxy, start


def main(input_data: str):
    garden, mxy, start = parse(input_data)
    return part1(garden, mxy, start), part2(garden, mxy, start)


if __name__ == "__main__":
    from libs.run import run

    run(main)

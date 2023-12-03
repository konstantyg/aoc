#!/usr/bin/env python3

import re


def part1(borders, symbols) -> int:
    return sum(num for num, border in borders if border & symbols)


def part2(borders, gears) -> int:
    s = 0
    for gear in gears:
        g = []
        for num, border in borders:
            if border & set([gear]):
                g.append(num)
        if len(g) == 2:
            s += g[0] * g[1]
    return s


def parse(input_data: str):
    borders = []
    symbols = set()
    gears = set()
    re_num = re.compile(r"\d+")
    re_symbol = re.compile(r"[^0-9.]")
    for y, line in enumerate(input_data.splitlines(), 1):
        for m in re_num.finditer(line):
            adj = set([(m.start(), y), (m.end() + 1, y)])
            for x in range(m.start(), m.end() + 2):
                adj.add((x, y - 1))
                adj.add((x, y + 1))
            borders.append((int(m[0]), adj))
        for m in re_symbol.finditer(line):
            symbols.add((m.end(), y))
            if m[0] == "*":
                gears.add((m.end(), y))
    return borders, symbols, gears


def main(input_data: str):
    borders, symbols, gears = parse(input_data)
    return part1(borders, symbols), part2(borders, gears)


if __name__ == "__main__":
    from libs.run import run

    run(main)

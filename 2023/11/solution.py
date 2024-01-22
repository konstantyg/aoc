#!/usr/bin/env python3

from itertools import combinations


def distance(ax, ay, bx, by, empty_x, empty_y, expand=2):
    if bx < ax:
        ax, bx = bx, ax
    if by < ay:
        ay, by = by, ay
    x_len = bx - ax + len(empty_x & set(range(ax, bx + 1))) * (expand - 1)
    y_len = by - ay + len(empty_y & set(range(ay, by + 1))) * (expand - 1)
    return x_len + y_len


def part1(data, empty_x, empty_y) -> int:
    return sum(
        distance(ax, ay, bx, by, empty_x, empty_y)
        for (ax, ay), (bx, by) in combinations(data, 2)
    )


def part2(data, empty_x, empty_y) -> int:
    return sum(
        distance(ax, ay, bx, by, empty_x, empty_y, 1_000_000)
        for (ax, ay), (bx, by) in combinations(data, 2)
    )


def parse(input_data: str):
    data = []
    empty_y = set()
    for y, line in enumerate(input_data.splitlines()):
        if "#" in line:
            for x, c in enumerate(line):
                if c == "#":
                    data.append((x, y))
        else:
            empty_y.add(y)
    empty_x = set()
    for x, col in enumerate(zip(*input_data.splitlines())):
        if "#" not in col:
            empty_x.add(x)

    return data, empty_x, empty_y


def main(input_data: str):
    data, empty_x, empty_y = parse(input_data)
    return part1(data, empty_x, empty_y), part2(data, empty_x, empty_y)


if __name__ == "__main__":
    from libs.run import run

    run(main)

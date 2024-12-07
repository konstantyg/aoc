#!/usr/bin/env python3
#       --- Day 7: Bridge Repair ---
#   https://adventofcode.com/2024/day/7


def valid(res: int, elems: list[int], part2: bool = False) -> bool:
    results = [elems[0]]
    for i in elems[1:]:
        newresults = []
        for r in results:
            if part2:
                newresults.extend([r + i, r * i, int(f"{r}{i}")])
            else:
                newresults.extend([r + i, r * i])
        results = newresults
    return any(result == res for result in results)


def part1(data: list[list[int]]) -> int:
    s = 0
    for line in data:
        res, *elems = line
        if valid(res, elems):
            s += res

    return s


def part2(data: list[list[int]]) -> int:
    s = 0
    for line in data:
        res, *elems = line
        if valid(res, elems, True):
            s += res

    return s


def parse(input_data: str) -> list[list[int]]:
    data: list[list[int]] = []
    for line in input_data.splitlines():
        data.append(list(map(int, line.replace(":", "").split())))
    return data


def main(input_data: str):
    data = parse(input_data)
    print("P1: ", part1(data))
    print("P2: ", part2(data))


if __name__ == "__main__":
    from pathlib import Path

    main(open(Path(__file__).parent / "input").read().strip())

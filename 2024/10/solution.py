#!/usr/bin/env python3
#         --- Day 10: Hoof It ---
#   https://adventofcode.com/2024/day/10

from collections import deque


def paths(data: dict[tuple[int, int], int]) -> int:
    s = 0
    pos = deque([(k, k) for k, v in data.items() if v == 0])
    reach: dict[tuple[int, int], set] = dict()
    while pos:
        start, cords = pos.popleft()
        x, y = cords
        h = data[cords] + 1
        if h == 10:
            if start not in reach:
                reach[start] = set()
            reach[start].add(cords)
            s += 1
            continue
        for npos in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if data.get(npos, -1) == h:
                pos.append((start, npos))

    return sum(len(v) for v in reach.values()), s


def parse(input_data: str) -> dict[tuple[int, int], int]:
    data: dict[tuple[int, int], int] = {}
    for y, line in enumerate(input_data.splitlines()):
        for x, h in enumerate(line):
            if h.isdigit():
                data[(x, y)] = int(h)
    return data


def main(input_data: str):
    data = parse(input_data)
    p1, p2 = paths(data)
    print("P1: ", p1)
    print("P2: ", p2)


if __name__ == "__main__":
    from pathlib import Path

    main(open(Path(__file__).parent / "input").read().strip())

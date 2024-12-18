#!/usr/bin/env python3
#         --- Day 18: RAM Run ---
#   https://adventofcode.com/2024/day/18

from heapq import heappop, heappush

Point = tuple[int, int]


class PathBlocked(Exception):
    pass


def part1(blocks: list[Point], num_falled: int = 1024) -> int:
    start = (0, 0)
    mx, my = max(x for x, _ in blocks), max(y for _, y in blocks)
    end = (mx, my)
    grid = {(x, y) for x, y in blocks[:num_falled]}

    paths: list[tuple[int, Point]] = [(0, start)]

    # for best scores
    visited_scores: dict[Point, int] = {}
    vd: set[Point] = set()

    while paths:
        score, path = heappop(paths)
        if path == end:
            return score
        if path in vd:
            continue
        vd.add(path)
        x, y = path
        for nx, ny in [
            (x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x, y - 1),
        ]:
            np = (nx, ny)
            if np in grid or nx < 0 or ny < 0 or nx > mx or ny > my:
                continue
            if visited_scores.get(np, float("inf")) < score:
                continue
            visited_scores[np] = score + 1
            heappush(paths, (score + 1, np))

    raise PathBlocked()


def part2(grid: list[Point]) -> str:
    low = 2
    high = len(grid)
    found = False
    while high - low > 1:
        test_split: int = (low + high) // 2
        try:
            part1(grid, test_split)
            low = test_split
        except PathBlocked:
            found = True
            high = test_split
    if found:
        return f"Path blocked at {grid[low]}"
    return "All paths not blocked"


def parse(input_data: str) -> list[Point]:
    falling_bytes = []
    for line in input_data.splitlines():
        x, y = map(int, line.split(","))
        falling_bytes.append((x, y))
    return falling_bytes


def main(input_data: str):
    falling_bytes = parse(input_data)
    print("P1: ", part1(falling_bytes, 1024))
    print("P2: ", part2(falling_bytes))


if __name__ == "__main__":
    from pathlib import Path

    main(open(Path(__file__).parent / "input").read().strip())

#!/usr/bin/env python3
#      --- Day 16: Reindeer Maze ---                          
#   https://adventofcode.com/2024/day/16    

from heapq import heappop, heappush

Point = tuple[int, int]
Direction = tuple[int, int]
PointDir = tuple[Point, Direction]
Grid = dict[Point, str]


def solve(grid: Grid) -> tuple[int, int]:
    start = next(k for k, v in grid.items() if v == "S")
    end = next(k for k, v in grid.items() if v == "E")

    # list of possible paths with score, path, and used points
    paths: list[tuple[int, PointDir, set]] = [(0, (start, (1, 0)), {start})]

    # for best scores
    visited_scores: dict[PointDir, int] = {}
    visited_points: dict[PointDir, set[Point]] = {}

    while paths:
        score, path, used_points = heappop(paths)
        (p, d) = path
        if p == end:
            return score, len(used_points)
        x, y = p
        dx, dy = d
        for new_score, pp, dd in [
            (score + 1, (x + dx, y + dy), d),
            (score + 1000, p, (-dy, -dx)),
            (score + 1000, p, (dy, dx)),
        ]:
            if pp != p and grid[pp] == "#":
                continue
            np = (pp, dd)
            if (pos_score := visited_scores.get(np, float("inf"))) <= new_score:
                if pos_score == new_score:
                    visited_points[np] |= used_points
                continue
            visited_scores[np] = new_score
            vp = visited_points[np] = used_points | {pp}
            heappush(paths, (new_score, np, vp))

    raise ValueError("no path")


def parse(input_data: str) -> Grid:
    grid = {}
    for y, line in enumerate(input_data.splitlines()):
        for x, c in enumerate(line):
            grid[(x, y)] = c
    return grid


def main(input_data: str):
    grid = parse(input_data)
    p1, p2 = solve(grid)
    print("P1: ", p1)
    print("P2: ", p2)


if __name__ == "__main__":
    from pathlib import Path

    main(open(Path(__file__).parent / "input").read().strip())

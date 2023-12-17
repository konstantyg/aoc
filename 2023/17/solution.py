#!/usr/bin/env python3

from heapq import heappop, heappush
from typing import TypeAlias

Point: TypeAlias = tuple[int, int]
Direction: TypeAlias = tuple[int, int]
Path: TypeAlias = tuple[Point, Direction]
Grid: TypeAlias = dict[Point, int]


def solve(grid: Grid, min_moves=1, max_moves=3) -> int:
    paths: list[tuple[int, Path]] = [(0, ((0, 0), (1, 0))), (0, ((0, 0), (0, 1)))]
    maxx, maxy = max(x for x, _ in grid), max(y for _, y in grid)
    end: Point = (maxx, maxy)
    visited: dict[Path, int] = {}
    vd: set[Path] = set()
    while paths:
        heat, path = heappop(paths)
        (p, d) = path
        if p == end:
            return heat
        if path in vd:
            continue
        vd.add(path)
        x, y = p
        dx, dy = d
        for dd in [(dy, dx), (-dy, -dx)]:
            ddx, ddy = dd
            newheat = heat
            for i in range(1, max_moves + 1):
                n = (x + (ddx * i), y + (ddy * i))
                if n not in grid:
                    break
                newheat += grid[n]
                if i < min_moves:
                    continue
                if visited.get((n, dd), 99999999) <= newheat:
                    continue
                visited[(n, dd)] = newheat
                heappush(paths, (newheat, (n, dd)))
    raise ValueError("No path found")


def part1(grid: Grid) -> int:
    return solve(grid)


def part2(grid: Grid) -> int:
    return solve(grid, 4, 10)


def parse(input_data: str) -> Grid:
    grid = {}
    for y, line in enumerate(input_data.splitlines()):
        for x, c in enumerate(line):
            grid[(x, y)] = int(c)
    return grid


def main(input_data: str):
    nodes = parse(input_data)
    return part1(nodes), part2(nodes)


if __name__ == "__main__":
    from libs.run import run

    run(main)

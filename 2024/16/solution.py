#!/usr/bin/env python3

from heapq import heappop, heappush
from typing import TypeAlias
from collections import defaultdict

Point: TypeAlias = tuple[int, int]
Direction: TypeAlias = tuple[int, int]
Path: TypeAlias = tuple[Point, Direction]
Grid: TypeAlias = dict[Point, str]


def solve(grid: Grid) -> tuple[int, int]:
    start = next(k for k, v in grid.items() if v == "S")
    end = next(k for k, v in grid.items() if v == "E")

    # list of possible paths with score, path, and used points
    paths: list[tuple[int, Path, set]] = [(0, (start, (1, 0)), set([start]))]

    # for best scores
    visited: dict[Path, int] = {}
    visited_points: defaultdict[Path, set] = defaultdict(set)

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
            if pp != p and grid.get(pp) == "#":
                continue
            if visited.get((pp, dd), 99999999) <= new_score:
                if visited.get((pp, dd), 99999999) == new_score:
                    visited_points[(pp, dd)] |= used_points
                continue
            visited[(pp, dd)] = new_score
            visited_points[(pp, dd)] = used_points | set([pp])
            heappush(paths, (new_score, (pp, dd), visited_points[(pp, dd)]))

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

    main("""###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
""")
    main("""#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################
""")
    main(open(Path(__file__).parent / "input").read().strip())

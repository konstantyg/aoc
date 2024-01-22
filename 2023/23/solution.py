#!/usr/bin/env python3

from typing import TypeAlias


Inst: TypeAlias = tuple[str, int]
Point: TypeAlias = tuple[int, int]


dirs: list[tuple[int, int]] = [(1, 0), (-1, 0), (0, -1), (0, 1)]
from libs.profiler import profiler


@profiler
def part1(input: dict[Point, str]) -> int:
    start, *_, end = list(input)
    paths = [(start, set([start]))]
    trails = []
    while paths:
        new_paths = []
        for curpos, path in paths:
            x, y = curpos
            for dx, dy in dirs:
                new = (x + dx, y + dy)
                if new not in input:
                    continue
                if new == end:
                    trails.append(len(path))
                    break
                if len(path) > 1 and new in path:
                    continue
                n = input[new]
                if (
                    (n == ">" and dx == -1)
                    or (n == "<" and dx == 1)
                    or (n == "^" and dy == 1)
                    or (n == "v" and dy == -1)
                ):
                    continue
                new_paths.append((new, path | set([new])))
        paths = new_paths
    return max(trails)


def connect(edges: dict[Point, set[Point]], point: Point, next: Point, dist=1):
    while len(edges[next]) == 2:
        nexts = edges[next] - set((point,))
        point, next, dist = next, nexts.pop(), dist + 1
    return next, dist


def search(
    edges: dict[Point, list[tuple[Point, int]]],
    pos: Point,
    dist: int,
    best: int,
    stop: Point,
    seen=set(),
) -> int:
    if pos == stop:
        return dist
    if pos in seen:
        return best

    seen.add(pos)
    best = max(search(edges, n, d + dist, best, stop) for n, d in edges[pos])
    seen.remove(pos)

    return best


@profiler
def part2(input: dict[Point, str]) -> int:
    points = list(input)
    steps: dict[Point, set[Point]] = {}
    for point in points:
        for dx, dy in dirs:
            new = (point[0] + dx, point[1] + dy)
            if new in points:
                if point not in steps:
                    steps[point] = set()
                steps[point].add(new)

    # leave only cross paths
    edges: dict[Point, list[tuple[Point, int]]] = {
        p: [connect(steps, p, n) for n in steps[p]] for p in points
    }

    return search(edges, points[0], 0, 0, points[-1])


def parse(input_data: str) -> dict[Point, str]:
    grid = {}
    for y, line in enumerate(input_data.splitlines()):
        for x, c in enumerate(line.strip()):
            if c == "#":
                continue
            grid[(x, y)] = c
    return grid


def main(input_data: str):
    input = parse(input_data)
    return part1(input), part2(input)


if __name__ == "__main__":
    from libs.run import run

    run(main)

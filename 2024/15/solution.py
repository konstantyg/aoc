#!/usr/bin/env python3
#      --- Day 15: Warehouse Woes ---
#   https://adventofcode.com/2024/day/15


Grid = dict[tuple[int, int], str]
Moves = str


def print_grid(grid: Grid):
    mx, my = max(x for x, _ in grid) + 1, max(y for _, y in grid) + 1
    gridmap = [["." for _ in range(mx)] for _ in range(my)]
    for (x, y), v in grid.items():
        gridmap[y][x] = v
    for row in gridmap:
        print("".join(row))
    print()


MOVES_DEF = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}


def part1(grid: Grid, moves: Moves) -> int:
    grid = grid.copy()
    sx, sy = next(k for k, v in grid.items() if v == "@")
    for m in moves:
        dx, dy = MOVES_DEF[m]
        x, y = sx, sy
        m = False
        while (c := grid[(x + dx, y + dy)]) != "#":
            if c == ".":
                if m:
                    grid[(x + dx, y + dy)] = "O"
                grid[(sx, sy)] = "."
                sx += dx
                sy += dy
                grid[(sx, sy)] = "@"
                break
            m = True
            x += dx
            y += dy
    return sum(x + y * 100 for (x, y), c in grid.items() if c == "O")


def get_possible_moves(grid, sx, sy, dy):
    ps = [(sx, sy)]
    m = []
    while ps:
        nps = []
        for x, y in ps:
            if grid[(x, y + dy)] == "#":
                return []
            if grid[(x, y + dy)] == ".":
                m.append(((x, y + dy), (x, y)))
            if grid[(x, y + dy)] == "[":
                nps.append((x, y + dy))
                nps.append((x + 1, y + dy))
                m.append(((x, y + dy), (x, y)))
            if grid[(x, y + dy)] == "]":
                nps.append((x, y + dy))
                nps.append((x - 1, y + dy))
                m.append(((x, y + dy), (x, y)))

        ps = nps

    return m[::-1]


def part2(orggrid: Grid, moves: Moves) -> int:
    grid = {}
    # make wider
    for (x, y), v in orggrid.items():
        if v == "O":
            v = "["
        grid[(2 * x, y)] = v
        if v == "[":
            v = "]"
        if v == "@":
            v = "."
        grid[(2 * x + 1, y)] = v

    sx, sy = next(k for k, v in grid.items() if v == "@")

    for m in moves:
        dx, dy = MOVES_DEF[m]
        x, y = sx, sy
        m = False
        if grid[(x + dx, y + dy)] == ".":
            grid[(sx, sy)] = "."
            sx += dx
            sy += dy
            grid[(sx, sy)] = "@"
            continue
        if dy == 0:
            while (c := grid[(x + dx, y)]) != "#":
                if c == ".":
                    for cx in range(x + dx, sx, -dx):
                        grid[(cx, y)] = grid[(cx - dx, y)]
                    grid[(sx, sy)] = "."
                    sx += dx
                    break
                x += dx
            continue

        pmoves = get_possible_moves(grid, sx, sy, dy)
        if not pmoves:
            continue
        dest = set()
        org = set()
        for p1, p2 in pmoves:
            dest.add(p1)
            org.add(p2)
            grid[p1] = grid[p2]
        for p in org - dest:
            grid[p] = "."
        sy += dy
    return sum(x + y * 100 for (x, y), c in grid.items() if c == "[")


def parse(input_data: str) -> tuple[Grid, Moves]:
    grid: Grid = {}
    moves: Moves = ""
    moves_line = False
    for y, line in enumerate(input_data.splitlines()):
        if line == "":
            moves_line = True
            continue
        if moves_line:
            moves += line
            continue
        for x, c in enumerate(line):
            grid[(x, y)] = c
    return grid, moves


def main(input_data: str):
    grid, moves = parse(input_data)
    print("P1: ", part1(grid, moves))
    print("P2: ", part2(grid, moves))


if __name__ == "__main__":
    from pathlib import Path

    main(open(Path(__file__).parent / "input").read().strip())

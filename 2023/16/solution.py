#!/usr/bin/env python3


def energize(sray, grid:dict[tuple[int,int],str]) -> int:
    rays: list[tuple[int,int,int,int]] = [sray]
    hrays: set[tuple[int,int,int,int]] = set()
    energized: set[tuple[int,int]] = set()
    maxx = max(x for x, _ in grid)
    maxy = max(y for _, y in grid)

    while rays:
        ray = rays.pop()
        if ray in hrays:
            continue
        hrays.add(ray)
        x,y,dx,dy = ray
        x = x + dx
        y = y + dy
        if not(0 <= x  <= maxx and 0 <= y  <= maxy):
            continue
        energized.add((x,y))
        g = grid.get((x,y), '.')
        if g == ".":
            rays.append((x, y, dx, dy))
        elif g == "-":
            if dy == 0:
                rays.append((x, y, dx, dy))
            else:
                rays.append((x, y, 1, 0))
                rays.append((x, y, -1, 0))
        elif g == "|":
            if dx == 0:
                rays.append((x, y, dx, dy))
            else:
                rays.append((x, y, 0, 1))
                rays.append((x, y, 0, -1))
        elif g == "/":
            rays.append((x, y, -dy, -dx))
        elif g  == "\\":
            rays.append((x, y, dy, dx))

    return len(energized)

def part1(grid:dict[tuple[int,int],str]) -> int:
    return energize((-1, 0, 1, 0), grid)

def part2(grid:dict[tuple[int,int],str]) -> int:
    max_energized = 0
    maxx = max(x for x, _ in grid)
    maxy = max(y for _, y in grid)
    max_energized = max(max_energized, *[energize((x, -1, 0, 1), grid) for x in range(maxx+1)])
    max_energized = max(max_energized, *[energize((x, maxy+1, 0, -1), grid) for x in range(maxx+1)])
    max_energized = max(max_energized, *[energize((-1, y, 1, 0), grid) for y in range(maxy+1)])
    max_energized = max(max_energized, *[energize((maxx+1, y, -1, 0), grid) for y in range(maxy+1)])
    return max_energized


def parse(input_data: str) -> dict[tuple[int,int],str]:
    grid = {}
    for y, line in enumerate(input_data.splitlines()):
        for x, c in enumerate(line):
            if c == ".":
                continue
            grid[(x, y)] = c
    return grid


def main(input_data: str):
    nodes = parse(input_data)
    return part1(nodes), part2(nodes)


if __name__ == "__main__":
    from libs.run import run

    run(main)

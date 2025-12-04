#!/usr/bin/env python3
#    --- Day 4: Printing Department ---
#   https://adventofcode.com/2025/day/4


def get_neighbors(x: int, y: int) -> list[tuple[int, int]]:
    return [
        (x - 1, y - 1),
        (x, y - 1),
        (x + 1, y - 1),
        (x - 1, y),
        (x + 1, y),
        (x - 1, y + 1),
        (x, y + 1),
        (x + 1, y + 1),
    ]


def get_num_rolls(pos: tuple[int, int], grid: dict[tuple[int, int], int]) -> int:
    count = 0
    for npos in get_neighbors(pos[0], pos[1]):
        if npos in grid:
            count += grid[npos]
    return count


def part1(data: dict[tuple[int, int], int]) -> int:
    s: int = 0
    for roll in data:
        if get_num_rolls(roll, data) < 4:
            s += 1
    return s


def remove_from_grid(grid: dict[tuple[int, int], int]) -> int:
    to_remove = []
    for pos in grid:
        if get_num_rolls(pos, grid) < 4:
            to_remove.append(pos)
    for pos in to_remove:
        del grid[pos]
    return len(to_remove)


def part2(data: dict[tuple[int, int], int]) -> int:
    s: int = 0
    grid = data.copy()
    while removed := remove_from_grid(grid):
        s += removed
    return s


def parse(input_data: str) -> dict[tuple[int, int], int]:
    grid = {}
    for y, line in enumerate(input_data.splitlines()):
        for x, ch in enumerate(line.strip()):
            if ch == "@":
                grid[(x, y)] = 1

    return grid


def main(input_data: str):
    data = parse(input_data)
    return part1(data), part2(data)


def test_solution():
    example_input = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""
    assert main(example_input) == (13, 43), "Invalid solution for the example input"


if __name__ == "__main__":
    from pathlib import Path

    r1, r2 = main(open(Path(__file__).parent / "input").read().strip())
    print(f"P1: {r1}  P2: {r2}")

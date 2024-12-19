#!/usr/bin/env python3
#       --- Day 19: Linen Layout ---
#   https://adventofcode.com/2024/day/19

from functools import cache


@cache
def get_parts(display: str, towels: tuple[str]) -> int:
    if display == "":
        return 1

    parts = 0
    for towel in towels:
        if display.startswith(towel):
            # we could use removeprefix, however we already know that display starts with towel
            parts += get_parts(display[len(towel) :], towels)
    return parts


def part1(towels: tuple[str], displays: list[str]) -> int:
    possible_displays = 0
    for display in displays:
        if get_parts(display, towels):
            possible_displays += 1

    return possible_displays


def part2(towels: tuple[str], displays: list[str]) -> int:
    return sum(get_parts(display, towels) for display in displays)


def parse(input_data: str) -> tuple[tuple[str], list[str]]:
    displays = []
    display_line = False
    for line in input_data.splitlines():
        if line == "":
            display_line = True
            continue
        if display_line:
            displays.append(line)
            continue
        towels = tuple(line.split(", "))
    return towels, displays


def main(input_data: str):
    towels, displays = parse(input_data)
    print("P1: ", part1(towels, displays))
    print("P2: ", part2(towels, displays))


if __name__ == "__main__":
    from pathlib import Path

    main(open(Path(__file__).parent / "input").read().strip())

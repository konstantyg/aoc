#!/usr/bin/env python3
#     --- Day 2: Red-Nosed Reports ---
#   https://adventofcode.com/2024/day/2


InputType = list[list[int]]


def is_safe(level: list[int]) -> bool:
    # diffs = {level[i + 1] - level[i] for i in range(len(level) - 1)}
    # return diffs <= {1, 2, 3} or diffs <= {-1, -2, -3}
    diffs = [a - b for a, b in zip(level, level[1:])]
    if any(d == 0 or abs(d) > 3 for d in diffs):
        return False
    has_inc = any(d > 0 for d in diffs)
    has_dec = any(d < 0 for d in diffs)
    if has_inc and has_dec:
        return False
    return True


def part1(data: InputType):
    # return sum(is_safe(level) for level in data)
    return len([1 for level in data if is_safe(level)])


def part2(data: InputType):
    safe = 0
    for level in data:
        if is_safe(level):
            safe += 1
            continue
        for i in range(len(level)):
            tolerated = level[:i] + level[i + 1 :]
            if is_safe(tolerated):
                safe += 1
                break
    return safe


def parse(input_data: str) -> InputType:
    levels = []
    for line in input_data.splitlines():
        levels.append(list(map(int, line.split())))
    return levels


def main(input_data: str):
    data = parse(input_data)
    print("P1: ", part1(data))
    print("P2: ", part2(data))


if __name__ == "__main__":
    main(open("input").read().strip())

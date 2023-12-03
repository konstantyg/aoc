#!/usr/bin/env python3

import re


def part1(data: list[int]):
    return sum(data)


replacements = {
    v: str(i)
    for i, v in enumerate(
        ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"], 1
    )
}


def parse(input_data: str):
    for line in input_data.splitlines():
        # for part 1 comment for loop
        for key, value in replacements.items():
            line = line.replace(key, key + value + key)
        digits = re.findall(r"(\d)", line)
        yield int(digits[0] + digits[-1])


def main(input_data: str):
    data = parse(input_data)
    return part1(data)


if __name__ == "__main__":
    from libs.run import run

    run(main)

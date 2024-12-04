#!/usr/bin/env python3
#   --- Day 4: Ceres Search ---
#   https://adventofcode.com/2024/day/4


InputType = list[str]


def look(line: str):
    return line.count("XMAS") + line.count("SAMX")


def part1(data: InputType):
    occurences = 0
    data_transposed = ["".join(y for y in x) for x in list(zip(*data))]

    row_len = len(data[0])
    col_len = len(data)

    data_diagonal = []
    for x in range(row_len):
        xrow = []
        yrow = []
        data_diagonal.append(xrow)
        data_diagonal.append(yrow)
        for y in range(x + 1):
            xrow.append(data[y][x - y])
            yrow.append(data[y][::-1][x - y])
    for y in range(1, col_len):
        xrow = []
        yrow = []
        data_diagonal.append(xrow)
        data_diagonal.append(yrow)
        d = 0
        for x in range(row_len - 1, -1, -1):
            if y + d >= col_len:
                break
            xrow.append(data[y + d][x])
            yrow.append(data[y + d][::-1][x])
            d += 1

    data_diagonal = ["".join(y for y in x) for x in data_diagonal]

    for line in data + data_transposed + data_diagonal:
        occurences += look(line)

    return occurences


def part2(data: InputType):
    occurences = 0
    patterns = [
        ["M S", " A ", "M S"],
        ["S M", " A ", "S M"],
        ["S S", " A ", "M M"],
        ["M M", " A ", "S S"],
    ]
    for pattern in patterns:
        for x in range(len(data[0]) - 2):
            for y in range(len(data) - 2):
                if all(
                    (data[y + y1][x + x1] == pattern[y1][x1] or pattern[y1][x1] == " ")
                    for y1 in range(3)
                    for x1 in range(3)
                ):
                    occurences += 1
    return occurences


def parse(input_data: str) -> InputType:
    return input_data.splitlines()


def main(input_data: str):
    data = parse(input_data)
    print("P1: ", part1(data))
    print("P2: ", part2(data))


if __name__ == "__main__":
    from pathlib import Path

    main(open(Path(__file__).parent / "input").read().strip())

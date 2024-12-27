#!/usr/bin/env python3
#   --- Day 4: Ceres Search ---
#   https://adventofcode.com/2024/day/4


# https://topaz.github.io/paste/#XQAAAQC1AQAAAAAAAAAzHIoib6pXbueH4X9F244lVRDcOZab5q1+VXY/ex42qR7D+RY2zqCmUJxVoKVyAHrhxL3iVxc+ucLBta1y80osoNaIjSvE+M0PFZytENTstYGzIkwLBXwXDfldXa+2yiyJhJADhvATKGKuUjdZSFt82HaizQ2WwdQXkxiCD7SaGCFK9d+8NXh4s3ZgMmNTzfQJoZVxMEI2xdgTjltrI7wIe8TNZ5Y6Ck+nJyH9tQhH4G6scSUZxaocXfhVILz9EU4mdlqIPu68rl3wXYDWIxvwrsFACSvuJX/PX6D7tjZHamCZmWv/tyGHAA==
from collections import defaultdict

G = defaultdict(str) | {(i,j):c for i,r in enumerate(open(0))
                                 for j,c in enumerate(r)}
# g = list(G.keys())
# D = -1,0,1

# T = list('XMAS'),
# print(sum([G[i+di*n, j+dj*n] for n in range(4)] in T
#                 for di in D for dj in D for i,j in g))

# T = list('MAS'), list('SAM')
# print(sum([G[i+d, j+d] for d in D] in T
#       and [G[i+d, j-d] for d in D] in T for i,j in g))

InputType = list[str]


def look(line: str):
    return line.count("XMAS") + line.count("SAMX")


def part1(data: InputType):
    occurences = 0
    data_transposed = ["".join(x) for x in zip(*data)]

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

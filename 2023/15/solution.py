#!/usr/bin/env python3

from collections import defaultdict


def fhash(data: str) -> int:
    h = 0
    for c in map(ord, data):
        h = ((h + c) * 17) % 256
    return h


def part1(data: list[str]) -> int:
    return sum(fhash(x) for x in data)


def part2(data: list[str]) -> int:
    boxes = defaultdict(dict)
    for i in data:
        if i.endswith("-"):
            label = i[:-1]
            boxes[fhash(label)].pop(label, None)
            continue
        label, s = i.split("=")
        boxes[fhash(label)][label] = int(s)
    res = 0
    for k, v in boxes.items():
        for i, b in enumerate(v, 1):
            res += (k + 1) * i * v[b]
    return res


def parse(input_data: str) -> list[str]:
    return [x for x in input_data.replace("\n", "").split(",")]


def main(input_data: str):
    data = parse(input_data)
    return part1(data), part2(data)


if __name__ == "__main__":
    from libs.run import run

    run(main)

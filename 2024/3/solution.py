#!/usr/bin/env python3
#       --- Day 3: Mull It Over ---
#   https://adventofcode.com/2024/day/3


from dataclasses import dataclass


@dataclass
class Operation:
    a: int = 0
    b: int = 0
    instruction: bool | None = None


InputType = list[Operation]


def part1(data: InputType):
    return sum(op.a * op.b for op in data if op.instruction is None)


def part2(data: InputType):
    result = 0
    enabled = True
    for op in data:
        if op.instruction is None and enabled:
            result += op.a * op.b
        elif op.instruction is not None:
            enabled = op.instruction
    return result


def parse(input_data: str) -> InputType:
    import re

    re_mul = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|(don't\(\))|(do\(\))")
    muls = []
    for m in re_mul.findall(input_data):
        if m[2]:
            muls.append(Operation(instruction=False))
        elif m[3]:
            muls.append(Operation(instruction=True))
        else:
            muls.append(Operation(int(m[0]), int(m[1])))
    return muls


def main(input_data: str):
    data = parse(input_data)
    print("P1: ", part1(data))
    print("P2: ", part2(data))


if __name__ == "__main__":
    from pathlib import Path

    main(open(Path(__file__).parent / "input").read().strip())

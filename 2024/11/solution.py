#!/usr/bin/env python3
#    --- Day 11: Plutonian Pebbles ---                        
#   https://adventofcode.com/2024/day/11  

from functools import cache, partial


InputType = list[int]


@cache
def blink(x: int, to_blink: int = 25):
    if to_blink == 0:
        return 1

    to_blink -= 1

    if x == 0:
        return blink(1, to_blink)

    sx = str(x)
    l = len(sx)
    if l % 2:
        return blink(x * 2024, to_blink)

    l = l // 2
    lx, rx = int(sx[:l]), int(sx[l:])

    return blink(lx, to_blink) + blink(rx, to_blink)


def do_blinking(data: InputType, reps: int = 25) -> int:
    blink_func = partial(blink, to_blink=reps)
    return sum(map(blink_func, data))


def parse(input_data: str) -> InputType:
    data = []
    for line in input_data.splitlines():
        data += list(map(int, line.split()))
    return data


def main(input_data: str):
    data = parse(input_data)
    print("P1: ", do_blinking(data))
    print("P2: ", do_blinking(data, 75))


if __name__ == "__main__":
    from pathlib import Path

    main(open(Path(__file__).parent / "input").read().strip())

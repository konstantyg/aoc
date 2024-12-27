#!/usr/bin/env python3
#      --- Day 9: Disk Fragmenter ---
#   https://adventofcode.com/2024/day/9

try:
    from typing import Self
except ImportError:
    from typing import TypeVar

    Self = TypeVar("Self", bound="Block")

InputType = list[int]


def part1(data: InputType):
    blocks = []
    eid = 0
    is_block = True
    for x in data:
        if is_block:
            blocks += [eid] * x
            eid += 1
        else:
            blocks += [None] * x
        is_block = not is_block
    rev = enumerate(blocks[::-1])
    blocks_len = len(blocks) - 1
    ii = 0
    s = []
    for i, x in enumerate(blocks):
        if blocks_len - ii - i == 0:
            break
        if x is None:
            ii, xx = next(rev)
            while xx is None:
                ii, xx = next(rev)
            s.append(xx)
        else:
            s.append(x)

    return sum(i * x for i, x in enumerate(s))


class Block:
    __slots__ = (
        "eid",
        "length",
        "next",
        "prev",
    )

    def __init__(
        self,
        eid: int | None,
        length: int,
        prev: Self | None = None,
        next: Self | None = None,
    ):
        self.eid = eid
        self.length = length
        self.prev = prev
        if prev:
            prev.next = self
        self.next = next
        if next:
            next.prev = self

    def __str__(self):
        return f"{self.eid if self.eid is not None else '.'}" * self.length

    def __repr__(self):
        return f"Block({self.eid}, {self.length})"


def print_blocks(b):
    while b:
        print(b, end="")
        b = b.next
    print()


def part2(data: InputType):
    # prepare linked list of blocks
    first = Block(0, data[0])
    eid = 1
    last = first
    is_block = False
    for x in data[1:]:
        if is_block:
            last = Block(eid, x, last)
            eid += 1
        elif x:
            # skip empty blocks of length 0
            last = Block(None, x, last)
        is_block = not is_block

    # reorganize blocks
    b = last
    while b != first:
        f = first
        while f and b and f != b:
            if f.eid is not None:
                if f.next is None:
                    break
                f = f.next
                continue
            if f.length >= b.length:
                f.eid = b.eid
                b.eid = None
                if gap := f.length - b.length:
                    f.length = b.length
                    Block(None, gap, f, f.next)
                # we don't need to merge empty blocks after current one
                break
            f = f.next
        b = b.prev
        if b.eid is None:
            b = b.prev
    s: list[int] = []
    while first:
        s = s + [first.eid or 0] * first.length
        first = first.next

    return sum(i * x for i, x in enumerate(s))


def parse(input_data: str) -> InputType:
    data = []
    for line in input_data.splitlines():
        data += list(map(int, line))
    return data


def main(input_data: str):
    data = parse(input_data)
    print("P1: ", part1(data))
    print("P2: ", part2(data))


if __name__ == "__main__":
    from pathlib import Path

    main(open(Path(__file__).parent / "input").read().strip())

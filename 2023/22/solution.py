#!/usr/bin/env python3

from dataclasses import dataclass, field
from functools import cached_property
from typing import TypeAlias

from libs.profiler import profiler

Point: TypeAlias = tuple[int, int]


@dataclass
class Brick:
    i: int
    x1: int
    y1: int
    z1: int
    x2: int
    y2: int
    z2: int
    supported_by: set["Brick"] = field(default_factory=set)
    supports: set["Brick"] = field(default_factory=set)

    def __hash__(self) -> int:
        return self.i

    def __eq__(self, other: "Brick") -> bool:
        return (
            self.x1 == other.x1
            and self.y1 == other.y1
            and self.z1 == other.z1
            and self.x2 == other.x2
            and self.y2 == other.y2
            and self.z2 == other.z2
        )

    def __repr__(self) -> str:
        return f"Brick {self.i}"

    def __lt__(self, other: "Brick") -> bool:
        return self.z1 < other.z1

    @cached_property
    def r(self):
        return set(
            (x, y)
            for x in range(self.x1, self.x2 + 1)
            for y in range(self.y1, self.y2 + 1)
        )

    def insert(self, stack: dict[int, dict[Point, "Brick"]]):
        for z in range(self.z1, self.z2 + 1):
            if z not in stack:
                stack[z] = {}
            for p in self.r:
                stack[z][p] = self

    def copy(self, stack: dict[int, dict[Point, "Brick"]] | None = None):
        b = Brick(self.i, self.x1, self.y1, self.z1, self.x2, self.y2, self.z2)
        if stack is not None:
            b.insert(stack)
        return b

    def move(self, stack: dict[int, dict[Point, "Brick"]]) -> bool:
        if self.z1 == 1:
            return False
        can_move = True
        for z in range(self.z1 - 1, self.z2):
            if not can_move:
                break
            if z not in stack:
                stack[z] = {}
            for p, b in stack[z].items():
                if p in self.r and b is not self:
                    can_move = False
                    break
        if can_move:
            self.z1 -= 1
            for p in self.r:
                stack[self.z1][p] = self
                stack[self.z2].pop(p, None)
            self.z2 -= 1
        return can_move

    def update_supports(self, stack: dict[int, dict[Point, "Brick"]]) -> None:
        for z in range(self.z1, self.z2 + 1):
            if z + 1 not in stack:
                continue
            for p in self.r:
                if p not in stack[z + 1]:
                    continue
                above = stack[z + 1][p]
                if above is self:
                    continue
                above.supported_by.add(self)
                self.supports.add(above)


@profiler
def part1(bricks: list[Brick]) -> int:
    # 0.4 msec to complete
    safe_to_remove = []
    for brick in bricks:
        safe = True
        for above in brick.supports:
            if len(above.supported_by) == 1:
                safe = False
        if safe:
            safe_to_remove.append(brick)
    return len(safe_to_remove)


@profiler
def part1_sim(bricks: list[Brick]) -> int:
    # 13s to complete
    safe_to_remove = 0
    for brick in bricks:
        stack: dict[int, dict[Point, Brick]] = {}
        bs = [b.copy(stack) for b in bricks if b is not brick]
        moved = False
        for b in bs:
            moved |= b.move(stack)
        if not moved:
            safe_to_remove += 1
    return safe_to_remove


def count_fallen(bricks: set[Brick]) -> int:
    unsupported = set()
    for brick in bricks:
        unsupported |= {
            above
            for above in brick.supports - bricks
            if len(above.supported_by - bricks) == 0
        }
    if not unsupported:
        return 0
    return len(unsupported) + count_fallen(bricks | unsupported)


@profiler
def part2(bricks: list[Brick]) -> int:
    # 1,5s to complete
    fallen = 0
    for brick in bricks:
        f = count_fallen({brick})
        fallen += f
    return fallen


@profiler
def part2_sim(bricks: list[Brick]) -> int:
    # 25s to complete
    moved_after_remove = 0
    for brick in bricks:
        stack: dict[int, dict[Point, Brick]] = {}
        bs = [b.copy(stack) for b in bricks if b is not brick]
        orig = [b.copy() for b in bs]
        moved = True
        while moved:
            moved = False
            for b in bs:
                moved |= b.move(stack)
        for a, b in zip(bs, orig):
            if a != b:
                moved_after_remove += 1
    return moved_after_remove


@profiler
def parse(input_data: str) -> list[Brick]:
    # 0,8s to complete
    bricks = []
    i = 1
    for line in input_data.splitlines():
        s, e = line.split("~")
        x1, y1, z1 = map(int, s.split(","))
        x2, y2, z2 = map(int, e.split(","))
        # assert all expand in one direction only
        assert (
            (x1 != x2 and y1 == y2 and z1 == z2)
            or (x1 == x2 and y1 != y2 and z1 == z2)
            or (x1 == x2 and y1 == y2 and z1 != z2)
            or (x1 == x2 and y1 == y2 and z1 == z2)
        )
        # and first coordinates is smaller or equal than second
        assert x1 <= x2 and y1 <= y2 and z1 <= z2
        bricks.append(Brick(i, x1, y1, z1, x2, y2, z2))
        i += 1
    stack: dict[int, dict[Point, Brick]] = {}
    for brick in sorted(bricks):
        brick.insert(stack)
    moved = True
    while moved:
        moved = False
        for brick in sorted(bricks):
            moved |= brick.move(stack)

    for brick in bricks:
        brick.update_supports(stack)
    return sorted(bricks)


def main(input_data: str):
    bricks = parse(input_data)
    # return part1_sim(bricks), part2_sim(bricks)
    return part1(bricks), part2(bricks)


if __name__ == "__main__":
    from libs.run import run

    run(main)

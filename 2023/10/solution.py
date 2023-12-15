#!/usr/bin/env python3

from itertools import pairwise
from operator import attrgetter


class E:
    connections_map = {"F": 6, "|": 5, "-": 10, "L": 3, "J": 9, "7": 12, "S": 15}
    pp_map = {
        "F": "╭",
        "|": "│",
        "-": "─",
        "L": "╰",
        "J": "╯",
        "7": "╮",
    }

    def __init__(self, c: str, x: int, y: int):
        #    1
        #  8 x 2
        #    4
        #
        # L = 3
        # | = 5
        # etc.
        self.c = c
        self.pos = (x, y)
        self.v = self.connections_map.get(c, 0)
        self.in_loop = False
        self.inside_loop = False
        self.dist = 0
        self.start = False

    @property
    def rich(self):
        if self.start:
            return f"[bright_cyan bold]*[/bright_cyan bold]"
        if self.in_loop:
            return f"{self.pp_map[self.c]}"
        if self.inside_loop:
            return f"[yellow bold]•[/yellow bold]"
        return f"[gray50 dim]•[/gray50 dim]"

    def get_connected(self, data: list[list["E"]]):
        x, y = self.pos
        n = data[y + 1][x]
        if self.v & 4 and n.v & 1:
            yield n
        n = data[y - 1][x]
        if self.v & 1 and n.v & 4:
            yield n
        n = data[y][x + 1]
        if self.v & 2 and n.v & 8:
            yield n
        n = data[y][x - 1]
        if self.v & 8 and n.v & 2:
            yield n

    def __repr__(self):
        return f"{self.c} {self.pos} {self.v}"

    def __str__(self):
        return f"{self.c} {self.pos} {self.v}"

    def __eq__(self, other) -> bool:
        if other is None:
            return False
        return self.pos == other.pos

    def __hash__(self) -> int:
        return hash(self.pos)


def get_start(data: list[list[E]]):
    for line in data:
        for c in line:
            if c.c == "S":
                return c
    raise (ValueError("No start found"))


def update_loop(data: list[list[E]]):
    start = get_start(data)
    start.in_loop = True
    start.start = True
    connections_from_start = list(start.get_connected(data))
    # update start connections types


    # only go one direction to get sorted nodes in loop (by dist)
    # needed to calculate area of loop
    first_connected = connections_from_start[0]
    first_connected.in_loop = True
    q: list[E] = [first_connected]
    dist = 0
    while q:
        dist += 1
        pos = q.pop(0)
        pos.dist = dist
        for c in pos.get_connected(data):
            if c.in_loop:
                continue
            c.in_loop = True
            q.append(c)


def print_map(data: list[list[E]]):
    from rich.console import Console

    console = Console(width=len(data[0]), record=True)
    for line in data:
        console.print(*[c.rich for c in line], sep="")
    console.save_svg("maze.svg", title="Maze")


def part1(data: list[list[E]]) -> int:
    loop_len = sum(1 for line in data for x in line if x.in_loop)
    return loop_len // 2


def part2(data: list[list[E]]) -> int:
    # Jordan theorem:
    # Point is inside the polygon if and only if
    # number of intersections of the ray with edges of polygon is odd
    # this gives us information which points are inside the loop
    inside_loop = 0
    for line in data:
        left = 0
        # every row from left to right
        for c in line:
            if not c.in_loop and left % 2 == 1:
                inside_loop += 1
                c.inside_loop = True
            if c.c in ["|", "L", "J"] and c.in_loop:  # works too ['|', '7', 'F']
                left += 1

    # Second method
    # Shoelace formula - to get area of trapezoid
    points = [c for line in data for c in line if c.in_loop]
    points.sort(key=attrgetter("dist"))
    area = 0
    for p1, p2 in pairwise(points + [points[0]]):
        area += p1.pos[0] * p2.pos[1] - p2.pos[0] * p1.pos[1]
    # need abs because of direction of points could be positive or negative
    area = abs(area) // 2

    # Pick's theorem
    # A = I + B/2 - 1
    interior_points = area - (len(points) // 2) + 1
    assert interior_points == inside_loop

    # print_map(data)

    return inside_loop


def parse(input_data: str):
    lines = input_data.splitlines()
    lines_with_edge = ["." + line + "." for line in lines]
    lines_with_edge.insert(0, "." * (len(lines[0]) + 2))
    lines_with_edge.append("." * (len(lines[0]) + 2))
    data = [
        [E(c, x, y) for x, c in enumerate(line)]
        for y, line in enumerate(lines_with_edge)
    ]
    update_loop(data)
    return data


def main(input_data: str):
    data = parse(input_data)
    return part1(data), part2(data)


if __name__ == "__main__":
    from libs.run import run

    run(main)

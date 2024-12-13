#!/usr/bin/env python3
#     --- Day 13: Claw Contraption ---
#   https://adventofcode.com/2024/day/13


from dataclasses import dataclass


@dataclass(slots=True)
class Button:
    incx: int = 0
    incy: int = 0


@dataclass(slots=True)
class Prize:
    x: int = 0
    y: int = 0


@dataclass(slots=True)
class Machine:
    a: Button
    b: Button
    p: Prize

    def best(self, max_steps=None):
        a = self.a
        aincx, aincy = a.incx, a.incy
        b = self.b
        bincx, bincy = b.incx, b.incy
        p = self.p
        px, py = p.x, p.y
        if max_steps is None:
            # part 2
            px += 10000000000000
            py += 10000000000000

        pb = (aincx * py - aincy * px) / (aincx * bincy - aincy * bincx)
        if int(pb) != pb:
            return 0
        pa = (px - bincx * pb) / aincx
        if int(pa) != pa:
            return 0
        return int(pa * 3 + pb)

        # part 1 brute force
        # cost = 0
        # for pa in range(max_steps+1):
        #     for pb in range(max_steps+1):
        #         if aincx * pa + bincx * pb != px:
        #             continue
        #         if aincy * pa + bincy * pb != py:
        #             continue
        #         c = pa * 3 + pb
        #         if cost == 0 or c < cost:
        #             cost = c


def part1(machines: list[Machine]) -> int:
    return sum(m.best(100) for m in machines)


def part2(machines: list[Machine]) -> int:
    return sum(m.best() for m in machines)


def parse(input_data: str) -> list[Machine]:
    machines = []
    a = None
    b = None
    for line in input_data.splitlines():
        if line == "":
            a = None
            b = None
            continue
        if line[0] == "B":
            _, bx, px, py = line.split(" ")
            if bx[0] == "A":
                a = Button(int(px[2:-1]), int(py[2:]))
            if bx[0] == "B":
                b = Button(int(px[2:-1]), int(py[2:]))
            continue
        if line[0] == "P":
            _, px, py = line.split(" ")
            p = Prize(int(px.split("=")[1][:-1]), int(py.split("=")[1]))
            assert a is not None and b is not None
            machines.append(Machine(a, b, p))
    return machines


def main(input_data: str):
    machines = parse(input_data)
    print("P1: ", part1(machines))
    print("P2: ", part2(machines))


if __name__ == "__main__":
    from pathlib import Path

    main("""Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
""")
    main(open(Path(__file__).parent / "input").read().strip())

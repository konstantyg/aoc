#!/usr/bin/env python3

from dataclasses import dataclass
from typing import TypeAlias
import math

Inst: TypeAlias = tuple[str, int]
Point: TypeAlias = tuple[int, int]


@dataclass
class Part:
    x: int
    m: int
    a: int
    s: int

    @property
    def v(self):
        return self.x + self.m + self.a + self.s


def part1(workflows, parts) -> int:
    accepted = []
    for part in parts:
        w = "in"
        while w not in ["A", "R"]:
            rules, f = workflows[w]
            for c, t, v, r in rules:
                if t == "<" and getattr(part, c) < v:
                    w = r
                    break
                elif t == ">" and getattr(part, c) > v:
                    w = r
                    break
            else:
                w = f
        if w == "A":
            accepted.append(part)
    return sum(p.v for p in accepted)


def process(workflows, w, ranges):
    if w == "A":
        assert all(a <= b for a, b in ranges.values())
        return math.prod(b - a + 1 for a, b in ranges.values())
    elif w == "R":
        return 0
    rules, final = workflows[w]
    curr = 0
    for c, t, v, r in rules:
        lo, hi = ranges[c]
        p2 = dict(ranges)
        if t == ">":
            p2[c] = (max(lo, v + 1), hi)
            curr += process(workflows, r, p2)
            ranges[c] = (lo, min(hi, v))
        else:
            p2[c] = (lo, min(hi, v - 1))
            curr += process(workflows, r, p2)
            ranges[c] = (max(lo, v), hi)
    curr += process(workflows, final, ranges)

    return curr


def part2(workflows, parts) -> int:
    return process(workflows, "in", {k: (1, 4000) for k in "xmas"})


def parse_workflow(input: str):
    w, d = input[:-1].split("{")
    *d, f = d.split(",")
    rules = []
    for x in d:
        c, r = x.split(":")
        c, t, v = c[0], c[1], c[2:]
        v = int(v)
        rules.append((c, t, v, r))
    return w, rules, f


def parse_part(input: str):
    return eval("Part(" + input[1:-1] + ")")


def parse(input_data: str):
    workflows = {}
    parts = []
    mode = 0
    for line in input_data.splitlines():
        if line == "":
            mode = 1
            continue
        if mode == 0:
            w, r, f = parse_workflow(line)
            workflows[w] = (r, f)
        else:
            parts.append(parse_part(line))
    return workflows, parts


def main(input_data: str):
    workflows, parts = parse(input_data)
    return part1(workflows, parts), part2(workflows, parts)


if __name__ == "__main__":
    from libs.run import run

    run(main)

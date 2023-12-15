#!/usr/bin/env python3

import re
from itertools import cycle
from math import lcm


def part1(nav, nodes) -> int:
    instructions = cycle(nav)
    steps = 0
    node = "AAA"
    for i in instructions:
        steps += 1
        node = nodes[node][i]
        if node == "ZZZ":
            break
    return steps


def part2(nav, nodes) -> int:
    instructions = cycle(nav)

    node_list = [(n, 0) for n in nodes if n[2] == "A"]
    cycles = []
    for i in instructions:
        if len(node_list) == 0:
            break
        new_node_list = []
        for n, c in node_list:
            n = nodes[n][i]
            c += 1
            if n[2] == "Z":
                cycles.append(c)
                continue
            new_node_list.append((n, c))
        node_list = new_node_list
    return lcm(*cycles)


def parse(input_data: str) -> tuple[list[int], dict[str, tuple[str, str]]]:
    data = input_data.splitlines()
    nav = [1 if s == "R" else 0 for s in data[0]]
    nodes = {}
    node_def = re.compile(r"([A-Z0-9]{3}) = \(([A-Z0-9]{3}), ([A-Z0-9]{3})\)")
    for line in data[2:]:
        m = node_def.match(line)
        if m:
            nodes[m.group(1)] = (m.group(2), m.group(3))

    return nav, nodes


def main(input_data: str):
    nav, nodes = parse(input_data)
    return part1(nav, nodes), part2(nav, nodes)


if __name__ == "__main__":
    from libs.run import run

    run(main)

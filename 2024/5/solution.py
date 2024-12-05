#!/usr/bin/env python3
#        --- Day 5: Print Queue ---
#   https://adventofcode.com/2024/day/5


from dataclasses import dataclass
from collections import defaultdict


from functools import cmp_to_key


def part1(rules, updates):
    s = 0

    def rsort(x, y):
        if y in rules.get(x):
            return -1
        return 0

    for update in updates:
        if update != sorted(update, key=cmp_to_key(rsort)):
            continue
        s += update[len(update) // 2]

    return s


def part2(rules, updates):
    s = 0

    def rsort(x, y):
        if y in rules.get(x):
            return -1
        return 0

    for update in updates:
        if (sorted_update := sorted(update, key=cmp_to_key(rsort))) != update:
            s += sorted_update[len(update) // 2]
    return s


def parse(input_data: str):
    rules = defaultdict(set)
    updates = list()
    rules_sections = True
    for line in input_data.splitlines():
        if line == "":
            rules_sections = False
            continue
        if rules_sections:
            x, y = map(int, line.split("|"))
            rules[x].add(y)
            continue
        updates.append(list(map(int, line.split(","))))
    return rules, updates


def main(input_data: str):
    rules, updates = parse(input_data)
    print("P1: ", part1(rules, updates))
    print("P2: ", part2(rules, updates))


if __name__ == "__main__":
    from pathlib import Path

    main(open(Path(__file__).parent / "input").read().strip())

#!/usr/bin/env python3

from dataclasses import dataclass


@dataclass
class RGB:
    b: int = 0
    r: int = 0
    g: int = 0

    def from_str(self, s: str):
        for e in s.split(","):
            match e.split():
                case [n, "red"]:
                    self.r += int(n)
                case [n, "green"]:
                    self.g += int(n)
                case [n, "blue"]:
                    self.b += int(n)


def part1(data: dict[int, list[RGB]]):
    s = 0
    max_r = 12
    max_g = 13
    max_b = 14
    for game, bags in data.items():
        for bag in bags:
            if bag.r > max_r or bag.g > max_g or bag.b > max_b:
                break
        else:
            s += game
    return s


def part2(data: dict[int, list[RGB]]):
    s = 0
    for game, bags in data.items():
        max_r = 0
        max_g = 0
        max_b = 0
        for bag in bags:
            max_r = max(max_r, bag.r)
            max_g = max(max_g, bag.g)
            max_b = max(max_b, bag.b)
        s += max_r * max_g * max_b
    return s


def parse(input_data: str):
    data: dict[int, list[RGB]] = {}
    for line in input_data.splitlines():
        g, d = line.split(":")
        game = int(g[4:])
        bags = []
        for bagdata in d.split(";"):
            bag = RGB()
            bag.from_str(bagdata)
            bags.append(bag)
        data[game] = bags
    return data


def main(input_data: str):
    data = parse(input_data)
    return part1(data), part2(data)


if __name__ == "__main__":
    from libs.run import run

    run(main)

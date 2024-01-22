#!/usr/bin/env python3

from dataclasses import dataclass
from libs.utils import pairs


@dataclass
class R:
    dest: int
    source: int
    length: int


def part1(seeds: list[int], sections: list[list[R]]) -> int:
    loc: list[int] = []
    for seed in seeds:
        for section in sections:
            for g in section:
                if g.source <= seed < g.source + g.length:
                    seed = g.dest + seed - g.source
                    break
        loc.append(seed)
    return min(loc)


def part2(seeds: list[int], sections: list[list[R]]) -> int:
    for section in sections:
        new_seeds = []
        for start_seed, seeds_len in pairs(seeds):
            while seeds_len != 0:
                dist = seeds_len
                for g in section:
                    if g.source <= start_seed < g.source + g.length:
                        remaining = min(g.length - start_seed + g.source, seeds_len)
                        new_seeds.extend([g.dest + start_seed - g.source, remaining])
                        start_seed += remaining
                        seeds_len -= remaining
                        break
                    else:
                        if start_seed < g.source:
                            dist = min(dist, g.source - start_seed)
                else:
                    # no match
                    h_len = min(dist, seeds_len)
                    new_seeds.extend([start_seed, h_len])
                    start_seed += h_len
                    seeds_len -= h_len
        seeds = new_seeds
    return min(start_seed for start_seed, _ in pairs(seeds))


def parse(input_data: str) -> tuple[list[int], list[list[R]]]:
    data = input_data.splitlines()
    seeds = list(map(int, data[0].split(": ")[1].split(" ")))
    sections: list[list[R]] = []
    section: list[R] = []
    for line in data[3:]:
        if line.endswith("map:"):
            continue
        if line == "":
            sections.append(section)
            section = []
            continue
        entry = list(map(int, line.split(" ")))
        section.append(R(*entry))
    sections.append(section)
    return seeds, sections


def main(input_data: str):
    seeds, sections = parse(input_data)
    return part1(seeds, sections), part2(seeds, sections)


if __name__ == "__main__":
    from libs.run import run

    run(main)

#!/usr/bin/env python3
#      --- Day 12: Garden Groups ---
#   https://adventofcode.com/2024/day/12


from dataclasses import dataclass, field

InputType = list[int]
Point = tuple[int, int]
Plant = str
Garden = dict[Point, Plant]

dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))


def neighbors(p: Point):
    x, y = p
    for d in dirs:
        dx, dy = d
        yield (x + dx, y + dy), d


@dataclass
class Region:
    plant: Plant
    points: set[Point] = field(default_factory=set)
    edges: set[tuple[Point, Point]] = field(default_factory=set)

    @classmethod
    def from_garden(cls, garden: Garden, p: Point):
        r = cls(garden[p])
        possible_points = set(garden.keys())
        c = r.plant
        r.points.add(p)

        def get_surrounding(region: Region) -> set[tuple[int, int]]:
            new_points = set()
            for q in region.points:
                new_points |= {p for p, _ in set(neighbors(q)) if p in possible_points and garden[p] == region.plant}
            return new_points - region.points

        while new_points := get_surrounding(r):
            r.points.update(new_points)
            possible_points -= new_points
        for p in r.points:
            for np, d in neighbors(p):
                if np not in r.points:
                    r.edges.add((p, d))
        return r

    @property
    def area(self):
        return len(self.points)

    @property
    def permimeter(self):
        return len(self.edges)

    @property
    def fences(self):
        fs = 0
        for p, d in self.edges:
            x, y = p
            dx, dy = d
            if dx == 0 and ((x + 1, y), d) not in self.edges and ((x - 1, y), d) not in self.edges:
                fs += 2
                continue
            if dy == 0 and ((x, y + 1), d) not in self.edges and ((x, y - 1), d) not in self.edges:
                fs += 2
                continue
            if dx == 0 and ((x + 1, y), d) in self.edges and ((x - 1, y), d) in self.edges:
                continue
            if dy == 0 and ((x, y + 1), d) in self.edges and ((x, y - 1), d) in self.edges:
                continue
            fs += 1
        return fs // 2

    @property
    def price(self):
        return self.area * self.permimeter

    @property
    def price_fences(self):
        return self.area * self.fences


def get_regions(data: Garden) -> list[Region]:
    points: set[Point] = set(data.keys())
    regions: list[Region] = []
    while points:
        p = points.pop()
        r = Region.from_garden(data, p)
        regions.append(r)
        points -= r.points

    return regions


def part1(regions: list[Region]) -> int:
    return sum(r.price for r in regions)


def part2(regions: list[Region]) -> int:
    return sum(r.price_fences for r in regions)


def parse(input_data: str) -> Garden:
    data: Garden = {}
    for y, line in enumerate(input_data.splitlines()):
        for x, c in enumerate(line):
            data[(x, y)] = c
    return data


def main(input_data: str):
    garden = parse(input_data)
    regions = get_regions(garden)
    print("P1: ", part1(regions))
    print("P2: ", part2(regions))


if __name__ == "__main__":
    from pathlib import Path

    main(open(Path(__file__).parent / "input").read().strip())

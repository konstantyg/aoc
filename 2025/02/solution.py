#!/usr/bin/env python3
#         --- Day 2: Gift Shop ---
#   https://adventofcode.com/2025/day/2


def part1(data: list[tuple[int, int]]) -> int:
    s: int = 0
    for x, y in data:
        for v in range(x, y + 1):
            c = str(v)
            l = len(c)
            if l % 2 == 1:
                continue
            first_half = c[: l // 2]
            second_half = c[l // 2 :]
            for z1, z2 in zip(first_half, second_half):
                if z1 != z2:
                    break
            else:
                s += v
    return s


def part2(data: list[tuple[int, int]]) -> int:
    s = 0
    for x, y in data:
        for v in range(x, y + 1):
            c = str(v)
            # if c in (c+c)[1:-1]:
            #     s+=v
            if len(set(c)) == 1 and v > 9:
                s += v
                continue
            ll = len(c)
            for d in range(2, ll // 2 + 1):
                if len(c) % d:
                    continue
                chunk = c[:d]
                for i in range(d, ll, d):
                    if c[i : i + d] != chunk:
                        break
                else:
                    s += v
                    break
    return s


def parse(input_data: str) -> list[tuple[int, int]]:
    sequence = []
    for line in input_data.splitlines():
        for r in line.split(","):
            x, y = map(int, r.split("-"))
            sequence.append((x, y))

    return sequence


def main(input_data: str):
    data = parse(input_data)
    return part1(data), part2(data)


def test_solution():
    example_input = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224
1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""
    assert main(example_input) == (1227775554, 4174379265), "Invalid solution for the example input"


if __name__ == "__main__":
    from pathlib import Path

    r1, r2 = main(open(Path(__file__).parent / "input").read().strip())
    print(f"P1: {r1}  P2: {r2}")

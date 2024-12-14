#!/usr/bin/env python3
#     --- Day 14: Restroom Redoubt ---
#   https://adventofcode.com/2024/day/14

from pathlib import Path


def part1(robots: list[tuple[int, int, int, int]]) -> int:
    mx, my = max(x for x, _, _, _ in robots), max(y for _, y, _, _ in robots)

    def calc(r):
        x, y, vx, vy = r
        x += vx
        y += vy
        if x < 0:
            x += mx + 1
        if y < 0:
            y += my + 1
        if x > mx:
            x %= mx + 1
        if y > my:
            y %= my + 1
        return (x, y, vx, vy)

    q1, q2, q3, q4 = 0, 0, 0, 0
    with open(Path(__file__).parent / "pics", "w") as f:
        for t in range(1, 10000):
            robots = [calc(r) for r in robots]
            f.write(f"Seconds: {t}\n")
            grid = [["." for _ in range(mx + 1)] for _ in range(my + 1)]
            for x, y, _, _ in robots:
                grid[y][x] = "#"
            f.writelines("".join(row) + "\n" for row in grid)
            if t == 100:
                mx1 = mx // 2
                my1 = my // 2
                for x, y, _, _ in robots:
                    if x < mx1 and y < my1:
                        q1 += 1
                    if x > mx1 and y < my1:
                        q2 += 1
                    if x < mx1 and y > my1:
                        q3 += 1
                    if x > mx1 and y > my1:
                        q4 += 1
    # for part 2 look for "########" in the output
    return q1 * q2 * q3 * q4


def parse(input_data: str) -> list[tuple[int, int, int, int]]:
    robots = []
    for line in input_data.splitlines():
        x, y, vx, vy = map(int, line[2:].replace("v=", "").replace(",", " ").split())
        robots.append((x, y, vx, vy))
    return robots


def main(input_data: str):
    robots = parse(input_data)
    print("P1: ", part1(robots))


if __name__ == "__main__":
    main(open(Path(__file__).parent / "input").read().strip())

#!/usr/bin/env python3
#      --- Day 20: Race Condition ---
#   https://adventofcode.com/2024/day/20

from collections import defaultdict


Point = tuple[int, int]


def manhattan(a: Point, b: Point) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def print_scores(scores: dict[int, int]):
    for saved in sorted(scores):
        s = scores[saved]
        if s == 1:
            n = "is one cheat that saves"
        else:
            n = f"are {s} cheats that save"
        print(f"There {n} {saved} picoseconds.")


def calc_saves(track: list[Point], cheat_len=20, min_saved=100) -> int:
    track_len = len(track)
    scores = defaultdict(int)
    for s_pos, s_cords in enumerate(track):
        for e_pos in range(s_pos + min_saved, track_len):
            distance = manhattan(s_cords, track[e_pos])
            saved = e_pos - s_pos - distance
            if saved < min_saved:
                continue
            if distance <= cheat_len:
                scores[saved] += 1

    # print_scores(scores)

    return sum(v for k, v in scores.items() if k >= min_saved)


def parse(input_data: str) -> list[Point]:
    track = []
    points = []
    for y, line in enumerate(input_data.splitlines()):
        for x, c in enumerate(line):
            if c == "S":
                start = (x, y)
            elif c == "E":
                end = (x, y)
            elif c != "#":
                points.append((x, y))
    p = start
    while p != end:
        track.append(p)
        if len(points) == 0:
            track.append(end)
            break
        x, y = p
        for np in [
            (x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x, y - 1),
        ]:
            if np in points:
                points.remove(np)
                p = np
                break
    return track


def main(input_data: str):
    track = parse(input_data)
    print("P1: ", calc_saves(track, 2))
    print("P2: ", calc_saves(track))


if __name__ == "__main__":
    from pathlib import Path

    main(open(Path(__file__).parent / "input").read().strip())

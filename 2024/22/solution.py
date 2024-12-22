#!/usr/bin/env python3
#      --- Day 22: Monkey Market ---
#   https://adventofcode.com/2024/day/22

from collections import deque, Counter


def calc(secret: int) -> int:
    secret = ((secret << 6) ^ secret) & 16777215
    secret = ((secret >> 5) ^ secret) & 16777215
    secret = ((secret << 11) ^ secret) & 16777215
    return secret


def process(secrets: list[int], generations: int = 2000) -> int:
    sum_secrets = 0
    sequences = Counter()
    for secret in secrets:
        changes = deque(maxlen=4)
        occurences = set()
        last_price = secret % 10
        for _ in range(generations):
            secret = calc(secret)
            price = secret % 10
            changes.append(price - last_price)
            last_price = price
            if len(changes) == 4 and (occurence := tuple(changes)) not in occurences:
                occurences.add(occurence)
                sequences[occurence] += price
        sum_secrets += secret
    return sum_secrets, sequences.most_common(1)[0][1]


def parse(input_data: str) -> list[int]:
    return list(map(int, input_data.splitlines()))


def main(input_data: str):
    secrets = parse(input_data)
    p1, p2 = process(secrets)
    print("P1: ", p1)
    print("P2: ", p2)


if __name__ == "__main__":
    from pathlib import Path

    main(open(Path(__file__).parent / "input").read().strip())

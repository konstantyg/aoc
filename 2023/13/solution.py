#!/usr/bin/env python3


def look(data: list[str], diff: int = 0) -> int:
    l = len(data)
    for i in range(1, l):
        if (
            sum(
                [
                    1 if x != y else 0
                    for (a, b) in zip(
                        data[max(0, i * 2 - l) : i], data[i : min(l, 2 * i)][::-1]
                    )
                    for x, y in zip(a, b)
                ]
            )
            == diff
        ):
            return i
    return 0


def part1(data) -> int:
    return sum(100 * look(p) + look(["".join(c) for c in zip(*p)]) for p in data)


def part2(data) -> int:
    return sum(100 * look(p, 1) + look(["".join(c) for c in zip(*p)], 1) for p in data)


def parse(input_data: str):
    lines = input_data.splitlines()
    data = []
    pattern = []
    for line in lines:
        if line == "":
            data.append(pattern)
            pattern = []
            continue
        pattern.append(line)
    data.append(pattern)
    return data


def main(input_data: str):
    data = parse(input_data)
    return part1(data), part2(data)


if __name__ == "__main__":
    from libs.run import run

    run(main)

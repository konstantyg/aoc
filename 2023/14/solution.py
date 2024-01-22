#!/usr/bin/env python3


def rotate(data: list[str], left=False) -> list[str]:
    if left:
        return ["".join(c) for c in zip(*data)][::-1]
    return ["".join(c) for c in zip(*data[::-1])]


def tilt(data: list[str]) -> list[str]:
    d: list[str] = []
    for line in data:
        l: list[str] = []
        co = 0
        cd = 0
        for c in line + "#":
            if c == ".":
                cd += 1
            elif c == "O":
                co += 1
            else:
                l.extend(["O" * co, "." * cd, "#"])
                co = 0
                cd = 0
        d.append("".join(l)[:-1])
    return d


def tilt2(data: list[str]) -> list[str]:
    while True:
        nd = list(map(lambda s: s.replace(".O", "O."), data))
        if nd == data:
            return data
        data = nd


def get_score(data: list[str]) -> int:
    return sum(r.count("O") * i for i, r in enumerate(rotate(data, True), 1))


def part1(data) -> int:
    return get_score(tilt(data))


def part2(data) -> int:
    d = data
    id = hash(tuple(d))
    seen = [id]
    scores = [get_score(d)]
    while True:
        d = tilt(d)
        d = tilt(rotate(d))
        d = tilt(rotate(d))
        d = tilt(rotate(d))
        d = rotate(d)

        id = hash(tuple(d))
        scores.append(get_score(d))
        if id in seen:
            break
        seen.append(id)
    first = seen.index(id)
    cycle = len(seen) - first
    want = (1000000000 - first) % cycle + first
    return scores[want]


def parse(input_data: str):
    data = input_data.splitlines()
    return data


def main(input_data: str):
    data = rotate(parse(input_data), True)
    return part1(data), part2(data)


if __name__ == "__main__":
    from libs.run import run

    run(main)

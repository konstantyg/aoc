#!/usr/bin/env python3
#      --- Day 24: Crossed Wires ---
#   https://adventofcode.com/2024/day/24


def part1(wires: dict[str, bool], gates: list[tuple[str, str, str, str]]) -> int:
    gates = gates.copy()
    while gates:
        i1n, op, i2n, o = gates.pop(0)
        i1 = wires.get(i1n)
        i2 = wires.get(i2n)
        if i1 is None or i2 is None:
            gates.append((i1n, op, i2n, o))
            continue
        if op == "AND":
            wires[o] = i1 & i2
        elif op == "OR":
            wires[o] = i1 | i2
        elif op == "XOR":
            wires[o] = i1 ^ i2
    out = [wires[k] for k in sorted(wires.keys()) if k.startswith("z")]
    return int("".join(map(str, out[::-1])), 2)


def part2(gates: list[tuple[str, str, str, str]]) -> str:
    # https://en.wikipedia.org/wiki/Adder_(electronics)#Ripple-carry_adder
    swapped = set()
    last_z = sorted([o for _, _, _, o in gates if o[0] == "z"])[-1]
    for i1, op, i2, o in gates:
        # gate which produces z has to be XOR (not true for last z)
        if o[0] == "z" and op != "XOR" and o != last_z:
            swapped.add(o)
        # all XOR gates needs to opearate only on x, y or z
        if op == "XOR" and o[0] not in "xyz" and i1[0] not in "xyz" and i2[0] not in "xyz":
            swapped.add(o)
        if op == "AND" and "x00" not in [i1, i2]:
            for subi1, subop, subi2, _ in gates:
                if (o == subi1 or o == subi2) and subop != "OR":
                    swapped.add(o)
        if op == "XOR":
            for subi1, subop, subi2, _ in gates:
                if (o == subi1 or o == subi2) and subop == "OR":
                    swapped.add(o)
    return ",".join(sorted(swapped))


def parse(input_data: str) -> list[int]:
    wires = {}
    gates = []

    for line in input_data.splitlines():
        if ":" in line:
            a, b = line.split(":")
            wires[a] = int(b)
        if "->" in line:
            i1, op, i2, _, o = line.split()
            gates.append((i1, op, i2, o))
    return wires, gates


def main(input_data: str):
    wires, gates = parse(input_data)

    print("P1: ", part1(wires, gates))
    print("P2: ", part2(gates))


if __name__ == "__main__":
    from pathlib import Path

    main(open(Path(__file__).parent / "input").read().strip())

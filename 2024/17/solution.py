#!/usr/bin/env python3
#   --- Day 17: Chronospatial Computer ---
#    https://adventofcode.com/2024/day/17


def run(A, B, C, prog) -> str:
    ret = []

    def combo(n, A, B, C):
        return {4: A, 5: B, 6: C}.get(n, n)

    pointer = 0
    while pointer < len(prog):
        opcode = prog[pointer]
        operand = prog[pointer + 1]
        match opcode:
            case 0:  # adv
                A = A >> combo(operand, A, B, C)
            case 1:  # bxl
                B = B ^ operand
            case 2:  # bst
                B = combo(operand, A, B, C) & 0o7
            case 3:  # jnz
                if A != 0:
                    pointer = operand * 2
                    continue
            case 4:  # bxc
                B = B ^ C
            case 5:  # out
                ret.append(combo(operand, A, B, C) & 0o7)
            case 6:  # bdv
                B = A >> combo(operand, A, B, C)
            case 7:  # cdv
                C = A >> combo(operand, A, B, C)
        pointer += 2
    return ret


def part2(A, B, C, prog):
    A = 0o0
    elems = 1
    felems = prog[-elems:]
    chk_vals = [A]
    while True:
        new_check_vals = []
        for xA in chk_vals:
            for i in range(8):
                if run(xA + i, B, C, prog) == felems:
                    new_check_vals.append((xA + i) << 3)
        if not new_check_vals:
            raise ValueError("No solution")
        chk_vals = new_check_vals
        elems += 1
        if elems > len(prog):
            break
        felems = prog[-elems:]

    return chk_vals[0] >> 3


def parse(input_data: str) -> tuple[int, int, int, list[int]]:
    reg, prog = input_data.split("\n\n")
    reg = reg.splitlines()
    A = int(reg[0].split()[-1])
    B = int(reg[1].split()[-1])
    C = int(reg[2].split()[-1])
    prog = list(map(int, prog.split()[1].split(",")))
    return A, B, C, prog


def main(input_data: str):
    A, B, C, prog = parse(input_data)
    print("P1: ", ",".join(map(str, run(A, B, C, prog))))
    print("P2: ", part2(0, B, C, prog))


if __name__ == "__main__":
    from pathlib import Path

    main(open(Path(__file__).parent / "input").read().strip())

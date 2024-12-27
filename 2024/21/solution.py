#!/usr/bin/env python3
#     --- Day 21: Keypad Conundrum ---
#   https://adventofcode.com/2024/day/21


from functools import cache, cached_property


class Keypad:
    keys = ()

    @cached_property
    def keys_coords(self):
        return {k: (x, y) for y, row in enumerate(self.keys) for x, k in enumerate(row)}

    @cached_property
    def empty_key_pos(self):
        return self.keys_coords[" "]

    @cache
    def get_presses(self, s: str, e: str) -> str:
        x, y = self.keys_coords[s]
        nx, ny = self.keys_coords[e]
        dx, dy = nx - x, ny - y
        path = "<" * -dx + "v" * dy + "^" * -dy + ">" * dx
        if (nx, y) == self.empty_key_pos or (x, ny) == self.empty_key_pos:
            path = path[::-1]
        return path + "A"

    def get_path(self, code: str, repeats: int = 1) -> str:
        if repeats == 0:
            return code
        path = ""
        for s, e in zip("A" + code, code):
            path += self.get_path(self.get_presses(s, e), repeats - 1)
        return path

    @cache
    def get_path_len(self, code: str, repeats: int = 2) -> int:
        if repeats == 0:
            return len(code)
        path_len = 0
        for s, e in zip("A" + code, code):
            path_len += self.get_path_len(self.get_presses(s, e), repeats - 1)
        return path_len


class NumericKeypad(Keypad):
    keys = (
        "789",
        "456",
        "123",
        " 0A",
    )


class DirectionKeypad(Keypad):
    keys = (
        " ^A",
        "<v>",
    )


nk = NumericKeypad()
dk = DirectionKeypad()


def complexity1(code: str) -> int:
    ncode = nk.get_path(code)
    dcode = dk.get_path(ncode)
    dcode2 = dk.get_path(dcode)
    # print(code, dcode2)
    return len(dcode2)


def complexity2(code: str, num_robots: int) -> int:
    ncode = nk.get_path(code)
    dcode_len = dk.get_path_len(ncode, num_robots)
    return dcode_len


def part1(codes: list[str]) -> int:
    return sum(complexity1(code) * int(code[:-1]) for code in codes)


def part2(codes: list[str]) -> int:
    return sum(complexity2(code, 25) * int(code[:-1]) for code in codes)


def parse(input_data: str) -> list[str]:
    return input_data.splitlines()


def main(input_data: str):
    codes = parse(input_data)
    print("P1: ", part1(codes))
    print("P2: ", part2(codes))


if __name__ == "__main__":
    from pathlib import Path

    main("""029A
980A
179A
456A
379A
""")
    main(open(Path(__file__).parent / "input").read().strip())

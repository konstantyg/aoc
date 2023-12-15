#!/usr/bin/env python3
from math import sqrt, prod
from libs.profiler import profiler


@profiler
def solve_math(time, dist):
    # solve quadratic equation
    # (time - x) * x > dist
    # -x^2 + time * x - dist > 0
    delta = sqrt(time * time - 4 * dist)
    x1 = (time - delta) / 2
    x2 = (time + delta) / 2
    # we want to find values bigger than dist
    # so need to substract additional 1 if x1 and x2 == dist
    eq_check = 1 if x1.is_integer() else 0
    # TODO: x2 - x1 equals delta, check rounding errors
    return int(x2) - int(x1) - eq_check


@profiler
def solve_count(time, dist):
    # brute force also finishes in finite time - takes ~4s to run
    # instead of 2 microseconds for the above solution (slower 2_000_000x)
    ways = 0
    for t in range(1, time):
        if (time - t) * t > dist:
            ways += 1
    return ways


@profiler
def solve_binary_search(time, dist):
    low, high = 1, (time + 1) // 2
    while high - low > 1:
        mid = (low + high) // 2
        if (time - mid) * mid > dist:
            high = mid
        else:
            low = mid

    # high is the lowest time which wins the race
    t = high
    remaining = time - t
    # All times between t and remaining (inclusive) will win
    # As such we just need to count how many times that is to know
    # how many winning options there are
    return remaining - t + 1


def part1(data: list[tuple[int, int]]):
    solve = solve_binary_search
    return prod(solve(time, dist) for time, dist in data)


def part2(time, dist):
    solve = solve_binary_search
    return solve(time, dist)


def parse(input_data: str):
    t, d = input_data.splitlines()
    ti = list(map(int, t.split()[1:]))
    di = list(map(int, d.split()[1:]))
    data = list(zip(ti, di))
    time = int(t.split(":")[1].replace(" ", ""))
    dist = int(d.split(":")[1].replace(" ", ""))
    return data, time, dist


def main(input_data: str):
    data, time, dist = parse(input_data)
    return part1(data), part2(time, dist)


if __name__ == "__main__":
    from libs.run import run

    run(main)

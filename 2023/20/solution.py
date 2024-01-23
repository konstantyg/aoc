#!/usr/bin/env python3

from dataclasses import dataclass, field
from typing import TypeAlias
from math import prod

Inst: TypeAlias = tuple[str, int]
Point: TypeAlias = tuple[int, int]
from collections import deque


@dataclass
class Mod:
    name: str
    dest: list[str] = field(default_factory=list)
    senders: list[str] = field(default_factory=list)
    state: dict[str, int] = field(default_factory=dict)

    def recv(self, q: deque, signal: int, sender: str, push=0) -> None:
        if isinstance(signal, int):
            return
        prev_sender, push = signal
        self.state[prev_sender] = push


@dataclass
class Broadcast(Mod):
    def recv(self, q: deque, signal: int, sender: str, push=0) -> None:
        for d in self.dest:
            q.append((signal, d, self.name))


@dataclass
class FlipFlop(Mod):
    state: int = 0

    def recv(self, q: deque, signal: int, sender: str, push=0) -> None:
        if signal == 0:
            self.state = 1 - self.state
            for d in self.dest:
                q.append((self.state, d, self.name))


@dataclass
class Conjunction(Mod):
    state: int = 0

    def recv(self, q: deque, signal: int, sender: str, push=0) -> None:
        i = self.senders.index(sender)
        if signal == 0:
            self.state &= ~(1 << i)
        else:
            self.state |= 1 << i
        pulse = 1
        if (1 << len(self.senders)) - 1 == self.state:
            pulse = 0
        for d in self.dest:
            if d == "rx":
                if self.state & 1 << i:
                    q.append(((sender, push), d, self.name))
            q.append((pulse, d, self.name))


def part1(mods) -> int:
    c = [0, 0]
    for push in range(1000):
        steps = deque([(0, "broadcaster", "button")])
        while steps:
            signal, dest, sender = steps.popleft()
            if isinstance(signal, int):
                c[signal] += 1
            else:
                _, push = signal
                c[push] += 1

            d = mods.get(dest)
            if d is None:
                continue
            d.recv(steps, signal, sender)
    return c[0] * c[1]


def part2(mods) -> int:
    push = 0
    rx = mods["rx"]
    while True:
        push += 1
        if len(rx.state) == 4:
            return prod(rx.state.values())
        steps = deque([(0, "broadcaster", "button")])
        while steps:
            signal, dest, sender = steps.popleft()
            d = mods.get(dest)
            if d is None:
                continue
            d.recv(steps, signal, sender, push)


def parse(input_data: str) -> dict[str, tuple[str, list[str]]]:
    mods = {}
    for line in input_data.splitlines():
        md, dest = line.split(" -> ")
        if md[0] == "b":
            t = "b"
            n = "broadcaster"
        else:
            t, n = md[0], md[1:]
        dest = dest.split(", ")
        if t == "b":
            mods[n] = Broadcast(n, dest)
        elif t == "%":
            mods[n] = FlipFlop(n, dest)
        elif t == "&":
            mods[n] = Conjunction(n, dest)
    empty_mods = []
    for mod in mods.values():
        for d in mod.dest:
            if d not in mods:
                empty_mods.append(d)
    for mod in empty_mods:
        mods[mod] = Mod(mod)
    for mod in mods.values():
        for d in mod.dest:
            if mod.name not in mods[d].senders:
                mods[d].senders.append(mod.name)
    for dest in mods["rx"].dest:
        mods["rx"].senders.append("rx")
    return mods


def main(input_data: str):
    nodes = parse(input_data)
    nodes2 = parse(input_data)
    return part1(nodes), part2(nodes2)


if __name__ == "__main__":
    from libs.run import run

    run(main)

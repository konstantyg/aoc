#!/usr/bin/env python3

from math import prod
import networkx as nx


def part1(wires: list[tuple[str, str]]) -> int:
    G = nx.Graph()
    G.add_edges_from(wires)
    G.remove_edges_from(nx.minimum_edge_cut(G))
    return prod(len(c) for c in nx.connected_components(G))


def parse(input_data: str):
    wires: list[tuple[str, str]] = []
    for line in input_data.splitlines():
        w1, conn = line.split(": ")
        for w2 in conn.split():
            wires.append((w1, w2))
    return wires


def main(input_data: str):
    wires = parse(input_data)
    return part1(wires)


if __name__ == "__main__":
    from libs.run import run

    run(main)

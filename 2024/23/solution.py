#!/usr/bin/env python3
#        --- Day 23: LAN Party ---
#   https://adventofcode.com/2024/day/23


import networkx as nx


def process(connections: list[tuple[str, str]]) -> int:
    # https://en.wikipedia.org/wiki/Clique_problem
    s = 0
    G = nx.Graph()
    G.add_edges_from(connections)
    for party in nx.enumerate_all_cliques(G):
        if len(party) == 3:
            if any(p.startswith("t") for p in party):
                s += 1

    return s, ",".join(sorted(party))


def parse(input_data: str) -> list[int]:
    return list(tuple(line.split("-")) for line in input_data.splitlines())


def main(input_data: str):
    connections = parse(input_data)
    p1, p2 = process(connections)
    print("P1: ", p1)
    print("P2: ", p2)


if __name__ == "__main__":
    from pathlib import Path

    main(open(Path(__file__).parent / "input").read().strip())

#!/usr/bin/env python3


from collections import Counter


card_types = "X23456789TJQKA"
card_types_j = "23456789TQKA"
MAX_CARDS = 5


def score(hand) -> list[int]:
    c = Counter(hand)
    return sorted(c.values(), reverse=True) + [0] * (MAX_CARDS - len(c))


def digits_to_int(counts) -> int:
    return int("".join(map(str, counts)))


class Hand:
    joker = False
    cv = {v: k for k, v in enumerate(card_types, 10)}

    def __init__(self, cards: str, bet):
        self.cards = cards
        self.bet = int(bet)
        self.score_nj = digits_to_int(
            score(self.cards) + [self.cv[c] for c in self.cards]
        )
        self.score_wj = digits_to_int(
            max(score(self.cards.replace("J", c)) for c in card_types_j)
            + [self.cv[c] for c in self.cards.replace("J", "X")]
        )

    @property
    def score(self):
        return self.score_wj if self.joker else self.score_nj

    def __repr__(self):
        return f"{self.cards} {self.bet} {self.score}"

    def __lt__(self, other):
        return self.score < other.score


def part1(data: list[Hand]):
    return sum(h.bet * i for i, h in enumerate(sorted(data), 1))


def part2(data: list[Hand]):
    s = 0
    Hand.joker = True
    for i, h in enumerate(sorted(data), 1):
        s += h.bet * i
    return s


def parse(input_data: str):
    return [Hand(*line.split()) for line in input_data.splitlines()]


def main(input_data: str):
    data = parse(input_data)
    return part1(data), part2(data)


if __name__ == "__main__":
    from libs.run import run

    run(main)

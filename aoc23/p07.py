from __future__ import annotations
import collections
import enum
import functools
import typing

from aoc23 import utils


REGULAR_CARD_NAMES = list("23456789TJQKA")
REGULAR_CARD_VALUES = {s: i for i, s in enumerate(REGULAR_CARD_NAMES)}

JOKER_CARD_NAMES = list("J23456789TQKA")
JOKER_CARD_VALUES = {s: i for i, s in enumerate(JOKER_CARD_NAMES)}


class Card(typing.NamedTuple):
    value: int
    joker: bool

    @classmethod
    def from_str(cls, s: str, *, joker: bool) -> Card:
        try:
            values = JOKER_CARD_VALUES if joker else REGULAR_CARD_VALUES
            return Card(values[s], joker=joker)
        except KeyError:
            raise ValueError(f"Unknown card: {s!r}")

    def __str__(self) -> str:
        names = JOKER_CARD_NAMES if self.joker else REGULAR_CARD_NAMES
        return names[self.value]


class HandType(enum.IntEnum):
    HIGH_CARD = enum.auto()
    ONE_PAIR = enum.auto()
    TWO_PAIR = enum.auto()
    THREE_OF_KIND = enum.auto()
    FULL_HOUSE = enum.auto()
    FOUR_OF_KIND = enum.auto()
    FIVE_OF_KIND = enum.auto()


@functools.total_ordering
class Hand(typing.NamedTuple):
    cards: tuple[Card, ...]
    bid: int
    joker: bool

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Hand):
            return False
        return self.cards == other.cards

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Hand):
            return False

        if self.hand_type() < other.hand_type():
            return True
        elif self.hand_type() > other.hand_type():
            return False

        for c1, c2 in zip(self.cards, other.cards):
            if c1 < c2:
                return True
            elif c1 > c2:
                return False
        return False

    @functools.cache
    def hand_type(self) -> HandType:
        return self.joker_hand_type() if self.joker else self.regular_hand_type()

    def regular_hand_type(self) -> HandType:
        counter = collections.Counter(self.cards)
        counts = list(counter.values())
        if 5 in counts:
            return HandType.FIVE_OF_KIND
        elif 4 in counts:
            return HandType.FOUR_OF_KIND
        elif 3 in counts and 2 in counts:
            return HandType.FULL_HOUSE
        elif 3 in counts:
            return HandType.THREE_OF_KIND
        elif counts.count(2) == 2:
            return HandType.TWO_PAIR
        elif 2 in counts:
            return HandType.ONE_PAIR
        else:
            return HandType.HIGH_CARD

    def joker_hand_type(self) -> HandType:
        counter = collections.Counter(self.cards)
        joker = Card.from_str("J", joker=True)
        non_joker_counts = [count for card, count in counter.items() if card != joker]
        all_counts = set(non_joker_counts) | (
            {22} if non_joker_counts.count(2) == 2 else set()
        )
        jokers_count = counter[joker]
        # ([regular, ...], joker)
        rules: list[tuple[list[tuple[list[int], int]], HandType]] = [
            (
                [([5], 0), ([4], 1), ([3], 2), ([2], 3), ([1], 4), ([], 5)],
                HandType.FIVE_OF_KIND,
            ),
            ([([4], 0), ([3], 1), ([2], 2), ([1], 3)], HandType.FOUR_OF_KIND),
            ([([2, 3], 0), ([22], 1)], HandType.FULL_HOUSE),
            ([([3], 0), ([2], 1), ([1], 2)], HandType.THREE_OF_KIND),
            ([([22], 0)], HandType.TWO_PAIR),
            ([([2], 0), ([1], 1)], HandType.ONE_PAIR),
            ([([1], 0)], HandType.HIGH_CARD),
        ]
        for combs, result in rules:
            for cnts, jkrs in combs:
                if all(cnt in all_counts for cnt in cnts) and jkrs == jokers_count:
                    return result
        raise ValueError(f"Unknown hand type: {self}")


def total_winnings(hands: list[Hand]) -> int:
    sorted_hands = sorted(hands)
    return sum(hand.bid * rank for rank, hand in enumerate(sorted_hands, start=1))


def parse_input(lines: list[str], *, joker: bool) -> list[Hand]:
    return [parse_line(line, joker=joker) for line in lines]


def parse_line(line: str, *, joker: bool) -> Hand:
    cards_str, bid = line.split(" ", 1)
    return Hand(
        cards=tuple(Card.from_str(c, joker=joker) for c in cards_str),
        bid=int(bid),
        joker=joker,
    )


def main() -> None:
    lines = utils.read_input_lines(__file__)
    print(total_winnings(parse_input(lines, joker=False)))
    print(total_winnings(parse_input(lines, joker=True)))


if __name__ == "__main__":
    main()

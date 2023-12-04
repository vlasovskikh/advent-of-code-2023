import functools
import re
import typing

from aoc23 import utils


class Card(typing.NamedTuple):
    """Scratch card with our numbers and winning numbers."""

    winning_numbers: tuple[int, ...]
    our_numbers: tuple[int, ...]

    def matching_numbers(self) -> int:
        # O(n)
        return len(set(self.winning_numbers) & set(self.our_numbers))

    def winning_points(self) -> int:
        count = self.matching_numbers()
        if count == 0:
            return 0
        return 2 ** (count - 1)


def parse_input(lines: list[str]) -> list[Card]:
    return [parse_line(line) for line in lines]


def sum_winning_points(cards: list[Card]) -> int:
    """Sum winning points on all the cards."""
    return sum(card.winning_points() for card in cards)


def sum_total_cards(cards: list[Card]) -> int:
    """Sum total amount of cards won by this set of cards."""
    cards_tuple = tuple(cards)
    return sum(total_cards_won(cards_tuple, i) for i in range(len(cards)))


@functools.cache
def total_cards_won(cards: tuple[Card, ...], card: int) -> int:
    """Count of total cards won by the specified card."""
    matches = cards[card].matching_numbers()
    copies = range(card + 1, min(card + matches + 1, len(cards)))
    return 1 + sum(total_cards_won(cards, copy) for copy in copies)


def parse_line(line: str) -> Card:
    m = re.match(r"Card +\d+: (.*) \| (.*)", line)
    if not m:
        raise ValueError(f"Unknown line: {line}")
    return Card(
        winning_numbers=tuple(int(n) for n in m.group(1).strip().split()),
        our_numbers=tuple(int(n) for n in m.group(2).strip().split()),
    )


def main() -> None:
    cards = parse_input(utils.read_input_lines(__file__))
    print(sum_winning_points(cards))
    print(sum_total_cards(cards))


if __name__ == "__main__":
    main()

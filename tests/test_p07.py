import pytest
from aoc23 import p07


def test_example_1() -> None:
    lines = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
""".strip().splitlines()
    assert p07.total_winnings(p07.parse_input(lines, joker=False)) == 6440


def test_example_2() -> None:
    lines = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
""".strip().splitlines()
    assert p07.total_winnings(p07.parse_input(lines, joker=True)) == 5905


@pytest.mark.parametrize(
    "cards,expected",
    [
        ("JJJJJ", p07.HandType.FIVE_OF_KIND),
        ("22222", p07.HandType.FIVE_OF_KIND),
        ("JJJJ2", p07.HandType.FIVE_OF_KIND),
        ("JJJ22", p07.HandType.FIVE_OF_KIND),
        ("JJ222", p07.HandType.FIVE_OF_KIND),
        ("J2222", p07.HandType.FIVE_OF_KIND),
        ("JJJ23", p07.HandType.FOUR_OF_KIND),
        ("JJ223", p07.HandType.FOUR_OF_KIND),
        ("J2223", p07.HandType.FOUR_OF_KIND),
        ("22223", p07.HandType.FOUR_OF_KIND),
        ("J2233", p07.HandType.FULL_HOUSE),
        ("22333", p07.HandType.FULL_HOUSE),
        ("JJ234", p07.HandType.THREE_OF_KIND),
        ("J2234", p07.HandType.THREE_OF_KIND),
        ("22234", p07.HandType.THREE_OF_KIND),
    ],
)
def test_joker_hand_type(cards: str, expected: p07.HandType) -> None:
    hand = p07.parse_line(f"{cards} 0", joker=True)
    assert hand.hand_type() == expected

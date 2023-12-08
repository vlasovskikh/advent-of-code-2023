import pytest

from aoc23 import p08


@pytest.mark.parametrize(
    ["input", "expected"],
    [
        (
            """
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
""",
            2,
        ),
        (
            """
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
""",
            6,
        ),
    ],
)
def test_example_1(input, expected) -> None:
    map = p08.parse_input(input.strip().splitlines())
    assert p08.count_steps(map) == expected


def test_example_2() -> None:
    lines = """
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
""".strip().splitlines()
    map = p08.parse_input(lines)
    assert p08.count_ghost_steps(map) == 6

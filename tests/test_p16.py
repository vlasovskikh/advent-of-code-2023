import pytest

from aoc23 import p16


def test_example_1() -> None:
    lines = r"""
.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
""".strip().splitlines()
    grid = p16.parse_lines(lines)
    assert grid.energized_count() == 46


@pytest.mark.parametrize(
    ("s", "expected"),
    [
        (
            r"""
\.
\.
""",
            3,
        ),
        (
            r"""
|-
\/
""",
            4,
        ),
    ],
)
def test_small_examples(s: str, expected: int) -> None:
    grid = p16.parse_lines(s.strip().splitlines())
    assert grid.energized_count() == expected


def test_example_2() -> None:
    lines = r"""
.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
""".strip().splitlines()
    grid = p16.parse_lines(lines)
    assert grid.max_energized() == 51

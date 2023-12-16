import pytest

from aoc23 import p14


def test_example() -> None:
    lines = """
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
""".strip().splitlines()
    platform = p14.parse_lines(lines)
    assert p14.load_after_tilt_north(platform) == 136


def test_spin_cycle() -> None:
    lines = """
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
""".strip().splitlines()
    platform = p14.parse_lines(lines)

    platform.spin_cycle()
    spin1 = """
.....#....
....#...O#
...OO##...
.OO#......
.....OOO#.
.O#...O#.#
....O#....
......OOOO
#...O###..
#..OO#....
""".strip()
    assert str(platform) == spin1

    spin2 = """
.....#....
....#...O#
.....##...
..O#......
.....OOO#.
.O#...O#.#
....O#...O
.......OOO
#..OO###..
#.OOO#...O
""".strip()
    platform.spin_cycle()
    assert str(platform) == spin2

    spin3 = """
.....#....
....#...O#
.....##...
..O#......
.....OOO#.
.O#...O#.#
....O#...O
.......OOO
#...O###.O
#.OOO#...O
""".strip()
    platform.spin_cycle()
    assert str(platform) == spin3


def test_example_2() -> None:
    lines = """
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
""".strip().splitlines()
    platform = p14.parse_lines(lines)
    platform.spin(1_000_000_000)
    assert platform.north_load() == 64


@pytest.mark.parametrize(
    ["count", "expected"],
    [
        (1, 3),
        (2, 3),
        (3, 3),
    ],
)
def test_cycle_of_1(count: int, expected: int) -> None:
    lines = """
OOO
...
...
""".strip().splitlines()
    platform = p14.parse_lines(lines)
    platform.spin(count)
    assert platform.north_load() == expected


@pytest.mark.parametrize(
    ["count", "expected"],
    [
        (1, 5),
        (2, 4),
        (3, 6),
        (4, 4),
        (5, 6),
        (6, 4),
        (7, 6),
    ],
)
def test_cycle_of_2(count: int, expected: int) -> None:
    lines = """
OOO
..#
...
""".strip().splitlines()
    platform = p14.parse_lines(lines)
    platform.spin(count)
    assert platform.north_load() == expected

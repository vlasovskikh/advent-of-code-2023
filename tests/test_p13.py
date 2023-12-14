from aoc23 import p13


def test_example_1() -> None:
    lines = """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
""".strip().splitlines()
    patterns = p13.parse_input(lines)
    assert p13.summarize(patterns, smudges=0) == 405


def test_example_2() -> None:
    lines = """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
""".strip().splitlines()
    patterns = p13.parse_input(lines)
    assert p13.summarize(patterns, smudges=1) == 400

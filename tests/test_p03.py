from aoc23 import p03


def test_example_1() -> None:
    lines = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
""".strip().splitlines()
    schematic = p03.parse_input(lines)
    assert p03.sum_part_numbers(schematic) == 4361


def test_example_2() -> None:
    lines = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
""".strip().splitlines()
    schematic = p03.parse_input(lines)
    assert p03.sum_gear_ratios(schematic) == 467835

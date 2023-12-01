from aoc23 import p01


def test_example_1() -> None:
    lines = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
""".strip().splitlines()
    assert p01.sum_only_digits(p01.parse_input(lines)) == 142


def test_example_2() -> None:
    lines = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
""".strip().splitlines()
    assert p01.sum_all_digits(p01.parse_input(lines)) == 281

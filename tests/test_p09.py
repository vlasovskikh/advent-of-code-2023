from aoc23 import p09


def test_example_1() -> None:
    lines = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
""".strip().splitlines()
    assert p09.sum_extrapolated_values(p09.parse_lines(lines), forwards=True) == 114


def test_example_2() -> None:
    lines = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
""".strip().splitlines()
    assert p09.sum_extrapolated_values(p09.parse_lines(lines), forwards=False) == 2

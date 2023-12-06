import pytest

from aoc23 import p06


@pytest.mark.parametrize(
    "time,distance,expected",
    [
        (7, 9, 4),
        (15, 40, 8),
        (30, 200, 9),
    ],
)
def test_example_small(time, distance, expected) -> None:
    assert p06.ways_to_beat_record(p06.Race(time, distance)) == expected


def test_example_1() -> None:
    lines = """
Time:      7  15   30
Distance:  9  40  200
""".strip().splitlines()
    assert p06.total_ways_to_beat_record(p06.parse_input(lines)) == 288


def test_example_2() -> None:
    lines = """
Time:      7  15   30
Distance:  9  40  200
""".strip().splitlines()
    assert p06.ways_to_beat_record(p06.fixed_parse_input(lines)) == 71503

import pytest

from aoc23 import p12


@pytest.mark.parametrize(
    ["line", "expected"],
    [
        ("???.### 1,1,3", 1),
        (".??..??...?##. 1,1,3", 4),
        ("?#?#?#?#?#?#?#? 1,3,1,6", 1),
        ("????.#...#... 4,1,1", 1),
        ("????.######..#####. 1,6,5", 4),
        ("?###???????? 3,2,1", 10),
    ],
)
def test_example_1(line: str, expected: int) -> None:
    record = p12.parse_record(line)
    assert record.arrangements() == expected


def test_example_2() -> None:
    lines = """
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
""".strip().splitlines()
    records = p12.unfold_records(p12.parse_input(lines))
    assert p12.sum_of_arrangements(records) == 525152

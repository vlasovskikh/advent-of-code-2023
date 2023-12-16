from aoc23 import p15


def test_example_1() -> None:
    lines = """
rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
""".strip().splitlines()
    assert p15.sum_step_hashes(p15.parse_lines(lines)) == 1320


def test_example_2() -> None:
    lines = """
rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
""".strip().splitlines()
    assert p15.focusing_power(p15.parse_lines(lines)) == 145

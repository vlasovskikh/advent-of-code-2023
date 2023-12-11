from aoc23 import p10


def test_example_1() -> None:
    lines = """
.....
.S-7.
.|.|.
.L-J.
.....
""".strip().splitlines()
    assert p10.farthest_tile(p10.parse_lines(lines)) == 4


def test_example_2() -> None:
    lines = """
...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
""".strip().splitlines()
    assert p10.tiles_inside_loop(p10.parse_lines(lines)) == 4


def test_example_3() -> None:
    lines = """
.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...
""".strip().splitlines()
    assert p10.tiles_inside_loop(p10.parse_lines(lines)) == 8


def test_example_4() -> None:
    lines = """
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
""".strip().splitlines()
    assert p10.tiles_inside_loop(p10.parse_lines(lines)) == 10

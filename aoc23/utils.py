import dataclasses
import itertools
import os
import typing
from pathlib import Path


T = typing.TypeVar("T")


def read_input_lines(module_path: str) -> list[str]:
    """Read lines of the input file that corresponds to the module name."""
    with open(input_file_path(module_path), "r") as fd:
        return [s.strip() for s in fd.readlines()]


def input_file_path(module_path: str) -> Path:
    """Input file path from `data/` that corresponds to the module name."""
    p = Path(module_path)  # "<path>/advent-of-code-2023/aoc23/p01.py"
    module_name, _ = os.path.splitext(p.name)
    return p.parent / ".." / "data" / f"{module_name}.txt"


def sliding_window(xs: typing.Iterable[T], n: int) -> typing.Iterable[tuple[T, ...]]:
    """Return a sliding window of size `n` for the specified iterable."""
    iterators = itertools.tee(xs, n)
    for shift_count, iterator in enumerate(iterators):
        for _ in range(shift_count):
            next(iterator, None)
    return zip(*iterators)


def split_by_empty_lines(lines: list[str]) -> list[list[str]]:
    """Split a list of lines into sections separated by empty lines in the list."""
    return [list(g) for k, g in itertools.groupby(lines, key=bool) if k]


class Coord(typing.NamedTuple):
    line: int
    pos: int


@dataclasses.dataclass
class Grid(typing.Generic[T]):
    """2D grid of tiles suitable for maze-like puzzles."""

    data: list[list[T]]

    def size(self) -> Coord:
        return Coord(len(self.data), len(self.data[0]))

    def lines(self) -> list[list[Coord]]:
        return [
            [Coord(line, pos) for pos in range(len(self.data[line]))]
            for line in range(len(self.data))
        ]

    def positions(self) -> list[list[Coord]]:
        return [
            [Coord(line, pos) for line in range(len(self.data))]
            for pos in range(len(self.data[0]))
        ]

    def neighbors(self, coord: Coord) -> list[Coord]:
        return self.cross_neighbors(coord) + self.diagonal_neighbors(coord)

    def cross_neighbors(self, coord: Coord) -> list[Coord]:
        results = []
        for line, pos in [
            (coord.line, coord.pos - 1),
            (coord.line, coord.pos + 1),
            (coord.line - 1, coord.pos),
            (coord.line + 1, coord.pos),
        ]:
            if 0 <= line < len(self.data) and 0 <= pos < len(self.data[coord.line]):
                results.append(Coord(line, pos))
        return results

    def diagonal_neighbors(self, coord: Coord) -> list[Coord]:
        return [
            Coord(line, pos)
            for line, pos in [
                (coord.line - 1, coord.pos - 1),
                (coord.line - 1, coord.pos + 1),
                (coord.line + 1, coord.pos - 1),
                (coord.line + 1, coord.pos + 1),
            ]
            if 0 <= line < len(self.data) and 0 <= pos < len(self.data[coord.line])
        ]

    def __getitem__(self, coord: Coord) -> T:
        return self.data[coord.line][coord.pos]

    def __iter__(self) -> typing.Iterator[Coord]:
        for line in range(len(self.data)):
            for pos in range(len(self.data[line])):
                yield Coord(line, pos)

    def __str__(self) -> str:
        return "\n".join("".join(str(x) for x in line) for line in self.data)

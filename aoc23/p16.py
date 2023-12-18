from __future__ import annotations
import dataclasses
import typing
import enum

import numpy as np

from aoc23 import utils


class Dir(enum.Enum):
    UP = enum.auto()
    RIGHT = enum.auto()
    DOWN = enum.auto()
    LEFT = enum.auto()


class Coord(typing.NamedTuple):
    line: int
    pos: int


class State(typing.NamedTuple):
    coord: Coord
    dir: Dir


@dataclasses.dataclass
class Grid:
    data: np.ndarray

    def energized_count(
        self,
        state: State = State(Coord(0, 0), Dir.RIGHT),
        *,
        cache: dict[State, frozenset[Coord]] | None = None,
    ) -> int:
        if cache is None:
            cache = {}
        res, _ = self.cached_energized(state, cache=cache, visited=frozenset())
        return len(res)

    def cached_energized(
        self,
        state: State,
        *,
        cache: dict[State, frozenset[Coord]],
        visited: frozenset[State] = frozenset(),
    ) -> tuple[frozenset[Coord], frozenset[State]]:
        if state in cache:
            return cache[state], frozenset()
        if state in visited:
            return frozenset(), frozenset([state])
        line, pos = state.coord
        length, width = self.data.shape
        if line < 0 or line >= length or pos < 0 or pos >= width:
            return frozenset(), frozenset()
        cell = typing.cast(str, self.data[line, pos])
        dirs = self.next_dirs(cell, state.dir)
        res = frozenset([state.coord])
        loops: frozenset[State] = frozenset()
        for dir in dirs:
            coord = self.next_coord(state.coord, dir)
            new_res, new_loops = self.cached_energized(
                State(coord, dir),
                cache=cache,
                visited=visited | frozenset([state]),
            )
            res |= new_res
            loops |= new_loops
        if state in loops:
            loops -= frozenset([state])
        elif not loops:
            cache[state] = res
        return res, loops

    def max_energized(self):
        res = 0
        cache = {}
        length, width = self.data.shape
        for i in range(length):
            res = max(
                self.energized_count(State(Coord(i, 0), Dir.RIGHT), cache=cache),
                res,
            )
            res = max(
                self.energized_count(State(Coord(i, width - 1), Dir.LEFT), cache=cache),
                res,
            )
        for j in range(width):
            res = max(
                self.energized_count(State(Coord(0, j), Dir.DOWN), cache=cache),
                res,
            )
            res = max(
                self.energized_count(State(Coord(length - 1, j), Dir.UP), cache=cache),
                res,
            )
        return res

    @staticmethod
    def next_dirs(cell: str, dir: Dir) -> list[Dir]:
        match cell, dir:
            case ".", _:
                return [dir]
            case ("/", Dir.RIGHT) | ("\\", Dir.LEFT):
                return [Dir.UP]
            case ("/", Dir.DOWN) | ("\\", Dir.UP):
                return [Dir.LEFT]
            case ("/", Dir.LEFT) | ("\\", Dir.RIGHT):
                return [Dir.DOWN]
            case ("/", Dir.UP) | ("\\", Dir.DOWN):
                return [Dir.RIGHT]
            case ("-", (Dir.LEFT | Dir.RIGHT)) | ("|", (Dir.UP | Dir.DOWN)):
                return [dir]
            case "|", (Dir.LEFT | Dir.RIGHT):
                return [Dir.UP, Dir.DOWN]
            case "-", (Dir.UP | Dir.DOWN):
                return [Dir.LEFT, Dir.RIGHT]
            case _:
                raise ValueError(f"Unknown direction {dir} for cell {cell!r}")

    @staticmethod
    def next_coord(coord: Coord, dir: Dir) -> Coord:
        match dir:
            case Dir.UP:
                return Coord(coord.line - 1, coord.pos)
            case Dir.RIGHT:
                return Coord(coord.line, coord.pos + 1)
            case Dir.DOWN:
                return Coord(coord.line + 1, coord.pos)
            case Dir.LEFT:
                return Coord(coord.line, coord.pos - 1)

    def __repr__(self) -> str:
        grid = "\n".join("".join(line) for line in self.data)
        return f"<Grid:\n{grid}\n>"


def parse_lines(lines: list[str]) -> Grid:
    return Grid(np.array([list(line) for line in lines]))


def main() -> None:
    grid = parse_lines(utils.read_input_lines(__file__))
    print(grid.energized_count())
    print(grid.max_energized())


if __name__ == "__main__":
    main()

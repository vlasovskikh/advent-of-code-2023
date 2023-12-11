from __future__ import annotations
import enum

from aoc23 import utils


class Tile(enum.StrEnum):
    SPACE = "."
    GALAXY = "#"


class Universe(utils.Grid[Tile]):
    def expanded_indexes(self) -> tuple[list[int], list[int]]:
        expanded_lines = [
            i
            for i, line in enumerate(self.lines())
            if all(self[c] == Tile.SPACE for c in line)
        ]
        expanded_positions = [
            i
            for i, pos in enumerate(self.positions())
            if all(self[c] == Tile.SPACE for c in pos)
        ]
        return expanded_lines, expanded_positions

    def galaxies(self) -> list[utils.Coord]:
        return [c for c in self if self[c] == Tile.GALAXY]


def parse_input(lines: list[str]) -> Universe:
    return Universe([[Tile(c) for c in line] for line in lines])


def sum_shortest_paths(universe: Universe, expansion_coefficient: int) -> int:
    galaxies = universe.galaxies()
    pairs = [
        (g1, g2)
        for i, g1 in enumerate(galaxies)
        for j, g2 in enumerate(galaxies)
        if i < j
    ]
    expanded_indexes = universe.expanded_indexes()
    distances = [
        distance(
            g1,
            g2,
            expanded_indexes=expanded_indexes,
            expansion_coefficient=expansion_coefficient,
        )
        for g1, g2 in pairs
    ]
    return sum(distances)


def distance(
    g1: utils.Coord,
    g2: utils.Coord,
    *,
    expanded_indexes: tuple[list[int], list[int]],
    expansion_coefficient: int,
) -> int:
    exp_lines, exp_positions = expanded_indexes
    line_start, line_stop = sorted([g1.line, g2.line])
    pos_start, pos_stop = sorted([g1.pos, g2.pos])
    exp_lines_count = len([line for line in exp_lines if line_start < line < line_stop])
    exp_positions_count = len(
        [pos for pos in exp_positions if pos_start < pos < pos_stop]
    )
    n = expansion_coefficient - 1
    return (
        abs(g1.line - g2.line)
        + n * exp_lines_count
        + abs(g1.pos - g2.pos)
        + n * exp_positions_count
    )


def main() -> None:
    universe = parse_input(utils.read_input_lines(__file__))
    print(sum_shortest_paths(universe, expansion_coefficient=2))
    print(sum_shortest_paths(universe, expansion_coefficient=1_000_000))


if __name__ == "__main__":
    main()

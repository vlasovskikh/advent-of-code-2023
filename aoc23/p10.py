from __future__ import annotations

import enum

from aoc23 import utils


class Tile(enum.StrEnum):
    V = "|"
    H = "-"
    L = "L"
    J = "J"
    S7 = "7"
    F = "F"
    GROUND = "."
    START = "S"

    def to_ascii(self) -> str:
        return ASCII_TABLES.get(self, self.value)

    def connections(self) -> list[utils.Coord]:
        return TILE_CONNECTIONS[self]


TILE_CONNECTIONS: dict[Tile, list[utils.Coord]] = {
    Tile.V: [utils.Coord(-1, 0), utils.Coord(1, 0)],
    Tile.H: [utils.Coord(0, -1), utils.Coord(0, 1)],
    Tile.L: [utils.Coord(-1, 0), utils.Coord(0, 1)],
    Tile.J: [utils.Coord(-1, 0), utils.Coord(0, -1)],
    Tile.S7: [utils.Coord(1, 0), utils.Coord(0, -1)],
    Tile.F: [utils.Coord(1, 0), utils.Coord(0, 1)],
    Tile.GROUND: [],
    Tile.START: [
        utils.Coord(-1, 0),
        utils.Coord(1, 0),
        utils.Coord(0, -1),
        utils.Coord(0, 1),
    ],
}


ASCII_TABLES = {
    Tile.V: "│",
    Tile.H: "─",
    Tile.L: "└",
    Tile.J: "┘",
    Tile.S7: "┐",
    Tile.F: "┌",
}


class PipeGrid(utils.Grid[Tile]):
    def loop_tiles(self) -> list[utils.Coord]:
        start = self._start()
        cur = prev = start
        steps = 0
        tiles: list[utils.Coord] = []
        while True:
            tiles.append(cur)
            cur, prev = next(c for c in self._connections(cur) if c != prev), cur
            if cur == start:
                return tiles
            steps += 1

    def clear(self) -> PipeGrid:
        loop = set(self.loop_tiles())

        def replace_start(c: utils.Coord) -> Tile:
            c1, c2 = self._connections(c)
            max_line = max(c1.line, c2.line)
            max_pos = max(c1.pos, c2.pos)
            min_line = min(c1.line, c2.line)
            min_pos = min(c1.pos, c2.pos)
            if c1.line == c2.line:
                return Tile.H
            elif c1.pos == c2.pos:
                return Tile.V
            elif c.line == max_line and c.pos == max_pos:
                return Tile.J
            elif c.line == max_line and c.pos == min_pos:
                return Tile.L
            elif c.line == min_line and c.pos == min_pos:
                return Tile.F
            elif c.line == min_line and c.pos == max_pos:
                return Tile.S7
            else:
                raise ValueError(f"Unknown connection type for S={c}: {c1=}, {c2=}")

        def clean_tile(c: utils.Coord) -> Tile:
            tile = self[c]
            if tile == Tile.START:
                return replace_start(c)
            elif c not in loop:
                return Tile.GROUND
            else:
                return tile

        return PipeGrid(
            [[clean_tile(coord) for coord in line] for line in self.lines()]
        )

    def _start(self) -> utils.Coord:
        s = next((c for c in self if self[c] == Tile.START), None)
        if s is None:
            raise ValueError("Start not found")
        return s

    def _connections(self, coord: utils.Coord) -> list[utils.Coord]:
        return [
            n
            for n in (self.cross_neighbors(coord))
            if self._connects_to(coord, n) and (self._connects_to(n, coord))
        ]

    def _connects_to(self, c1: utils.Coord, c2: utils.Coord) -> bool:
        tile = self[c1]
        for c in tile.connections():
            if c1.line + c.line == c2.line and c1.pos + c.pos == c2.pos:
                return True
        return False

    def __str__(self) -> str:
        return "\n".join(
            "".join(self[x].to_ascii() for x in line) for line in self.lines()
        )


def farthest_tile(grid: PipeGrid) -> int:
    return len(grid.loop_tiles()) // 2


def tiles_inside_loop(grid: PipeGrid) -> int:
    grid = grid.clear()
    count = 0
    for line in grid.lines():
        state = InsideLoopState.OUTSIDE_NONE
        for coord in line:
            tile = grid[coord]
            state = state.transition(tile)
            if tile == Tile.GROUND and state == InsideLoopState.INSIDE_NONE:
                count += 1
    return count


def parse_lines(lines: list[str]) -> PipeGrid:
    return PipeGrid(data=[[Tile(c) for c in line] for line in lines])


class InsideLoopState(enum.Enum):
    # I/O  L/F/None
    INSIDE_L = enum.auto()
    INSIDE_F = enum.auto()
    INSIDE_NONE = enum.auto()
    OUTSIDE_L = enum.auto()
    OUTSIDE_F = enum.auto()
    OUTSIDE_NONE = enum.auto()

    def transition(self, tile: Tile) -> InsideLoopState:
        match self, tile:
            case InsideLoopState.INSIDE_L, Tile.J:
                return InsideLoopState.INSIDE_NONE
            case InsideLoopState.INSIDE_L, Tile.S7:
                return InsideLoopState.OUTSIDE_NONE
            case InsideLoopState.INSIDE_F, Tile.J:
                return InsideLoopState.OUTSIDE_NONE
            case InsideLoopState.INSIDE_F, Tile.S7:
                return InsideLoopState.INSIDE_NONE
            case InsideLoopState.INSIDE_NONE, Tile.V:
                return InsideLoopState.OUTSIDE_NONE
            case InsideLoopState.INSIDE_NONE, Tile.F:
                return InsideLoopState.INSIDE_F
            case InsideLoopState.INSIDE_NONE, Tile.L:
                return InsideLoopState.INSIDE_L
            case InsideLoopState.OUTSIDE_L, Tile.J:
                return InsideLoopState.OUTSIDE_NONE
            case InsideLoopState.OUTSIDE_L, Tile.S7:
                return InsideLoopState.INSIDE_NONE
            case InsideLoopState.OUTSIDE_F, Tile.J:
                return InsideLoopState.INSIDE_NONE
            case InsideLoopState.OUTSIDE_F, Tile.S7:
                return InsideLoopState.OUTSIDE_NONE
            case InsideLoopState.OUTSIDE_NONE, Tile.V:
                return InsideLoopState.INSIDE_NONE
            case InsideLoopState.OUTSIDE_NONE, Tile.F:
                return InsideLoopState.OUTSIDE_F
            case InsideLoopState.OUTSIDE_NONE, Tile.L:
                return InsideLoopState.OUTSIDE_L
            case _:
                return self


def main() -> None:
    print(farthest_tile(parse_lines(utils.read_input_lines(__file__))))
    print(tiles_inside_loop(parse_lines(utils.read_input_lines(__file__))))


if __name__ == "__main__":
    main()

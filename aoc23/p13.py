from __future__ import annotations

import dataclasses

from aoc23 import utils


@dataclasses.dataclass
class Pattern:
    rows: list[str]
    columns: list[str] = dataclasses.field(init=False)

    def __post_init__(self):
        self.columns = [
            "".join(self.rows[i][j] for i in range(len(self.rows)))
            for j in range(len(self.rows[0]))  # Assume a rectangle
        ]

    def summarize(self, smudges: int) -> int:
        column = symmetry_index(self.columns, smudges=smudges)
        row = symmetry_index(self.rows, smudges=smudges) if column == 0 else 0
        return column + row * 100


def symmetry_index(lines: list[str], *, smudges: int) -> int:
    """Return the zero-based index of the line symmetry in the given lines."""
    for i in range(len(lines) - 1):
        if is_symmetric(lines, i, smudges=smudges):
            return i + 1
    return 0


def is_symmetric(lines: list[str], index: int, *, smudges: int) -> bool:
    """Check if the lines are symmetric at a given index.

    Require the exact number of smudges to be present in the symmetric lines.
    """
    before = reversed(range(index + 1))
    after = range(index + 1, len(lines))
    found = 0
    for i, j in zip(before, after):
        for k in range(len(lines[i])):
            if lines[i][k] != lines[j][k]:
                found += 1
                if found > smudges:
                    return False
    return found == smudges


def summarize(patterns: list[Pattern], *, smudges: int) -> int:
    return sum([p.summarize(smudges) for p in patterns])


def parse_input(lines: list[str]) -> list[Pattern]:
    return [Pattern(section) for section in utils.split_by_empty_lines(lines)]


def main() -> None:
    print(summarize(parse_input(utils.read_input_lines(__file__)), smudges=0))
    print(summarize(parse_input(utils.read_input_lines(__file__)), smudges=1))


if __name__ == "__main__":
    main()

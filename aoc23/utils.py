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

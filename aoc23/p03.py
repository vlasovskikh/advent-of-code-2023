from __future__ import annotations
import itertools
import operator
import re
import typing

from aoc23 import utils


class Match(typing.NamedTuple):
    value: str
    line: int
    span: tuple[int, int]


def parse_input(lines: list[str]) -> list[str]:
    return lines


def sum_part_numbers(schematic: list[str]) -> int:
    return sum(sum(part_numbers(schematic, line)) for line in range(len(schematic)))


def sum_gear_ratios(schematic: list[str]) -> int:
    gear_like = sorted(
        (part, num)
        for line in range(len(schematic))
        for num, parts in numbers_to_parts(schematic, line).items()
        for part in parts
        if part.value == "*"
    )
    gear_nums = [
        [int(num.value) for _, num in g]
        for _, g_it in itertools.groupby(
            gear_like,
            key=operator.itemgetter(0),
        )
        if len(g := list(g_it)) == 2
    ]
    return sum(n1 * n2 for n1, n2 in gear_nums)


def part_numbers(schematic: list[str], line: int) -> list[int]:
    return [
        int(num.value)
        for num, parts in numbers_to_parts(schematic, line).items()
        if parts
    ]


def numbers_to_parts(schematic: list[str], line: int) -> dict[Match, list[Match]]:
    nums = [
        Match(value=m.group(), line=line, span=m.span())
        for m in re.finditer(r"\d+", schematic[line])
    ]
    return {num: parts(num, schematic) for num in nums}


def parts(num: Match, schematic: list[str]) -> list[Match]:
    start = max(num.span[0] - 1, 0)
    end = min(num.span[1] + 1, len(schematic[num.line]))
    return [
        Match(
            value=m.group(),
            line=line,
            span=(
                start + m.span()[0],
                start + m.span()[1],
            ),
        )
        for line in range(max(num.line - 1, 0), min(num.line + 2, len(schematic)))
        for m in re.finditer(r"[^\d.]", schematic[line][start:end])
    ]


def main() -> None:
    schematic = parse_input(utils.read_input_lines(__file__))
    print(sum_part_numbers(schematic))
    print(sum_gear_ratios(schematic))


if __name__ == "__main__":
    main()

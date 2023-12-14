from __future__ import annotations

import functools
import typing

from aoc23 import utils


class Record(typing.NamedTuple):
    springs: str
    groups: tuple[int, ...]

    @functools.cache
    def arrangements(
        self,
        pos: int = 0,
        group: int = 0,
        spent: int = 0,
    ) -> int:
        if pos == len(self.springs):
            if (group == len(self.groups) - 1 and spent == self.groups[group]) or (
                group == len(self.groups) and spent == 0
            ):
                return 1
            else:
                return 0
        res = 0
        s = self.springs[pos]
        if s in ".?":
            if spent == 0:
                res += self.arrangements(pos + 1, group, spent)
            elif spent == self.groups[group]:
                res += self.arrangements(pos + 1, group + 1, 0)
        if s in "#?":
            if group < len(self.groups) and spent < self.groups[group]:
                res += self.arrangements(pos + 1, group, spent + 1)
        return res


def sum_of_arrangements(records: list[Record]) -> int:
    result = 0
    for record in records:
        result += record.arrangements()
    return result


def unfold_records(records: list[Record]) -> list[Record]:
    return [
        Record(
            springs="?".join([r.springs] * 5),
            groups=r.groups * 5,
        )
        for r in records
    ]


def parse_input(lines: list[str]) -> list[Record]:
    return [parse_record(line) for line in lines]


def parse_record(line: str) -> Record:
    springs, sizes = line.split()
    return Record(
        springs=springs,
        groups=tuple(int(c) for c in sizes.split(",")),
    )


def main() -> None:
    records = parse_input(utils.read_input_lines(__file__))
    print(sum_of_arrangements(records))
    print(sum_of_arrangements(unfold_records(records)))


if __name__ == "__main__":
    main()

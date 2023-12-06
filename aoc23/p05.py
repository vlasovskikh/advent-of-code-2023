from __future__ import annotations
import functools
import itertools
import re
import typing

from aoc23 import utils


class IntSet(typing.NamedTuple):
    """Immutable set for ranges of integers."""

    ranges: tuple[range, ...]

    def __and__(self, other: IntSet) -> IntSet:
        intersections = (
            self._range_intersection(r1, r2)
            for r1 in self.ranges
            for r2 in other.ranges
        )
        return IntSet(tuple(filter(None, intersections)))

    def __add__(self, other: IntSet) -> IntSet:  # type: ignore[override]
        return IntSet(self.ranges + other.ranges)

    def __sub__(self, other: IntSet) -> IntSet:
        if not other:
            return IntSet(self.ranges)
        differences = [
            functools.reduce(
                IntSet.__and__,
                [IntSet(self._range_difference(r1, r2)) for r2 in other.ranges],
            )
            for r1 in self.ranges
        ]
        return functools.reduce(IntSet.__add__, filter(None, differences), IntSet(()))

    def __bool__(self) -> bool:
        return any(self.ranges)

    @classmethod
    def _range_intersection(cls, r1: range, r2: range) -> range | None:
        start = max(r1.start, r2.start)
        stop = min(r1.stop, r2.stop)
        if start < stop:
            return range(start, stop)
        else:
            return None

    @classmethod
    def _range_difference(cls, r1: range, r2: range) -> tuple[range, ...]:
        inter = cls._range_intersection(r1, r2)
        if not inter:
            return (r1,)

        if inter == r1:
            return ()
        elif inter.start == r1.start:
            return (range(inter.stop, r1.stop),)
        elif inter.stop == r1.stop:
            return (range(r1.start, inter.start),)
        else:
            return (
                range(r1.start, inter.start),
                range(inter.stop, r1.stop),
            )


class MapEntry(typing.NamedTuple):
    dst: int
    src: int
    length: int

    def to_int_set(self) -> IntSet:
        return IntSet((range(self.src, self.src + self.length),))

    @property
    def offset(self) -> int:
        return self.dst - self.src


class Map(typing.NamedTuple):
    src: str
    dst: str
    entries: list[MapEntry]

    def translate(self, int_set: IntSet) -> IntSet:
        intersections = {e.to_int_set() & int_set: e for e in self.entries}
        shifts = [self._shift(s, e.offset) for s, e in intersections.items()]
        remaining = functools.reduce(IntSet.__sub__, intersections.keys(), int_set)
        return functools.reduce(IntSet.__add__, shifts, remaining)

    @classmethod
    def _shift(cls, int_set: IntSet, offset: int) -> IntSet:
        result = tuple(range(r.start + offset, r.stop + offset) for r in int_set.ranges)
        return IntSet(result)


def min_location_for_seeds(seeds: list[int], maps: list[Map]) -> int:
    ranges = tuple(range(seed, seed + 1) for seed in seeds)
    return min_location_for_set(IntSet(ranges), maps)


def min_location_for_ranges(seeds: list[int], maps: list[Map]) -> int:
    ranges = tuple(
        range(start, start + length) for start, length in itertools.batched(seeds, 2)
    )
    return min_location_for_set(IntSet(ranges), maps)


def min_location_for_set(int_set: IntSet, maps: list[Map]) -> int:
    result = translate(int_set, src="seed", dst="location", maps=maps)
    starts = [r.start for r in result.ranges]
    return min(starts)


def translate(int_set: IntSet, src: str, dst: str, maps: list[Map]) -> IntSet:
    if src == dst:
        return int_set
    translate_map = next(m for m in maps if m.src == src)
    result = translate_map.translate(int_set)
    return translate(result, src=translate_map.dst, dst=dst, maps=maps)


def parse_input(lines: list[str]) -> tuple[list[int], list[Map]]:
    seeds_section, *map_sections = utils.split_by_empty_lines(lines)
    return parse_seeds(seeds_section), [parse_map(m) for m in map_sections]


def parse_seeds(section: list[str]) -> list[int]:
    line = section[0]
    m = re.match(r"seeds: (.*)", line)
    if not m:
        raise ValueError(f"Unknown seeds line: {line}")
    return [int(s) for s in m.group(1).split()]


def parse_map(section: list[str]) -> Map:
    header, *range_lines = section
    m = re.match(r"(.*)-to-(.*) map:", header)
    if not m:
        raise ValueError(f"Unknown map header: {header}")
    return Map(
        src=m.group(1),
        dst=m.group(2),
        entries=[parse_map_entry(line) for line in range_lines],
    )


def parse_map_entry(line: str) -> MapEntry:
    dst, src, length = line.split()
    return MapEntry(int(dst), int(src), int(length))


def main() -> None:
    seeds, maps = parse_input(utils.read_input_lines(__file__))
    print(min_location_for_seeds(seeds, maps))
    print(min_location_for_ranges(seeds, maps))


if __name__ == "__main__":
    main()

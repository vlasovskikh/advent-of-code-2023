import bisect
import functools
import operator
import typing

from aoc23 import utils


class Race(typing.NamedTuple):
    time: int
    distance: int

    def push(self, t: int) -> int:
        """Distance travelled after pushing the button for t ms."""

        return t * (self.time - t)


def total_ways_to_beat_record(races: list[Race]) -> int:
    ways = [ways_to_beat_record(race) for race in races]
    return functools.reduce(operator.mul, ways, 1)


def ways_to_beat_record(race: Race) -> int:
    times = range(race.time // 2 + 1)
    i = bisect.bisect_right(times, race.distance, key=race.push)
    extra = 1 if race.time % 2 == 1 else 0
    return len(times[i:]) * 2 - 1 + extra


def parse_input(lines: list[str]) -> list[Race]:
    times = parse_numbers(lines[0])
    distances = parse_numbers(lines[1])
    return [Race(t, d) for t, d in zip(times, distances)]


def fixed_parse_input(lines: list[str]) -> Race:
    return Race(
        time=parse_kerning_number(lines[0]),
        distance=parse_kerning_number(lines[1]),
    )


def parse_numbers(s: str) -> list[int]:
    _, rest = s.split(":", maxsplit=1)
    return [int(n) for n in rest.split()]


def parse_kerning_number(s: str) -> int:
    _, rest = s.split(":", maxsplit=1)
    return int(rest.replace(" ", ""))


def main() -> None:
    lines = utils.read_input_lines(__file__)
    print(total_ways_to_beat_record(parse_input(lines)))
    print(ways_to_beat_record(fixed_parse_input(lines)))


if __name__ == "__main__":
    main()

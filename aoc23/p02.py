import re
import typing

from aoc23 import utils


class Handful(typing.NamedTuple):
    red: int
    green: int
    blue: int

    def power(self) -> int:
        return self.red * self.green * self.blue


class Game(typing.NamedTuple):
    id: int
    handfuls: list[Handful]

    def is_possible(self, bag: Handful) -> bool:
        return all(
            h.red <= bag.red and h.green <= bag.green and h.blue <= bag.blue
            for h in self.handfuls
        )

    def smallest_bag(self) -> Handful:
        return Handful(
            red=max(h.red for h in self.handfuls),
            green=max(h.green for h in self.handfuls),
            blue=max(h.blue for h in self.handfuls),
        )


def sum_possible_games(games: list[Game]) -> int:
    bag = Handful(red=12, green=13, blue=14)
    return sum(game.id for game in games if game.is_possible(bag))


def sum_powers_of_smallest_bags(games: list[Game]) -> int:
    return sum(game.smallest_bag().power() for game in games)


def parse_input(lines: list[str]) -> list[Game]:
    return [parse_line(line) for line in lines]


def parse_line(line: str) -> Game:
    m = re.match(r"Game (\d+): (.*)", line)
    if not m:
        raise ValueError(f"Unknown format: {line}")
    return Game(
        id=int(m.group(1)),
        handfuls=[parse_handful(s) for s in m.group(2).split("; ")],
    )


def parse_handful(s: str) -> Handful:
    colors = dict(parse_color(c) for c in s.split(", "))
    return Handful(
        red=colors.get("red", 0),
        green=colors.get("green", 0),
        blue=colors.get("blue", 0),
    )


def parse_color(s: str) -> tuple[str, int]:
    n, c = s.split(" ")
    return c, int(n)


def main() -> None:
    games = parse_input(utils.read_input_lines(__file__))
    print(sum_possible_games(games))
    print(sum_powers_of_smallest_bags(games))


if __name__ == "__main__":
    main()

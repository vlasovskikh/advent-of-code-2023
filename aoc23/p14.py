from __future__ import annotations

import dataclasses

import numpy as np

from aoc23 import utils


@dataclasses.dataclass
class Platform:
    data: np.ndarray

    def __str__(self) -> str:
        return "\n".join("".join(line) for line in self.data)

    def spin(self, count: int) -> None:
        platforms: list[np.ndarray] = []
        index = 0
        for _ in range(count):
            platforms.append(self.data.copy())
            self.spin_cycle()
            found = False
            for index, platform in enumerate(platforms):
                if np.all(platform == self.data):
                    found = True
                    break
            if found:
                break
        else:
            return
        cycle = len(platforms) - index
        cycle_index = index + (count - index) % cycle
        self.data = platforms[cycle_index].copy()

    def north_load(self) -> int:
        lines, cols = self.data.shape
        weights = (np.arange(lines) + 1)[::-1]
        return np.sum((self.data == "O") * weights.reshape(lines, 1))

    def spin_cycle(self) -> None:
        self.tilt_north()
        self.tilt_west()
        self.tilt_south()
        self.tilt_east()

    def tilt_north(self) -> None:
        for line in np.rot90(self.data, 1):
            self.tilt_line(line)

    def tilt_east(self) -> None:
        for line in np.rot90(self.data, 2):
            self.tilt_line(line)

    def tilt_south(self) -> None:
        for line in np.rot90(self.data, 3):
            self.tilt_line(line)

    def tilt_west(self) -> None:
        for line in self.data:
            self.tilt_line(line)

    @classmethod
    def tilt_data(cls, data: np.ndarray) -> None:
        for line in data:
            cls.tilt_line(line)

    @staticmethod
    def tilt_line(line: np.ndarray) -> None:
        rock = False
        last = 0
        for i, x in enumerate(line):
            if rock and (x == "." or x == "O"):
                rock = False
                last = i
            if not rock and x == "#":
                rock = True
            if x == "O":
                if i != last:
                    line[last] = "O"
                    line[i] = "."
                last += 1


def load_after_spin(platform: Platform, count: int = 1_000_000_000) -> int:
    platform.spin(count)
    return platform.north_load()


def load_after_tilt_north(platform: Platform) -> int:
    platform.tilt_north()
    return platform.north_load()


def parse_lines(lines: list[str]) -> Platform:
    return Platform(np.array([list(line) for line in lines], dtype=str))


def main() -> None:
    platform = parse_lines(utils.read_input_lines(__file__))
    print(load_after_tilt_north(platform))
    print(load_after_spin(platform))


if __name__ == "__main__":
    main()

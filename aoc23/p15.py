import dataclasses
import re
import typing

from aoc23 import utils


class Lens(typing.NamedTuple):
    label: str
    number: int


@dataclasses.dataclass
class Box:
    lenses: list[Lens] = dataclasses.field(init=False, default_factory=list)
    labels: dict[str, Lens] = dataclasses.field(init=False, default_factory=dict)

    def dash(self, label: str) -> None:
        existing = self.labels.get(label)
        if existing is None:
            return
        index = self.lenses.index(existing)
        self.lenses.pop(index)
        del self.labels[label]

    def equals(self, label: str, number: int) -> None:
        new = Lens(label, number)
        existing = self.labels.get(label)
        if existing is None:
            self.lenses.append(new)
            self.labels[label] = new
        else:
            index = self.lenses.index(existing)
            self.lenses.pop(index)
            self.lenses.insert(index, new)
            self.labels[label] = new


STEP_RE = re.compile(r"([a-z]+)([\-=])([0-9]*)")


@dataclasses.dataclass
class Step:
    string: str
    label: str = dataclasses.field(init=False)
    op: str = dataclasses.field(init=False)
    arg: int | None = None

    def __post_init__(self):
        m = STEP_RE.match(self.string)
        if m is None:
            raise ValueError(f"Failed to parse {self.string!r}")
        self.label = m.group(1)
        self.op = m.group(2)
        arg = m.group(3)
        if arg:
            self.arg = int(arg)


def hash_string(s: str) -> int:
    res = 0
    for c in s:
        res += ord(c)
        res *= 17
        res %= 256
    return res


@dataclasses.dataclass
class Initialization:
    boxes: list[Box] = dataclasses.field(init=False)

    def __post_init__(self) -> None:
        self.boxes = [Box() for _ in range(256)]

    def run(self, steps: list[Step]) -> None:
        for step in steps:
            box = self.boxes[hash_string(step.label)]
            match step.op:
                case "-":
                    box.dash(step.label)
                case "=":
                    if step.arg is None:
                        raise ValueError(f"Empty argument for {step}")
                    box.equals(step.label, step.arg)

    def focusing_power(self) -> int:
        res = 0
        for i, box in enumerate(self.boxes):
            for j, lens in enumerate(box.lenses):
                res += (i + 1) * (j + 1) * lens.number
        return res


def focusing_power(steps: list[Step]) -> int:
    init = Initialization()
    init.run(steps)
    return init.focusing_power()


def sum_step_hashes(steps: list[Step]) -> int:
    return sum([hash_string(step.string) for step in steps])


def parse_lines(lines: list[str]) -> list[Step]:
    line = lines[0]
    return [Step(s) for s in line.split(",")]


def main() -> None:
    steps = parse_lines(utils.read_input_lines(__file__))
    print(sum_step_hashes(steps))
    print(focusing_power(steps))


if __name__ == "__main__":
    main()

import itertools
import math
import re
import typing

from aoc23 import utils


Instruction = typing.Literal["L", "R"]
Node = str


class Fork(typing.NamedTuple):
    left: Node
    right: Node

    def follow(self, instruction: Instruction) -> Node:
        match instruction:
            case "L":
                return self.left
            case "R":
                return self.right
            case _:
                raise ValueError(f"Unkonwn instruciton: {instruction!r}")


class Map(typing.NamedTuple):
    instructions: list[Instruction]
    nodes: dict[Node, Fork]

    def navigate(self, start: Node) -> typing.Iterator[Node]:
        node = start
        for i in itertools.count():
            instruction = self.instructions[i % len(self.instructions)]
            node = self.nodes[node].follow(instruction)
            yield node


def count_steps(map: Map) -> int:
    path = itertools.takewhile(lambda node: node != "ZZZ", map.navigate("AAA"))
    return sum(1 for _ in path) + 1


def count_ghost_steps(map: Map) -> int:
    starts = [node for node in map.nodes if node.endswith("A")]
    endless_paths = [map.navigate(node) for node in starts]
    paths_to_z = [
        itertools.takewhile(lambda node: not node.endswith("Z"), path)
        for path in endless_paths
    ]
    periods = [sum(1 for _ in path) + 1 for path in paths_to_z]
    gcd = math.gcd(*periods)
    return math.prod(p // gcd for p in periods) * gcd


def parse_input(lines: list[str]) -> Map:
    return Map(
        instructions=[typing.cast(Instruction, s) for s in lines[0]],
        nodes=dict(parse_node(line) for line in lines[2:]),
    )


def parse_node(line: str) -> tuple[Node, Fork]:
    m = re.match(r"(\w{3}) = \((\w{3}), (\w{3})\)", line)
    if not m:
        raise ValueError(f"Unknown line: {line!r}")
    return m.group(1), Fork(left=m.group(2), right=m.group(3))


def main() -> None:
    map = parse_input(utils.read_input_lines(__file__))
    print(count_steps(map))
    print(count_ghost_steps(map))


if __name__ == "__main__":
    main()

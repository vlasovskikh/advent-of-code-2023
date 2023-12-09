from aoc23 import utils


def extrapolate_forwards(dataset: list[int]) -> int:
    seqs = diff_sequences(dataset)
    for i in range(len(seqs) - 1, 0, -1):
        new_value = seqs[i][-1] + seqs[i - 1][-1]
        seqs[i - 1].append(new_value)
    return seqs[0][-1]


def extrapolate_backwards(dataset: list[int]) -> int:
    seqs = diff_sequences(dataset)
    for i in range(len(seqs) - 1, 0, -1):
        new_value = seqs[i - 1][0] - seqs[i][0]
        seqs[i - 1].insert(0, new_value)
    return seqs[0][0]


def diff_sequences(dataset: list[int]) -> list[list[int]]:
    seqs = [dataset.copy()]
    seq = seqs[0]
    while not all(x == 0 for x in seq):
        seq = differentiate(seq)
        seqs.append(seq)
    return seqs


def differentiate(dataset: list[int]) -> list[int]:
    sliding_pairs = utils.sliding_window(dataset, 2)
    return [x2 - x1 for x1, x2 in sliding_pairs]


def sum_extrapolated_values(datasets: list[list[int]], forwards: bool) -> int:
    f = extrapolate_forwards if forwards else extrapolate_backwards
    return sum(f(dataset) for dataset in datasets)


def parse_lines(lines: list[str]) -> list[list[int]]:
    return [parse_line(line) for line in lines]


def parse_line(line: str) -> list[int]:
    return [int(s) for s in line.split()]


def main() -> None:
    datasets = parse_lines(utils.read_input_lines(__file__))
    print(sum_extrapolated_values(datasets, forwards=True))
    print(sum_extrapolated_values(datasets, forwards=False))


if __name__ == "__main__":
    main()

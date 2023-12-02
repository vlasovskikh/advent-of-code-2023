import re
import typing

from aoc23 import utils


DIGITS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def sum_calibration_values(lines: list[str], digits: list[str]) -> int:
    # CPU = O(n), memory = O(n)
    forward_re = re.compile("|".join(digits))
    backward_re = re.compile("|".join(s[::-1] for s in digits))
    return sum(
        calibration_value(
            line,
            forward_re=forward_re,
            backward_re=backward_re,
        )
        for line in lines
    )


def sum_only_digits(lines: list[str]) -> int:
    return sum_calibration_values(lines, digits=list(DIGITS.values()))


def sum_all_digits(lines: list[str]) -> int:
    all_digits = list(DIGITS.keys()) + list(DIGITS.values())
    return sum_calibration_values(lines, digits=all_digits)


def parse_input(lines: list[str]) -> list[str]:
    return lines


def calibration_value(
    s: str,
    forward_re: typing.Pattern[str],
    backward_re: typing.Pattern[str],
) -> int:
    first = to_digit(search_number(s, forward_re))
    last = to_digit(search_number(s[::-1], backward_re)[::-1])
    return int(first + last)


def search_number(s: str, regexp: typing.Pattern[str]) -> str:
    m = regexp.search(s)
    if not m:
        raise ValueError(f"No number found in {s!r}")
    return to_digit(m.group())


def to_digit(s: str) -> str:
    return DIGITS.get(s, s)


def main() -> None:
    lines = parse_input(utils.read_input_lines(__file__))
    print(sum_only_digits(lines))
    print(sum_all_digits(lines))


if __name__ == "__main__":
    main()

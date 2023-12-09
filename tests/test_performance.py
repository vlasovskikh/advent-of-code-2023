import pathlib
import statistics
import subprocess
import sys
import time

import plotext
import pytest
import aoc23


@pytest.fixture(scope="session")
def puzzle_runs() -> dict[str, float]:
    return run_puzzles()


def run_puzzles():
    return {path.stem: running_time(path) for path in puzzle_paths()}


def puzzle_paths() -> list[pathlib.Path]:
    return sorted(pathlib.Path(aoc23.__file__).parent.glob("p*.py"))


def running_time(path: pathlib.Path) -> float:
    t = time.perf_counter()
    module_name = f"{aoc23.__name__}.{path.stem}"
    print(f"Running python -m {module_name}...")
    subprocess.call([sys.executable, "-m", module_name])
    return time.perf_counter() - t


@pytest.mark.parametrize(
    "puzzle",
    [path.stem for path in puzzle_paths()],
)
def test_benchmark(puzzle: str, puzzle_runs: dict[str, float]) -> None:
    if len(puzzle_runs) < 2:
        return
    times = puzzle_runs.values()
    no_outliers = {
        p: t
        for p, t in puzzle_runs.items()
        if abs(t - statistics.mean(times)) <= statistics.stdev(times)
    }
    if len(no_outliers) < 2:
        return
    mean = statistics.mean(no_outliers.values())
    t = puzzle_runs[puzzle]
    limit = mean * 10
    if t > limit:
        show_times_plot(puzzle_runs)
        pytest.fail(
            f"Time limit exceeded for {puzzle!r}: "
            f"time: {t:.3f}, limit: {limit:.3f}, mean: {mean:.3f}"
        )


def show_times_plot(runs: dict[str, float]) -> None:
    run_items = sorted(runs.items())
    names = [name for name, _ in run_items]
    times = [value for _, value in run_items]
    plotext.simple_bar(names, times, title="Run Times")
    plotext.show()


def main() -> None:
    show_times_plot(run_puzzles())


if __name__ == "__main__":
    main()

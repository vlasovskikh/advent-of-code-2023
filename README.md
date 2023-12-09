# advent-of-code-2023

Having winter fun with Advent of Code 2023 ☃️


```shell
$ poetry run pre-commit run -av
black....................................................................Passed
- hook id: black
- duration: 0.18s

All done! ✨ 🍰 ✨
21 files left unchanged.

flake8...................................................................Passed
- hook id: flake8
- duration: 0.25s
mypy.....................................................................Passed
- hook id: mypy
- duration: 0.21s

Success: no issues found in 21 source files

pytest...................................................................Passed
- hook id: pytest
- duration: 0.35s

============================= test session starts ==============================
platform darwin -- Python 3.12.0, pytest-7.4.3, pluggy-1.3.0
configfile: pytest.ini
collected 46 items / 9 deselected / 37 selected

tests/test_p01.py ..                                                     [  5%]
tests/test_p02.py ..                                                     [ 10%]
tests/test_p03.py ..                                                     [ 16%]
tests/test_p04.py ..                                                     [ 21%]
tests/test_p05.py ..                                                     [ 27%]
tests/test_p06.py .....                                                  [ 40%]
tests/test_p07.py .................                                      [ 86%]
tests/test_p08.py ...                                                    [ 94%]
tests/test_p09.py ..                                                     [100%]

======================= 37 passed, 9 deselected in 0.03s =======================

performance..............................................................Passed
- hook id: performance
- duration: 0.63s

============================= test session starts ==============================
platform darwin -- Python 3.12.0, pytest-7.4.3, pluggy-1.3.0
configfile: pytest.ini
collected 46 items / 37 deselected / 9 selected

tests/test_performance.py .........
────────────────────────────────── Run Times ───────────────────────────────────
p01 ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 0.02
p02 ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 0.02
p03 ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 0.03
p04 ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 0.03
p05 ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 0.03
p06 ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 0.02
p07 ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 0.05
p08 ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 0.05
p09 ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 0.03


======================= 9 passed, 37 deselected in 0.31s =======================
```
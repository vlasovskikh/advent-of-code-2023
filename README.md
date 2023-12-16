# advent-of-code-2023

Having winter fun with Advent of Code 2023 ☃️


```shell
$ poetry run pre-commit run -av
black....................................................................Passed
- hook id: black
- duration: 0.57s

All done! ✨ 🍰 ✨
33 files left unchanged.

flake8...................................................................Passed
- hook id: flake8
- duration: 0.44s
mypy.....................................................................Passed
- hook id: mypy
- duration: 1.81s

Success: no issues found in 33 source files

pytest...................................................................Passed
- hook id: pytest
- duration: 1.54s

============================= test session starts ==============================
platform linux -- Python 3.12.1, pytest-7.4.3, pluggy-1.3.0
rootdir: /home/runner/work/advent-of-code-2023/advent-of-code-2023
configfile: pytest.ini
collecting ... 
collecting 82 items                                                            
collected 82 items / 15 deselected / 67 selected                               

tests/test_p01.py ..                                                     [  2%]
tests/test_p02.py ..                                                     [  5%]
tests/test_p03.py ..                                                     [  8%]
tests/test_p04.py ..                                                     [ 11%]
tests/test_p05.py ..                                                     [ 14%]
tests/test_p06.py .....                                                  [ 22%]
tests/test_p07.py .................                                      [ 47%]
tests/test_p08.py ...                                                    [ 52%]
tests/test_p09.py ..                                                     [ 55%]
tests/test_p10.py ....                                                   [ 61%]
tests/test_p11.py ..                                                     [ 64%]
tests/test_p12.py .......                                                [ 74%]
tests/test_p13.py ..                                                     [ 77%]
tests/test_p14.py .............                                          [ 97%]
tests/test_p15.py ..                                                     [100%]

====================== 67 passed, 15 deselected in 0.70s =======================

performance..............................................................Passed
- hook id: performance
- duration: 6.37s

============================= test session starts ==============================
platform linux -- Python 3.12.1, pytest-7.4.3, pluggy-1.3.0
rootdir: /home/runner/work/advent-of-code-2023/advent-of-code-2023
configfile: pytest.ini
collecting ... 
collected 82 items / 67 deselected / 15 selected                               

tests/test_performance.py ...............
────────────────────────────────── Run Times ───────────────────────────────────
p01 ▇ 0.04
p02 ▇ 0.04
p03 ▇ 0.06
p04 ▇▇ 0.07
p05 ▇ 0.06
p06 ▇ 0.04
p07 ▇▇ 0.09
p08 ▇▇ 0.09
p09 ▇ 0.06
p10 ▇▇▇▇▇▇▇ 0.29
p11 ▇▇▇▇▇▇▇▇▇▇ 0.44
p12 ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 1.1
p13 ▇ 0.05
p14 ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 3.06
p15 ▇ 0.05


====================== 15 passed, 67 deselected in 5.76s =======================
```
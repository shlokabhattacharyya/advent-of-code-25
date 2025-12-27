# Advent of Code 2025: Solutions

Below are my Python solutions for the Advent of Code event in 2025! I started late this year so it is currently a work in progress.

|Day|Name|Brief Explanation|Solution|
|-|-|-|-|
|Day 01|[Secret Entrance](https://adventofcode.com/2025/day/1)|Can you count how many times a rotating safe dial lands on or passes by zero?|[`day01.py`](./day01.py)|
|Day 02|[Gift Shop](https://adventofcode.com/2025/day/2)|Can you find and add up all of the twice-repeated numbers within given ranges?|[`day02.py`](./day02.py)|
|Day 03|[Lobby](https://adventofcode.com/2025/day/3)|Can you find the maximum integer made up by non-consecutive digits within a number without rearranging the digits?|[`day03.py`](./day03.py)|
|Day 04|[Printing Department](https://adventofcode.com/2025/day/4)|Can you find grid positions with fewer than four adjacent cells and calculate the total amount removable?|[`day04.py`](./day04.py)|
|Day 05|[Cafeteria](https://adventofcode.com/2025/day/5)|Can you filter a list of numbers by checking if they fall within given ranges and count the total unique numbers covered by those ranges?|[`day05.py`](./day05.py)|

To try solve all problems, run:

```py
python3 main.py
```

To run one day individually, run:

```py
python3 dayN.py
```

## Layout
The input data for each day lives in [`data/inputX.txt`](./data) where `X` is the day number. The functions in [`utils.py`](./utils.py) provide convience functions for looking up and parsing the input data.

Each `dayN.py` file defines two functions `part1()` and `part2` along with a global `answers` variable which is an array that looks like

```
answers = [
    [part1, 123],
    [part2, 456],
]
```

This is then imported into [`main.py`](main.py) where the two functions are run, timed and compared against what's expected. [`day_template.py`](day_template.py) is just a template for copying and pasting each day all the scaffolding.
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Advent of Code 2020, day one."""

INPUT_FILE = 'data/day_01.txt'


def main() -> None:
    """Accounting report repair."""
    with open(INPUT_FILE, encoding='utf-8') as input_file:
        numbers = [int(line.strip()) for line in input_file]

    target = 2020
    for number_1 in numbers:
        number_2 = target - number_1
        if number_2 in numbers:
            print(f'Part One: Product of two numbers that sum 2020: '
                  f'{number_1 * number_2}')
            break

    for number_1 in numbers:
        target = 2020 - number_1
        for number_2 in numbers:
            number_3 = target - number_2
            if number_3 in numbers:
                print(f'Part Two: Product of three numbers that sum 2020: '
                      f'{number_1 * number_2 * number_3}')
                return


main()

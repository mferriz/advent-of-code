#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Advent of Code 2022, day one."""

from typing import List

INPUT_FILE = 'data/day_01.txt'


def main() -> None:
    """Print calories carried by elves with a special criteria."""
    elf_calories: List[int] = []
    with open(INPUT_FILE, encoding='utf-8') as input_file:
        calories: int = 0
        for line in input_file:
            if (line := line.strip()):
                calories += int(line)
            else:
                elf_calories.append(calories)
                calories = 0
    # Sort the list
    elf_calories.sort(reverse=True)
    print(f'Part One: Most calories carried by an elf: {elf_calories[0]}')
    top_three = sum(elf_calories[0:3])
    print(f'Part Two: Calories carried by top three elves: {top_three}')


main()

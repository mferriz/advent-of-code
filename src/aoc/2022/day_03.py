#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Advent of Code 2022, day three."""

INPUT_FILE = 'data/day_03.txt'
PRIORITY = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main() -> None:
    """Calculate sum of priorities."""
    sum_of_priorities = 0
    sum_of_badge_priorities = 0
    group_rucksack = ['', '', '']
    with open(INPUT_FILE, encoding='utf-8') as input_file:
        for rucksack_number, rucksack in enumerate(input_file):
            rucksack = rucksack.strip()
            group_rucksack[rucksack_number % 3] = set(rucksack)
            half_length = len(rucksack) // 2
            compartment_1 = set(rucksack[:half_length])
            compartment_2 = set(rucksack[half_length:])
            item_shared = (compartment_1 & compartment_2).pop()
            sum_of_priorities += PRIORITY.index(item_shared) + 1
            if rucksack_number % 3 == 2:
                badge = (
                    group_rucksack[0] & group_rucksack[1] & group_rucksack[2]
                ).pop()
                sum_of_badge_priorities += PRIORITY.index(badge) + 1

    print(f'Part One: Sum of priorities: {sum_of_priorities}')
    print(f'Part Two: Sum of badge priorities: {sum_of_badge_priorities}')


main()

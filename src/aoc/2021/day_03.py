#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Advent of Code 2021, day three."""

import copy
from typing import List, Tuple

BITS = 12
INPUT_FILE = 'data/day_03.txt'


def parse_input(filename: str) -> List[int]:
    """Parse input file and return a list of tuples of commands and units."""
    diagnostics: List[int] = []
    with open(filename, encoding='utf-8') as input_file:
        for line in input_file:
            diagnostics.append(int(line.strip(), 2))
    return diagnostics


def obtain_power_consumption(diagnostics: List[int]) -> Tuple[int, int]:
    """Obtain the power consumption."""
    gamma_rate: int = 0
    epsilon_rate: int = 0

    for bit_count in range(BITS):
        bit_number = 1 << bit_count
        one_count = 0
        zero_count = 0
        for reading in diagnostics:
            if reading & bit_number:
                one_count += 1
            else:
                zero_count += 1
        if one_count > zero_count:
            gamma_rate = gamma_rate | bit_number
        else:
            epsilon_rate = epsilon_rate | bit_number
    return gamma_rate, epsilon_rate


def debug_diags(diagnostics: List[int]) -> None:
    """Print diagnostics report."""
    for reading in diagnostics:
        print(f'{reading:012b} ({reading})')
    print('')


def obtain_rating(diagnostics: List[int],
                  is_oxygen: bool) -> int:
    """Obtain the oxygen generator rating or CO2 scrubber rating."""
    working_numbers: List[int] = copy.deepcopy(diagnostics)

    for bit_place in range(BITS - 1, -1, -1):
        bit: int = 1 << bit_place
        one_numbers: List[int] = []
        zero_numbers: List[int] = []
        if len(working_numbers) == 1:
            return working_numbers[0]
        if len(working_numbers) == 2:
            if is_oxygen:
                return working_numbers[0] if working_numbers[0] & bit \
                    else working_numbers[1]
            return working_numbers[1] if working_numbers[0] & bit \
                else working_numbers[0]
        for reading in working_numbers:
            if reading & bit:
                one_numbers.append(reading)
            else:
                zero_numbers.append(reading)
        if len(one_numbers) >= len(zero_numbers):
            working_numbers = one_numbers if is_oxygen else zero_numbers
        else:
            working_numbers = zero_numbers if is_oxygen else one_numbers
    return -1


def main() -> None:
    """Print horizontal position and depth."""
    diagnostics: List[int] = parse_input(INPUT_FILE)
    gamma_rate, epsilon_rate = obtain_power_consumption(diagnostics)
    print(f'Part 1: Power consumption: {gamma_rate * epsilon_rate}')
    oxygen = obtain_rating(diagnostics, is_oxygen=True)
    co2 = obtain_rating(diagnostics, is_oxygen=False)
    print(f'Part 2: Life support rating: {oxygen * co2}')


main()

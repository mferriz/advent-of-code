#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Advent of Code 2021, day seven."""

from typing import List

import numpy


INPUT_FILE = 'data/day_07.txt'


def calculate_least_fuel(crabs: List[int], linear_cost: bool) -> int:
    """Calculate least amount of fuel."""
    max_number: int = max(crabs)
    least_fuel: int = -1

    work_crabs = numpy.asarray(crabs, dtype=int)
    for reference in range(max_number + 1):
        steps = numpy.abs(work_crabs - reference)
        if linear_cost:
            cost = steps
        else:
            cost = numpy.array([(step * (step + 1)) // 2 for step in steps])
        fuel = numpy.sum(cost, dtype=int)
        if not reference or fuel < least_fuel:
            least_fuel = fuel
    return least_fuel


def main() -> None:
    """Count lanterfishes after eighty days."""
    with open(INPUT_FILE, encoding='utf-8') as input_file:
        crabs = [int(x) for x in input_file.readline().strip().split(',')]
        least_fuel = calculate_least_fuel(crabs, linear_cost=True)
        print(f'Part One: Least fuel: {least_fuel}')
        least_fuel = calculate_least_fuel(crabs, linear_cost=False)
        print(f'Part Two: Least fuel: {least_fuel}')


main()

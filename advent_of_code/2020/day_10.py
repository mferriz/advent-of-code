#!/usr/bin/env python

"""Day 10 of the Advent of Code 2021."""

import copy
from typing import List

INPUT_FILE = 'data/day_10.txt'

chain_cache = {}


def count_chains(current_joltage: int, adapter_joltages: List[int]) -> int:
    """Count the number of chains."""
    global chain_cache

    if current_joltage in chain_cache:
        return chain_cache[current_joltage]

    if not adapter_joltages:
        counter = 1
    else:
        counter = 0
        for adapter_joltage in adapter_joltages:
            if adapter_joltage - current_joltage <= 3:
                new_adapters = copy.deepcopy(adapter_joltages)
                new_adapters.remove(adapter_joltage)
                counter += count_chains(adapter_joltage, new_adapters)
    chain_cache[current_joltage] = counter
    return counter


def main() -> None:
    """Program that finds joltage chain."""
    with open(INPUT_FILE, encoding='utf-8') as input_file:
        adapter_joltages = sorted([int(x.strip()) for x in input_file])

    # Add device built-in joltage.
    adapter_joltages.append(adapter_joltages[-1] + 3)

    one_jolt_difference = 0
    three_jolt_difference = 0
    current_joltage = 0
    for adapter_joltage in adapter_joltages:
        difference = adapter_joltage - current_joltage
        if difference == 1:
            one_jolt_difference += 1
        elif difference == 3:
            three_jolt_difference += 1
        current_joltage = adapter_joltage
    print(f'Part One: One jolt difference multiplied by three jolt '
          f'difference: {one_jolt_difference * three_jolt_difference}')
    print(f'Part Two: Distinct ways to connect adapters: '
          f'{count_chains(0, adapter_joltages)}')


main()

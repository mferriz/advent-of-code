#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Advent of Code 2021, day six."""

from typing import List

INPUT_FILE = 'data/day_06.txt'


def parse_input(filename: str) -> List[int]:
    """Parse filename and return a list of integers."""
    # Nine possible values as timers, 0 to 8 inclusive.
    timers: List[int] = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    with open(filename, encoding='utf-8') as input_file:
        line = input_file.readline().strip()
        for number_str in line.split(','):
            timers[int(number_str)] += 1
    return timers


def simulate_day_activity(timers: List[int]) -> List[int]:
    """Decrement timer for all lantern fishes."""
    zeros: int = timers[0]
    timers = timers[1:]   # Shift numbers. Acting as subtraction of timers.
    timers.append(zeros)  # Add new generation
    timers[6] += zeros    # Restart timers for the ones that reached zero.
    return timers


def main() -> None:
    """Count lanterfishes after eighty days."""
    timers = parse_input(INPUT_FILE)
    for day in range(1, 257):
        timers = simulate_day_activity(timers)
        if day == 80:
            print(f'Part One: Number of lantern fishes: {sum(timers)}')
    print(f'Part Two: Number of lantern fishes: {sum(timers)}')


main()

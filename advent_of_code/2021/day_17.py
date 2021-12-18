#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Advent of Code 2021, day seventeen."""

import re
from typing import Optional

MAX_ITER = 250
INPUT_FILE = 'data/day_17.txt'
INPUT_RE = re.compile(r'target area:\sx=(\d+)\.\.(\d+),\s'
                      r'y=(-?\d+)\.\.(-?\d+)')

def simulate(x: int, y: int, target_x_range, target_y_range) -> Optional[int]:
    """Simulate"""
    i = 0
    j = 0
    max_height = 0
    for _ in range(MAX_ITER):
        # print(f'{i}, {j}, {target_x_range}, {target_y_range}')
        if i in target_x_range and j in target_y_range:
            return max_height
        i += x
        x = max(0, x - 1)
        j += y
        y -= 1
        max_height = max(max_height, j)
    return None

def main() -> None:
    """Shooting."""
    with open(INPUT_FILE, encoding='utf-8') as input_file:
        match = INPUT_RE.match(input_file.readline().strip())
        target_x_0 = int(match.group(1))
        target_x_1 = int(match.group(2))
        target_y_0 = int(match.group(3))
        target_y_1 = int(match.group(4))
        target_x_range = range(int(match.group(1)),
                               int(match.group(2)) + 1)
        target_y_range = range(int(match.group(3)),
                               int(match.group(4)) + 1)

        # Preserving this way for calculating max height.
        # However this can be also found in calculation of part two.
        max_height = 0
        for n in range(0, MAX_ITER):
            height = n * (n + 1) // 2  # Rising

            height_prime_min = height - target_y_1
            height_prime_max = height - target_y_0
            for m in range(0, 1000):
                height_prime = m * (m + 1) // 2  # Falling
                if height_prime_min <= height_prime <= height_prime_max:
                    #print(f'Found N={n}, M={m}, height={height}, '
                    #      f'Height prime={height_prime}')
                    max_height = height

        print(f'Part One: Maximum height: {max_height}')

        solutions = []
        max_height = 0
        for x in range(-MAX_ITER, MAX_ITER):
            for y in range(-MAX_ITER, MAX_ITER):
                height = simulate(x, y, target_x_range, target_y_range)
                if height is not None:
                    max_height = max(max_height, height)
                    solutions.append((x, y))
        print(f'Part Two: Permutations of velocities that reach target: '
              f'{len(solutions)}')
    
main()

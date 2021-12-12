#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Advent of Code 2021, day one."""

from typing import List, Optional

INPUT_FILE = 'data/day_01.txt'


def get_sliding_window_depths(depths: List[int]) -> List[int]:
    """Get sliding windows depths."""
    new_depths: List[int] = []
    index: int = 0

    while index < len(depths) - 2:
        sliding_depth = \
            depths[index] + depths[index + 1] + depths[index + 2]
        new_depths.append(sliding_depth)
        index += 1
    return new_depths


def calculate_increases(depths: List[int]) -> int:
    """Calculate the number of depth increases."""
    previous: Optional[int] = None
    depth_increase: int = 0

    for depth in depths:
        if previous is not None and depth > previous:
            depth_increase += 1
        previous = depth
    return depth_increase


def main() -> None:
    """Print number of changes."""
    depths: List[int] = []
    with open(INPUT_FILE, encoding='utf-8') as input_file:
        for line in input_file:
            depths.append(int(line.strip()))
    print(f'Part 1: Count of measurements larger than previous: '
          f'{calculate_increases(depths)}')
    print(f'Part 2: Count of measurements larger than previous: '
          f'{calculate_increases(get_sliding_window_depths(depths))}')


main()

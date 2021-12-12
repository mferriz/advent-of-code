#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Advent of Code 2021, day two."""

from typing import List, Tuple

INPUT_FILE = 'data/day_02.txt'


def navigate_part_one(commands: List[Tuple[str, int]]) -> Tuple[int, int]:
    """Navigate and return the horizontal position and depth."""
    horizontal: int = 0
    depth: int = 0
    for command, units in commands:
        if command == 'forward':
            horizontal += units
        elif command == 'down':
            depth += units
        elif command == 'up':
            depth -= units
    return horizontal, depth


def navigate_part_two(commands: List[Tuple[str, int]]) -> Tuple[int, int]:
    """Navigate and return the horizontal position and depth."""
    horizontal: int = 0
    depth: int = 0
    aim: int = 0

    for command, units in commands:
        if command == 'forward':
            horizontal += units
            depth += aim * units
        elif command == 'down':
            aim += units
        elif command == 'up':
            aim -= units
    return horizontal, depth


def main() -> None:
    """Print horizontal position and depth."""
    commands: List[Tuple[str, int]] = []
    with open(INPUT_FILE, encoding='utf-8') as input_file:
        for line in input_file:
            command, units = line.strip().split(' ')
            commands.append((command, int(units)))
    horizontal, depth = navigate_part_one(commands)
    print(f'Part 1: Multiplication of horizontal and depth: '
          f'{horizontal * depth}')
    horizontal, depth = navigate_part_two(commands)
    print(f'Part 2: Multiplication of horizontal and depth: '
          f'{horizontal * depth}')


main()

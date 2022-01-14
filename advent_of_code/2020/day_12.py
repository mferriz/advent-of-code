#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Advent of Code 2020, day twelve."""

from typing import List, Tuple

INPUT_FILE = 'data/day_12.txt'


def part_one_navigation(navigation: List[Tuple[str, int]]) -> None:
    """Navigate according to part one instructions."""
    turn = {'N': ('E', 'W'), 'S': ('W', 'E'), 'E': ('S', 'N'), 'W': ('N', 'S')}
    facing = 'E'
    ship = {'N': 0, 'S': 0, 'E': 0, 'W': 0}
    for action, value in navigation:
        if action in {'R', 'L'}:
            for _ in range(value // 90):
                facing = turn[facing][0 if action == 'R' else 1]
            continue
        if action == 'F':
            action = facing
        ship[action] += value
    distance = abs(ship['N'] - ship['S']) + abs(ship['E'] - ship['W'])
    print(f'Part One: Manhattan distance: {distance}')


def part_two_navigation(navigation: List[Tuple[str, int]]) -> None:
    """Navigate according to part two instructions."""
    waypoint = {'E': 10, 'N': 1}
    ship = {'E': 0, 'N': 0}
    opposite = {'S': 'N', 'W': 'E'}
    for action, value in navigation:
        if action == 'F':
            ship['N'] += waypoint['N'] * value
            ship['E'] += waypoint['E'] * value
        elif action in {'N', 'E'}:
            waypoint[action] += value
        elif action in {'S', 'W'}:
            waypoint[opposite[action]] -= value
        elif action in {'R', 'L'}:
            for _ in range(value // 90):
                waypoint = {
                    'E': waypoint['N'] if action == 'R' else -waypoint['N'],
                    'N': waypoint['E'] if action == 'L' else -waypoint['E']
                }
    distance = abs(ship['N']) + abs(ship['E'])
    print(f'Part Two: Manhattan distance: {distance}')


def main() -> None:
    """Solve problem of Advent of code, year 2020, day 12."""
    with open(INPUT_FILE, encoding='utf-8') as input_file:
        navigation = [(line[0], int(line[1:-1])) for line in input_file]
    part_one_navigation(navigation)
    part_two_navigation(navigation)


main()

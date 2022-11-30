#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Advent of Code 2020, day eleven."""

from typing import List

INPUT_FILE = 'data/day_11.txt'


def occupied_in_axis(seating: List[List[str]], row: int, col: int,
                     delta_row: int, delta_col: int, recurse: bool) -> int:
    """Find if there is an occupied seat in an axis."""
    row += delta_row
    col += delta_col
    occupied = 0

    if 0 <= row < len(seating) and 0 <= col < len(seating[0]):
        if seating[row][col] == '#':
            occupied = 1
        elif seating[row][col] == '.' and recurse:
            occupied = (
                occupied_in_axis(seating, row, col, delta_row, delta_col,
                                 recurse)
            )
    return occupied


def adjacent_occupied(seating: List[List[str]], row: int, col: int,
                      recurse: bool) -> int:
    """Find the number of occupied seats for part two."""
    occupied = 0
    for delta_row in range(-1, 2):
        for delta_col in range(-1, 2):
            if delta_row or delta_col:
                occupied += occupied_in_axis(seating, row, col,
                                             delta_row, delta_col, recurse)
    return occupied


def occupation_simulation(seating: List[List[str]],
                          part: str) -> List[str]:
    """Perform occupation simulation until there are no more changes."""
    threshold = 4 if part == 'one' else 5
    work_seating = [seating[x] for x in range(len(seating))]
    while True:
        new_seating = (
            [list('.' * len(seating[0])) for _ in range(len(seating))]
        )
        for row, _ in enumerate(work_seating):
            for col, _ in enumerate(work_seating[0]):
                if work_seating[row][col] == 'L':
                    occupied = adjacent_occupied(work_seating, row, col,
                                                 part == 'two')
                    new_seating[row][col] = 'L' if occupied else '#'
                elif work_seating[row][col] == '#':
                    occupied = adjacent_occupied(work_seating, row, col,
                                                 part == 'two')
                    new_seating[row][col] = (
                        'L' if occupied >= threshold else '#'
                    )
        if new_seating == work_seating:
            break
        work_seating = new_seating
    return new_seating


def count_occupied(seating: List[List[str]]) -> int:
    """Count the number of seats that are occupied."""
    count = 0
    for row in seating:
        count += row.count('#')
    return count


def main() -> None:
    """Work with seating system."""
    with open(INPUT_FILE, encoding='utf-8') as input_file:
        seating = [list(x.strip()) for x in input_file]

    new_seating = occupation_simulation(seating, part='one')
    print(f'Part One: Number of occupied seats: {count_occupied(new_seating)}')
    new_seating = occupation_simulation(seating, part='two')
    print(f'Part Two: Number of occupied seats: {count_occupied(new_seating)}')


main()

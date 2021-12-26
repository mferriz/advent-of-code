#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Advent of Code 2021, day twenty five."""

import numpy

INPUT_FILE = 'data/day_25.txt'
SOUTH = 0
EAST = 1


def main() -> None:
    """Find the first step where no sea cucumber move."""
    input_matrix = []
    with open(INPUT_FILE, encoding='utf-8') as input_file:
        for line in input_file:
            line = line.strip().replace('.', '0,').replace('>', '1,')
            line = line.replace('v', '2,')
            line = line[:-1]  # Remove last comma
            input_matrix.append([int(x) for x in line.split(',')])

    matrix = numpy.array(input_matrix, dtype=int)
    trues = numpy.full(matrix.shape, True, dtype=bool)
    falses = numpy.full(matrix.shape, False, dtype=bool)

    cucumbers = {EAST: numpy.where(matrix == 1, trues, falses),
                 SOUTH: numpy.where(matrix == 2, trues, falses)}

    still_moving = {EAST: True, SOUTH: True}
    step_count = 0
    while still_moving[EAST] or still_moving[SOUTH]:
        still_moving = {EAST: False, SOUTH: False}

        for direction in [EAST, SOUTH]:
            all_cucumbers = cucumbers[EAST] | cucumbers[SOUTH]
            moving_cucumbers = cucumbers[direction].copy()

            # Identify the sea cucumbers that cannot move toward the direction
            moving_cucumbers = numpy.roll(moving_cucumbers, 1, axis=direction)
            moving_cucumbers = moving_cucumbers & all_cucumbers
            moving_cucumbers = numpy.roll(moving_cucumbers, -1, axis=direction)
            # Now, get the cucumbers that can move to that direction.
            moving_cucumbers = (
                cucumbers[direction] & numpy.logical_not(moving_cucumbers)
            )
            if numpy.any(moving_cucumbers):
                still_moving[direction] = True
                # Remove sea cucumbers that can move from their original pos.
                cucumbers[direction] &= numpy.logical_not(moving_cucumbers)
                # Then apply the move to their new position.
                cucumbers[direction] |= numpy.roll(moving_cucumbers, 1,
                                                   axis=direction)
        step_count += 1

    print(f'Part One: First step on which no sea cucumber move: {step_count}')


main()

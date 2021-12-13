#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Advent of Code 2021, day thirteen."""

import re
from typing import List, Tuple

import numpy


INPUT_FILE = 'data/day_13.txt'
INSTRUCTION = re.compile(r'fold along (x|y)=(\d+)')


def main() -> None:
    """Perform folding instructions."""
    with open(INPUT_FILE, encoding='utf-8') as input_file:
        # Get coordinates and instructions
        coordinates: List[Tuple[int, int]] = []
        instructions: List[Tuple[str, int]] = []
        max_x = -1
        max_y = -1
        for line in input_file:
            line = line.strip()
            if not line:
                continue
            match = INSTRUCTION.match(line)
            if match is not None:
                instructions.append((match.group(1),
                                     int(match.group(2))))
            else:
                x_coordinate_str, y_coordinate_str = line.split(',')
                x_coordinate = int(x_coordinate_str)
                y_coordinate = int(y_coordinate_str)
                coordinates.append((x_coordinate, y_coordinate))
                if x_coordinate > max_x:
                    max_x = x_coordinate
                if y_coordinate > max_y:
                    max_y = y_coordinate

        # Build the matrix
        matrix = numpy.zeros((max_y + 1, max_x + 1), dtype=int)

        # Fill matrix with coordinates.
        for x_coordinate, y_coordinate in coordinates:
            matrix[y_coordinate][x_coordinate] = 1

        # Do the folding operations.
        for count, (fold_coordinate, row_col) in enumerate(instructions):
            if fold_coordinate == 'x':
                complement = numpy.fliplr(matrix)
                matrix = numpy.logical_or(matrix, complement)
                matrix = numpy.rot90(matrix, k=3)
                matrix = numpy.resize(matrix,
                                      (row_col, matrix.shape[1]))
                matrix = numpy.rot90(matrix, k=1)
            else:
                complement = numpy.flipud(matrix)
                matrix = numpy.logical_or(matrix, complement)
                matrix = numpy.resize(matrix,
                                      (row_col, matrix.shape[1]))
            if not count:
                print(f'Part One: Number of dots visible: '
                      f'{numpy.count_nonzero(matrix)}')

        print('Part Two: Activation Code: ')
        for x in range(matrix.shape[0]):
            for y in range(matrix.shape[1]):
                if matrix[x][y]:
                    print('#', end='')
                else:
                    print(' ', end='')
            print()


main()

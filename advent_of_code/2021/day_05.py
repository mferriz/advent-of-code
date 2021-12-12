#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Advent of Code 2021, day five."""

import numpy

MAX_DIMENSION = 1000
INPUT_FILE = 'data/day_05.txt'


def main() -> None:
    """Calculate dangerous locations in hydrothermal vents."""
    part_one = numpy.zeros((MAX_DIMENSION, MAX_DIMENSION),
                           dtype=int, order='C')
    part_two = numpy.zeros((MAX_DIMENSION, MAX_DIMENSION),
                           dtype=int, order='C')
    dangerous_threshold = numpy.ones((MAX_DIMENSION, MAX_DIMENSION),
                                     dtype=int, order='C')

    with open(INPUT_FILE, encoding='utf-8') as input_file:
        for line in input_file:
            # Parse a line of the file
            coord1, coord2 = line.strip().split(' -> ')
            x1_str, y1_str = coord1.split(',')
            x2_str, y2_str = coord2.split(',')
            x1 = int(x1_str)
            y1 = int(y1_str)
            x2 = int(x2_str)
            y2 = int(y2_str)
            if x1 == x2:
                min_y = min(y1, y2)
                max_y = max(y1, y2)
                for y in range(min_y, max_y + 1):
                    part_one[x1][y] += 1
                    part_two[x1][y] += 1
            elif y1 == y2:
                min_x = min(x1, x2)
                max_x = max(x1, x2)
                for x in range(min_x, max_x + 1):
                    part_one[x][y1] += 1
                    part_two[x][y1] += 1
            else:  # Must be diagonal
                increment_x = 1 if x2 > x1 else -1
                increment_y = 1 if y2 > y1 else -1
                x = x1
                y = y1
                while x != x2 and x < MAX_DIMENSION:
                    part_two[x][y] += 1
                    x += increment_x
                    y += increment_y
                part_two[x][y] += 1

        dangerous = numpy.greater(part_one, dangerous_threshold)
        count_dangerous = numpy.count_nonzero(dangerous)
        print(f'Part One: Count of dangerous positions: {count_dangerous}')
        dangerous = numpy.greater(part_two, dangerous_threshold)
        count_dangerous = numpy.count_nonzero(dangerous)
        print(f'Part Two: Count of dangerous positions: {count_dangerous}')


main()

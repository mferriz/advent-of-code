#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Advent of Code 2021, day nine."""

import numpy


INPUT_FILE = 'data/day_09.txt'


def find_basin_elements(matrix: numpy.ndarray, visited: numpy.ndarray,
                        row: int, col: int) -> None:
    """Identify all the neighbors of a row and column."""
    if 0 <= row < matrix.shape[0] \
       and 0 <= col < matrix.shape[1] \
       and not visited[row][col] \
       and matrix[row][col] != 9:
        visited[row][col] = True
        find_basin_elements(matrix, visited, row, col - 1)
        find_basin_elements(matrix, visited, row - 1, col)
        find_basin_elements(matrix, visited, row + 1, col)
        find_basin_elements(matrix, visited, row, col + 1)


def main() -> None:
    """Obtain risk levels and largest bins determination."""
    input_rows = []
    with open(INPUT_FILE, encoding='utf-8') as input_file:
        for line in input_file:
            input_rows.append([int(x) for x in list(line.strip())])

    matrix = numpy.array(input_rows, dtype=int)
    # Part one: Find lows
    risk_levels = []
    lows = []
    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            if (not col or matrix[row][col] < matrix[row][col - 1]) \
               and (col == matrix.shape[1] - 1
                    or matrix[row][col] < matrix[row][col + 1]) \
                and (not row or matrix[row][col] < matrix[row - 1][col]) \
                and (row == matrix.shape[0] - 1
                     or matrix[row][col] < matrix[row + 1][col]):
                risk_levels.append(matrix[row][col] + 1)
                lows.append((row, col))

    # Part two: Find basin sizes
    basin_sizes = []
    for row, col in lows:
        visited = numpy.full(matrix.shape, False)
        find_basin_elements(matrix, visited, row, col)
        basin_sizes.append(numpy.sum(visited))

    basin_sizes = sorted(basin_sizes, reverse=True)
    mult_largest_basins = basin_sizes[0] * basin_sizes[1] * basin_sizes[2]

    print(f'Part One: Sum of the risk level: {sum(risk_levels)}')
    print(f'Part Two: Multiplication of element counts of '
          f'largest basins: {mult_largest_basins}')


main()

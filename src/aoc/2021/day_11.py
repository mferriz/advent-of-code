#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Advent of Code 2021, day eleven."""

import numpy


INPUT_FILE = 'data/day_11.txt'


def main() -> None:
    """Obtain flashing information."""
    input_rows = []
    with open(INPUT_FILE, encoding='utf-8') as input_file:
        for line in input_file:
            input_rows.append([int(x) for x in list(line.strip())])
        matrix = numpy.array(input_rows, dtype=int)

        flash_count = 0
        first_step_all_flashed = None
        step = 0
        while first_step_all_flashed is None or step < 100:
            matrix = matrix + 1
            energized_octupi = matrix > 9
            flashed = numpy.full(matrix.shape, False)
            while numpy.any(numpy.not_equal(flashed, energized_octupi)):
                rows, cols = numpy.nonzero(energized_octupi)
                for index, row in enumerate(rows):
                    col = cols[index]
                    if not flashed[row][col]:
                        if step < 100:
                            flash_count += 1
                        flashed[row][col] = True
                        # Increase energy on adjacent
                        for energy_row in range(row - 1, row + 2):
                            for energy_col in range(col - 1, col + 2):
                                if (energy_row == row and energy_col == col) \
                                   or not 0 <= energy_row < matrix.shape[0] \
                                   or not 0 <= energy_col < matrix.shape[1]:
                                    continue
                                matrix[energy_row][energy_col] += 1
                energized_octupi = matrix > 9
            matrix[flashed] = 0
            if numpy.all(flashed) and first_step_all_flashed is None:
                first_step_all_flashed = step + 1
            # print(matrix)
            step += 1

        print(f'Part One: Number of flashes after 100 steps: {flash_count}')
        print(f'Part Two: First step where all flashed: '
              f'{first_step_all_flashed}')


main()

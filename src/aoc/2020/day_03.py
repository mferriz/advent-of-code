#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Advent of Code 2020, day three."""

INPUT_FILE = 'data/day_03.txt'


def main() -> None:
    """Identify toboggan trajectory."""
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    with open(INPUT_FILE, encoding='utf-8') as input_file:
        grid = [line.strip() for line in input_file]

    tree_count = {}
    prod_slopes = 1
    for col_offset, row_offset in slopes:
        tree_count[(col_offset, row_offset)] = 0
        row, col = row_offset, col_offset
        while row < len(grid):
            if grid[row][col] == '#':
                tree_count[(col_offset, row_offset)] += 1
            col = (col + col_offset) % len(grid[0])
            row += row_offset
        prod_slopes *= tree_count[(col_offset, row_offset)]
    print(f'Part One: Number of Trees: {tree_count[(3, 1)]}')
    print(f'Part Two: Product of trees encountered in all slopes: '
          f'{prod_slopes}')


main()

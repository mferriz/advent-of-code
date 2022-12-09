#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Advent of Code 2022, day nine."""

import numpy

INPUT_FILE = 'data/day_09.txt'
OPERATION = {
    'R': (1, 0),
    'U': (0, 1),
    'L': (-1, 0),
    'D': (0, -1)
}
FOLLOW = {
    (2, 0): (1, 0),
    (-2, 0): (-1, 0),
    (0, 2): (0, 1),
    (0, -2): (0, -1),
    (1, 2): (1, 1),
    (1, -2): (1, -1),
    (-1, 2): (-1, 1),
    (-1, -2): (-1, -1),
    (2, 1): (1, 1),
    (2, -1): (1, -1),
    (-2, 1): (-1, 1),
    (-2, -1): (-1, -1)
}


def main() -> None:
    """Simulate rope movement."""
    with open(INPUT_FILE, encoding='utf-8') as input_file:
        tail_locations = set()
        head = (0, 0)
        tail = (0, 0)
        tail_locations.add(tail)
        for line in input_file:
            instruction, quantity = line.strip().split(' ')
            for _ in range(int(quantity)):
                head = tuple(numpy.add(head, OPERATION[instruction]))
                if (delta := tuple(numpy.subtract(head, tail))) in FOLLOW:
                    tail = tuple(numpy.add(tail, FOLLOW[delta]))
                    tail_locations.add(tail)
        print(f'Part One: Positions tail of rope visit: {len(tail_locations)}')


main()

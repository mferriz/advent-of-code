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


def main() -> None:
    """Simulate rope movement."""
    with open(INPUT_FILE, encoding='utf-8') as input_file:
        tail_locations = set()
        head = (0, 0)
        tail = (0, 0)
        for line in input_file:
            instruction, quantity = line.strip().split(' ')
            for _ in range(int(quantity)):
                old_head = head
                head = tuple(numpy.add(head, OPERATION[instruction]))
                delta = tuple(numpy.subtract(head, tail))
                if abs(delta[0]) > 1 or abs(delta[1]) > 1:
                    tail = old_head
                tail_locations.add(tail)
        print(f'Part One: Positions tail of rope visit: {len(tail_locations)}')


main()

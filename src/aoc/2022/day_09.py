#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Advent of Code 2022, day nine."""

import numpy

INPUT_FILE = 'data/day_09.txt'
OPERATION = {
    'R': numpy.array((1, 0)),
    'U': numpy.array((0, 1)),
    'L': numpy.array((-1, 0)),
    'D': numpy.array((0, -1)),
}
FOLLOW = {
    (2, 0): numpy.array((1, 0)),
    (-2, 0): numpy.array((-1, 0)),
    (0, 2): numpy.array((0, 1)),
    (0, -2): numpy.array((0, -1)),
    (1, 2): numpy.array((1, 1)),
    (1, -2): numpy.array((1, -1)),
    (-1, 2): numpy.array((-1, 1)),
    (-1, -2): numpy.array((-1, -1)),
    (2, 1): numpy.array((1, 1)),
    (2, -1): numpy.array((1, -1)),
    (-2, 1): numpy.array((-1, 1)),
    (-2, -1): numpy.array((-1, -1)),
    (2, 2): numpy.array((1, 1)),
    (2, -2): numpy.array((1, -1)),
    (-2, 2): numpy.array((-1, 1)),
    (-2, -2): numpy.array((-1, -1)),
}


def simulate(knots: int = 2) -> int:
    """Simulate rope movement."""
    with open(INPUT_FILE, encoding='utf-8') as input_file:
        tail_locations = set()
        rope = [numpy.array((0, 0)) for _ in range(knots)]
        tail_locations.add(tuple(rope[-1]))
        for line in input_file:
            instruction, quantity = line.strip().split(' ')
            for _ in range(int(quantity)):
                rope[0] += OPERATION[instruction]
                for knot in range(1, len(rope)):
                    if (delta := tuple(rope[knot - 1] - rope[knot])) in FOLLOW:
                        rope[knot] += FOLLOW[delta]
                    else:
                        break
                tail_locations.add(tuple(rope[-1]))
    return len(tail_locations)


def main() -> None:
    """Simulate a couple of rope movements."""
    print(f'Part One: Positions tail of visits (2 knots): {simulate(2)}')
    print(f'Part One: Positions tail of visits (10 knots): {simulate(10)}')


main()

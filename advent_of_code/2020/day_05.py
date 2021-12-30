#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Advent of Code 2020, day five."""

INPUT_FILE = 'data/day_05.txt'


def main() -> None:
    """Identify missing ticket."""
    with open(INPUT_FILE, encoding='utf-8') as input_file:
        tkt = sorted([int(x.strip().replace('F', '0').replace('B', '1')
                          .replace('L', '0').replace('R', '1'), 2)
                      for x in input_file])
    print(f'Part One: Highest Seat Id: {tkt[-1]}')

    # Finding the missing ticket.
    # Using triangular numbers to get sum from 0 to last seat
    # Removing sum from 0 to seat before first one.
    sum_all = (tkt[-1] * (tkt[-1] + 1) - (tkt[0] - 1) * tkt[0]) // 2
    missing_ticket = sum_all - sum(tkt)
    print(f'Part Two: Missing Seat Id: {missing_ticket}')


main()

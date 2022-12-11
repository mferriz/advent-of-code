#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Advent of Code 2022, day ten."""

import bitarray

INPUT_FILE = 'data/day_10.txt'


def format_crt(crt: bitarray.bitarray) -> str:
    """Print CRT as part of exercise two."""
    buffer = ''
    for i in range(len(crt)):
        if i and not (i % 40):
            buffer += '\n'
        buffer += '#' if crt[i] else '.'
    return buffer


def main() -> None:
    """Calculate signal strengths."""
    clock_cycle = 0
    register_x = 1
    mark = 20
    total_strength = 0
    with open(INPUT_FILE, encoding='utf-8') as input_file:
        for line in input_file:
            line = line.strip()
            if line == 'noop':
                clock_cycle += 1
                if clock_cycle == mark:
                    total_strength += clock_cycle * register_x
                    mark += 40
            else:
                _, operator = line.split(' ')
                clock_cycle += 1
                if clock_cycle == mark:
                    total_strength += clock_cycle * register_x
                    mark += 40
                clock_cycle += 1
                if clock_cycle == mark:
                    total_strength += clock_cycle * register_x
                    mark += 40
                register_x += int(operator)

    print(f'Part One: Positions tail of visits (2 knots): {total_strength}')

    register_x = 1
    crt = bitarray.bitarray('0' * 240)
    sprite = bitarray.bitarray(bitarray.bitarray('111' + '0' * 37)) * 6
    cycle = bitarray.bitarray('1' + '0' * 239)
    with open(INPUT_FILE, encoding='utf-8') as input_file:
        for line in input_file:
            line = line.strip()
            crt |= sprite & cycle
            if line == 'noop':
                cycle >>= 1
            else:
                _, operator = line.split(' ')
                cycle >>= 1
                crt |= sprite & cycle
                cycle >>= 1
                register_x += int(operator)
                if register_x > 0:
                    sprite = (bitarray.bitarray(
                        '111' + '0' * 37) >> (register_x - 1)) * 6
                else:
                    sprite = (bitarray.bitarray(
                        '111' + '0' * 37) << (abs(register_x - 1))) * 6
    print(f'Part Two: Render Image:\n{format_crt(crt)}')


main()

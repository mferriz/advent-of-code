#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Advent of Code 2020, day nine."""

INPUT_FILE = 'data/day_09.txt'
PREAMBLE = 25


def main() -> None:
    """Decode eXchange-Masking Addition System (XMAS)."""
    with open(INPUT_FILE, encoding='utf-8') as input_file:
        numbers = [int(x.strip()) for x in input_file]

    invalid_number = 0
    for index in range(PREAMBLE, len(numbers)):
        previous_numbers = numbers[index - PREAMBLE:index]
        for previous_number in previous_numbers:
            if (numbers[index] - previous_number) in previous_numbers:
                break
        else:
            invalid_number = numbers[index]
            print(f'Part One: First invalid number: {invalid_number}')
            break

    for index_a in range(index):
        accumulator = 0
        largest_number = None
        smallest_number = None
        for index_b in range(index_a, index):
            accumulator += numbers[index_b]
            if largest_number is None or numbers[index_b] > largest_number:
                largest_number = numbers[index_b]
            if smallest_number is None or numbers[index_b] < smallest_number:
                smallest_number = numbers[index_b]
            if accumulator >= invalid_number:
                break
        if accumulator == invalid_number:
            print(f'Part Two: Encryption Weakness: '
                  f'{largest_number + smallest_number}')
            break


main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Advent of Code 2022, day six."""

INPUT_FILE = 'data/day_06.txt'


def main() -> None:
    """Find and report start-of-packet and start-of-message."""
    with open(INPUT_FILE, encoding='utf-8') as input_file:
        data = input_file.read()
    for index in range(4, len(data)):
        if len(set(data[index - 4:index])) == 4:
            print(f'Part One: Start of packet: {index}')
            break
    for index in range(14, len(data)):
        if len(set(data[index - 14:index])) == 14:
            print(f'Part Two: Start of message: {index}')
            break


main()

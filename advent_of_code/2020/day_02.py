#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Advent of Code 2020, day two."""

import collections
import re

INPUT_FILE = 'data/day_02.txt'
RULE = re.compile(r'(\d+)-(\d+)\s([a-z]):\s([a-z]+)')


def main() -> None:
    """Password rule verification."""
    with open(INPUT_FILE, encoding='utf-8') as input_file:
        part_one_valid_count = 0
        part_two_valid_count = 0
        for line in input_file:
            if (match := RULE.match(line.strip())) is not None:
                first_number = int(match.group(1))
                second_number = int(match.group(2))
                character = match.group(3)
                password = match.group(4)
                counter = collections.Counter(list(password))
                if counter.get(character, 0) in range(first_number,
                                                      second_number + 1):
                    part_one_valid_count += 1
                if ((password[first_number - 1] == character)
                        != (password[second_number - 1] == character)):
                    part_two_valid_count += 1
    print(f'Part One: Valid passwords: {part_one_valid_count}')
    print(f'Part Two: Valid passwords: {part_two_valid_count}')


main()

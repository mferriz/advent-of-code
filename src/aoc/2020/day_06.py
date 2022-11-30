#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Advent of Code 2020, day six."""

import collections

INPUT_FILE = 'data/day_06.txt'


def main() -> None:
    """Identify missing ticket."""
    with open(INPUT_FILE, encoding='utf-8') as input_file:
        accumulator = 0
        common_in_group = {}
        for group_number, group in enumerate(input_file.read().split('\n\n')):
            persons_in_group = group.strip().count('\n') + 1
            counter = collections.Counter(list(group.replace('\n', '')))
            common_in_group[group_number] = 0
            for value in counter.values():
                if value == persons_in_group:
                    common_in_group[group_number] += 1
            accumulator += len(counter.keys())
        print(f'Part One: Sum of counts: {accumulator}')
        print(f'Part Two: Sum of counts: {sum(common_in_group.values())}')


main()

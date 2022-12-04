#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Advent of Code 2022, day four."""

INPUT_FILE = 'data/day_04.txt'


def main() -> None:
    """Calculate assignment overlaps."""
    full_overlap = 0
    overlap_at_all = 0
    with open(INPUT_FILE, encoding='utf-8') as input_file:
        for pair_assignment in input_file:
            assignment_1, assignment_2 = pair_assignment.split(',')
            first, last = assignment_1.split('-')
            first_set = set(range(int(first), int(last) + 1))
            first, last = assignment_2.split('-')
            second_set = set(range(int(first), int(last) + 1))
            intersection_set = first_set & second_set
            if len(intersection_set):
                overlap_at_all += 1
                if intersection_set in (first_set, second_set):
                    full_overlap += 1

    print(f'Part One: Full overlap: {full_overlap}')
    print(f'Part Two: Overlap at all: {overlap_at_all}')


main()

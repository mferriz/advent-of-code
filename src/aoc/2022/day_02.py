#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Advent of Code 2022, day two."""

INPUT_FILE = 'data/day_02.txt'
ROUND_SCORE = {
    'A X': 3,
    'A Y': 6,
    'A Z': 0,
    'B X': 0,
    'B Y': 3,
    'B Z': 6,
    'C X': 6,
    'C Y': 0,
    'C Z': 3,
}
PART_TWO_MAPPING = {
    'A X': 'A Z',
    'A Y': 'A X',
    'A Z': 'A Y',
    'B X': 'B X',
    'B Y': 'B Y',
    'B Z': 'B Z',
    'C X': 'C Y',
    'C Y': 'C Z',
    'C Z': 'C X',
}
SHAPE_SCORE = {'X': 1, 'Y': 2, 'Z': 3}


def main() -> None:
    """Calculate score of rock-paper-scissors tournament."""
    part_one_score = 0
    part_two_score = 0
    with open(INPUT_FILE, encoding='utf-8') as input_file:
        for line in input_file:
            line = line.strip()
            part_one_score += ROUND_SCORE[line] + SHAPE_SCORE[line[-1]]
            line = PART_TWO_MAPPING[line]
            part_two_score += ROUND_SCORE[line] + SHAPE_SCORE[line[-1]]
    print(f'Part One: Tournament Score: {part_one_score}')
    print(f'Part Two: Tournament Score: {part_two_score}')


main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Advent of Code 2021, day fourteen."""

import collections

INPUT_FILE = 'data/day_14.txt'


def main() -> None:
    """Perform expansion of a polymer."""
    # Get polymer template and pair insertion rules.
    with open(INPUT_FILE, encoding='utf-8') as input_file:
        polymer_template, insertion_rules = input_file.read().split('\n\n')

    rules = {}
    for insertion_rule in insertion_rules.splitlines():
        pair, insertion_character = insertion_rule.split(' -> ')
        rules[pair] = insertion_character

    # Accounting for initial state.
    counters = collections.Counter()
    for index in range(len(polymer_template) - 1):
        counters[polymer_template[index:index + 2]] += 1

    for step in range(40):
        char_counter = collections.Counter()
        new_counters = collections.Counter()
        for key, value in counters.items():
            new_counters[f'{key[0]}{rules[key]}'] += value
            new_counters[f'{rules[key]}{key[1]}'] += value
            char_counter[key[0]] += value
            char_counter[rules[key]] += value
            counters = new_counters
        if step in [9, 39]:
            part_str = 'One' if step == 9 else 'Two'
            char_counter[polymer_template[-1]] += 1
            values = sorted(char_counter.values())
            print(f'Part {part_str}: Most common element less least '
                  f'element: {values[-1] - values[0]}')


main()

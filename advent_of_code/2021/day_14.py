#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Advent of Code 2021, day fourteen."""

import collections
from typing import Dict

INPUT_FILE = 'data/day_14.txt'


def expand_polymer(rules: Dict[str, str], polymer: str, steps: int) -> str:
    """Expand polymer segment."""
    resulting_polymer = ''
    for step in range(steps):
        for index in range(len(polymer) - 1):
            segment = polymer[index:index + 2]
            resulting_polymer += f'{polymer[index]}{rules[segment]}'
        polymer = resulting_polymer + polymer[-1]
        resulting_polymer = ''
    return polymer


def deep_expansion(polymer: str,
                   polymer_expansion: Dict[str, str],
                   polymer_counters: collections.Counter,
                   depth: int) -> collections.Counter:
    """Deep expansion of a polymer."""
    counters = collections.Counter()
    for index in range(len(polymer) - 1):
        new_polymer = polymer_expansion[polymer[index:index+2]]
        if depth:
            counters.update(deep_expansion(new_polymer,
                                           polymer_expansion,
                                           polymer_counters, depth - 1))
        else:
            counters.update(polymer_counters[polymer[index:index+2]])
        # This technique overlaps characters. So there is a need to remove
        # that count.
        if index:
            counters.update(collections.Counter({new_polymer[0]: -1}))
    return counters


def main() -> None:
    """Perform folding instructions."""
    # Get polymer template and pair insertion rules.
    with open(INPUT_FILE, encoding='utf-8') as input_file:
        polymer_template = None
        rules = {}
        for line in input_file:
            line = line.strip()
            if not line:
                continue
            if polymer_template is None:
                polymer_template = line
            else:
                pair, insertion = line.split(' -> ')
                rules[pair] = insertion

    # Cache polymer expansion and counts for 10 steps.
    polymer_expansion = {}
    polymer_counters = {}
    for rule in rules:
        polymer_expansion[rule] = expand_polymer(rules, rule, 10)
        polymer_counters[rule] = collections.Counter(polymer_expansion[rule])

    counters = deep_expansion(polymer_template, polymer_expansion,
                              polymer_counters, 0)
    collection_list = counters.most_common()
    print(f'Part One: Most common less least common after 10 steps: '
          f'{collection_list[0][1] - collection_list[-1][1]}')

    counters = deep_expansion(polymer_template, polymer_expansion,
                              polymer_counters, 3)
    collection_list = counters.most_common()
    print(f'Part Two: Most common less least common after 10 steps: '
          f'{collection_list[0][1] - collection_list[-1][1]}')


main()

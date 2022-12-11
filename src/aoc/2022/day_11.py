#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Advent of Code 2022, day eleven."""

import re

INPUT_FILE = 'data/day_11.txt'
MONKEY_MODEL = re.compile(r'\s*(\d+):\s+Starting items:\s(.+)\s+'
                          r'Operation:\s(.+)\s+Test: divisible by (\d+)\s+'
                          r'If true: throw to monkey (\d)\s+'
                          r'If false: throw to monkey (\d)')


def main() -> None:
    """Calculate monkey play."""
    with open(INPUT_FILE, encoding='utf-8') as input_file:
        sections = input_file.read().replace('\n', '').split('Monkey')[1:]

    # Initialization
    monkey_queues = []
    monkey_rules = []
    monkey_inspections = []
    for _ in range(len(sections)):
        monkey_queues.append([])
        monkey_rules.append([])
        monkey_inspections.append(0)
    for section in sections:
        if (match := MONKEY_MODEL.match(section)):
            monkey_queues[int(match.group(1))] = (
                [int(number) for number in match.group(2).split(',')]
            )
            monkey_rules[int(match.group(1))] = [
                match.group(3), int(match.group(4)),
                int(match.group(5)), int(match.group(6)),
            ]
    for _round in range(20):
        for monkey in range(len(sections)):
            while len(monkey_queues[monkey]):
                # Account inspection
                monkey_inspections[monkey] += 1
                # Get the item in queue
                item = monkey_queues[monkey].pop(0)
                # Get the operation
                operation = (
                    monkey_rules[monkey][0].replace('old', f'{item}')
                    .replace('new = ', '').strip()
                )
                # Do the operation.
                # flake8: noqa: SCS101
                value = eval(f'{operation}')  # pylint: disable=eval-used
                # Monkey gets bored
                value = value // 3
                # Do the test
                test_passes = not value % monkey_rules[monkey][1]
                # Throw to appropriate monkey
                next_monkey = (
                    monkey_rules[monkey][2] if test_passes
                    else monkey_rules[monkey][3]
                )
                monkey_queues[next_monkey].append(value)

    monkey_inspections.sort(reverse=True)
    monkey_business = monkey_inspections[0] * monkey_inspections[1]
    print(f'Part One: Level of Monkey business: {monkey_business}')


main()

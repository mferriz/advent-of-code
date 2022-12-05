#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Advent of Code 2022, day five."""

import copy
import re

INPUT_FILE = 'data/day_05.txt'
STACK_NUMBERS = re.compile(r'(\s\d+)+\s')
INSTRUCTION = re.compile(r'move (\d+) from (\d+) to (\d+)')


def main() -> None:
    """Calculate assignment overlaps."""
    number_of_stacks = 0
    stacks = []
    with open(INPUT_FILE, encoding='utf-8') as input_file:
        # Read initial stack configuration
        for line in input_file:
            if not number_of_stacks:
                number_of_stacks = len(line) // 4
                for _ in range(number_of_stacks):
                    stacks.append([])
            if not STACK_NUMBERS.match(line):
                for stack_number, crate in enumerate(
                        range(1, (number_of_stacks - 1) * 4 + 2, 4)):
                    if line[crate] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                        stacks[stack_number].insert(0, line[crate])
            else:
                break
        # Read and execute instructions
        part_one_stacks = stacks
        part_two_stacks = copy.deepcopy(stacks)
        for line in input_file:
            if (match := INSTRUCTION.match(line)) is not None:
                count = int(match.group(1))
                from_stack = int(match.group(2)) - 1
                to_stack = int(match.group(3)) - 1
                # Instructions for part one of the puzzle
                for _ in range(0, count):
                    crate = part_one_stacks[from_stack].pop()
                    part_one_stacks[to_stack].append(crate)
                # Instructions for part two.
                crates = part_two_stacks[from_stack][-count:]
                part_two_stacks[from_stack] = (
                    part_two_stacks[from_stack][:-count]
                )
                part_two_stacks[to_stack] = (
                    part_two_stacks[to_stack] + crates
                )

        crates_at_top = ''
        for stack in part_one_stacks:
            if len(stack):
                crates_at_top += stack[-1]
        print(f'Part One: Crates at top of stacks {crates_at_top}')
        crates_at_top = ''
        for stack in part_two_stacks:
            if len(stack):
                crates_at_top += stack[-1]
        print(f'Part Two: Crates at top of stacks {crates_at_top}')


main()

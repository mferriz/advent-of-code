#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Advent of Code 2020, day eight."""

import copy
import contextlib
from typing import List, Tuple

INPUT_FILE = 'data/day_08.txt'
OPER = 0
VALUE = 1


def execute(program: List[Tuple[str, str]]) -> int:
    """Execute a program until completion. Returns value of accumulator.

    Raises RuntimeError if there is an infinite loop.
    """
    executed = set()
    accumulator = 0
    index = 0
    while index not in executed and index < len(program):
        operation, value = program[index][OPER], int(program[index][VALUE])
        executed.add(index)
        if operation == 'acc':
            accumulator += value
            index += 1
        elif operation == 'jmp':
            index += value
        else:
            index += 1
    if index < len(program):
        raise RuntimeError(f'{accumulator}')
    return accumulator


def main() -> None:
    """Execute handheldhalting."""
    with open(INPUT_FILE, encoding='utf-8') as input_file:
        program = [x.strip().split() for x in input_file]

    # Part One: Finding infinite loop.
    try:
        accumulator = execute(program)
    except RuntimeError as exception:
        accumulator = int(str(exception))
        print(f'Part One: Value of accumulator: {accumulator}')

    # Second part. Try changing nop for jmp and jmp for nop.
    for index in range(len(program)):
        if program[index][OPER] in ['nop', 'jmp']:
            program_copy = copy.deepcopy(program)
            program_copy[index][OPER] = (
                'jmp' if program[index][OPER] == 'nop' else 'nop'
            )
            with contextlib.suppress(RuntimeError):
                accumulator = execute(program_copy)
                print(f'Part Two: Accumulator after program terminates: '
                      f'{accumulator}')
                break


main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Advent of Code 2021, day twenty four."""

from typing import List

INPUT_FILE = 'data/day_24.txt'


class ArithmeticLogicUnit:
    """Submarine ALU."""

    def __init__(self) -> None:
        """Initialize the ALU."""
        self.var = {'w': 0, 'x': 0, 'y': 0, 'z': 0}

    def execute(self, instructions: List[str], user_input: str) -> None:
        """Execute a program."""
        for line in instructions:
            if line.startswith('inp'):
                _operation, operand = line.split()
                self.var[operand] = int(user_input[0])
                user_input = user_input[1:]
            else:
                operation, op_1, op_2 = line.split()
                if op_2 in self.var:
                    op_2 = self.var[op_2]
                else:
                    op_2 = int(op_2)
                if operation == 'add':
                    self.var[op_1] += op_2
                elif operation == 'mul':
                    self.var[op_1] *= op_2
                elif operation == 'div':
                    self.var[op_1] //= op_2
                elif operation == 'mod':
                    self.var[op_1] %= op_2
                elif operation == 'eql':
                    self.var[op_1] = 1 if (self.var[op_1] == op_2) else 0
                else:
                    raise ValueError('Imposible operation')


def main() -> None:
    """Read program and find MONAD model numbers."""
    program = []
    with open(INPUT_FILE, encoding='utf-8') as input_file:
        program = [line.strip() for line in input_file]

    # This particular puzzle involves reverse engineering the input file
    # to find patterns that can turn register z to zero on the last
    # operation.
    #
    # The patterns were found because the instructions use a base-26 encoding
    # plus offsets.
    #
    # The most significant digit in the model number is called w0,
    # then w1. The last digit is w13.
    #
    # From analysis, the following rules make a model number NOMAD compatible:
    #
    # * w2 == w3
    # * w7 == w6 - 1
    # * w9 == w8 + 2
    # * w10 == w5 + 3
    # * w11 == W4 - 5
    # * w12 == w1 - 7
    # * w13 == w0 + 6
    #
    # Following the rules obtained above, the response to the
    # challenge can be calculated manually:

    model_number = '39999698799429'
    alu = ArithmeticLogicUnit()
    alu.execute(program, model_number)
    if not alu.var['z']:
        print(f'Part One: Largest model number supported by NOMAD: '
              f'{model_number}')

    model_number = '18116121134117'
    alu = ArithmeticLogicUnit()
    alu.execute(program, model_number)
    if not alu.var['z']:
        print(f'Part Two: Smallest model number supported by NOMAD: '
              f'{model_number}')


main()

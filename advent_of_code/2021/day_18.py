#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Advent of Code 2021, day eighteen."""

import ast
import copy
from typing import Tuple, Union

INPUT_FILE = 'data/day_18.txt'


class SnailfishNumber:
    """Representation of a SnailfishNumber."""

    def __init__(self, number: Union[str, list]) -> None:
        """Initialize a Snailfish number from a string."""
        if isinstance(number, list):
            self._number = copy.deepcopy(number)
        else:
            self._number = (
                ast.literal_eval(number)
            )

    def magnitude(self, term: list = None) -> int:
        """Obtain the magnitude of a snailfish number."""
        if term is None:
            term = self._number
        a_magnitude = 0
        b_magnitude = 0
        if isinstance(term[0], list):
            a_magnitude = self.magnitude(term[0])
        else:
            a_magnitude = term[0]
        if isinstance(term[1], list):
            b_magnitude = self.magnitude(term[1])
        else:
            b_magnitude = term[1]
        return 3 * a_magnitude + 2 * b_magnitude

    def apply_explosion_right(self,
                              term: list,
                              number: int):
        """Apply explosion to leftmost number."""
        if isinstance(term[0], list):
            self.apply_explosion_right(term[0], number)
        else:
            term[0] += number

    def apply_explosion_left(self,
                             term: list,
                             number: int):
        """Apply explosion to rightmost number."""
        if isinstance(term[1], list):
            self.apply_explosion_left(term[1], number)
        else:
            term[1] += number

    def _explode(self,
                 term: list,
                 level: int,
                 flags: list) -> Tuple[int, int]:
        """Explode a snailfish number, if applicable."""
        a_term = None
        b_term = None
        if isinstance(term[0], list) and 'explode' not in flags:
            a_term = self._explode(term[0], level + 1, flags)
            if 'explode' in flags and 'explode-right' not in flags:
                flags.append('explode-right')
                if isinstance(term[1], list):
                    self.apply_explosion_right(term[1], a_term[1])
                else:
                    term[1] += a_term[1]
        if isinstance(term[1], list) and 'explode' not in flags:
            b_term = self._explode(term[1], level + 1, flags)
            if 'explode' in flags and 'explode-left' not in flags:
                flags.append('explode-left')
                if isinstance(term[0], list):
                    self.apply_explosion_left(term[0], b_term[0])
                else:
                    term[0] += b_term[0]
        if level == 3 and 'explode' not in flags:
            if a_term is not None:
                flags.append('explode')
                flags.append('explode-right')
                term[0] = 0
                if isinstance(term[1], list):
                    self.apply_explosion_right(term[1], a_term[1])
                else:
                    term[1] += a_term[1]
                return a_term
            elif b_term is not None:
                flags.append('explode')
                flags.append('explode-left')
                term[1] = 0
                if isinstance(term[0], list):
                    self.apply_explosion_left(term[0], b_term[0])
                else:
                    term[0] += b_term[0]
                return b_term
        if b_term is not None:
            return b_term
        if a_term is not None:
            return a_term
        return term

    def _split(self, term: list, flags: list):
        """Split a snailfish number."""
        if 'split' not in flags:
            if isinstance(term[0], list):
                self._split(term[0], flags)
            else:
                if term[0] >= 10:
                    flags.append('split')
                    term[0] = [term[0] // 2, term[0] - term[0] // 2]
        if 'split' not in flags:
            if isinstance(term[1], list) and 'split' not in flags:
                self._split(term[1], flags)
            else:
                if term[1] >= 10:
                    flags.append('split')
                    term[1] = [term[1] // 2, term[1] - term[1] // 2]

    def add(self, number: "SnailfishNumber") -> "SnailfishNumber":
        """Add two snailfish numbers and return a snailfish."""
        accumulator = [copy.deepcopy(self._number),
                       copy.deepcopy(number._number)]
        # Reduce
        while True:
            flags = []
            self._explode(accumulator, 0, flags)
            if 'explode' not in flags:
                self._split(accumulator, flags)
                if 'split' not in flags:
                    break
        return SnailfishNumber(accumulator)

    def __str__(self) -> str:
        """String representation of a snailfish number."""
        return str(self._number)


def main() -> None:
    """Snailfish addition exercise."""
    with open(INPUT_FILE, encoding='utf-8') as input_file:
        numbers = [SnailfishNumber(line.strip()) for line in input_file]

    accumulator = numbers[0]
    for number in numbers[1:]:
        accumulator = accumulator.add(number)
    print(f'Part One: Magnitude of snailfish number: '
          f'{accumulator.magnitude()}')

    max_magnitude = 0
    for a_index, a_number in enumerate(numbers):
        for b_index, b_number in enumerate(numbers):
            if a_index == b_index:
                continue
            magnitude = a_number.add(b_number).magnitude()
            if magnitude > max_magnitude:
                max_magnitude = magnitude
    print(f'Part Two: Largest magnitude of any two numbers: '
          f'{max_magnitude}')


main()

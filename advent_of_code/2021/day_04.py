#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Advent of Code 2021, day four."""

import copy
from typing import List, Tuple

from bitarray import bitarray

INPUT_FILE = 'data/day_04.txt'


class BingoCard:
    """Represents a bingo card."""

    def __init__(self, card_numbers: List[int]) -> None:
        """Prepare a bingo card with a list of numbers."""
        if len(card_numbers) != 25:
            raise ValueError('Bad card')
        self.bingo: bool = False
        self._numbers = copy.deepcopy(card_numbers)
        self._sum_unmarked_numbers = 0
        self._score = -1
        for number in self._numbers:
            self._sum_unmarked_numbers += number
        self._rows: List[bitarray] = [
            bitarray('00000'),
            bitarray('00000'),
            bitarray('00000'),
            bitarray('00000'),
            bitarray('00000')
        ]
        self._columns: List[str] = [
            bitarray('00000'),
            bitarray('00000'),
            bitarray('00000'),
            bitarray('00000'),
            bitarray('00000')
        ]

    def __str__(self) -> str:
        """Print bingo card for the user."""
        output = ''
        for count, number in enumerate(self._numbers):
            if count % 5 == 0:
                output = output.strip() + '\n'
            if self._rows[count // 5][count % 5]:
                output += f'\033[31;1;4m{number:02}\033[0m '
            else:
                output += f'{number:02} '
        return output.strip()

    def mark_number(self, number: int) -> bool:
        """Mark a bingo number. Return True if bingo!***"""
        bingo_match = bitarray('11111')
        if number in self._numbers:
            index = self._numbers.index(number)
            # Convert the index to row and column.
            row = index // 5
            column = index % 5
            self._rows[row][column] = 1
            self._columns[column][row] = 1
            self._sum_unmarked_numbers -= number
            self._score = self._sum_unmarked_numbers * number
            if bingo_match in [self._rows[row], self._columns[row]]:
                self.bingo = True
                return True
        return False

    def score(self) -> int:
        """Score of the winning board."""
        return self._score


def parse_input(filename: str) -> Tuple[List[int], List[BingoCard]]:
    """Parse input file and return a list of numbers drawn and bingo cards."""

    numbers_drawn: List[int] = []
    bingo_cards: List[BingoCard] = []
    bingo_card_numbers: List[int] = []
    with open(filename, encoding='utf-8') as input_file:
        for line in input_file:
            line = line.strip()
            if not line:  # There are some spaces in input file.
                continue
            # First line contains drawn numbers for bingo.
            if not numbers_drawn:
                numbers_drawn = list(map(int, line.split(',')))
            else:
                bingo_card_line: List[int] = list(map(int, line.split()))
                bingo_card_numbers = bingo_card_numbers + bingo_card_line
                if len(bingo_card_numbers) == 25:
                    bingo_card = BingoCard(bingo_card_numbers)
                    bingo_card_numbers = []
                    bingo_cards.append(bingo_card)
    return numbers_drawn, bingo_cards


def main() -> None:
    """Play bingo."""
    _numbers_drawn, bingo_cards = parse_input(INPUT_FILE)
    boards_to_remove: List[int] = []
    board_count = len(bingo_cards)

    for number in _numbers_drawn:
        if not bingo_cards:
            break
        for bingo_card_number, bingo_card in enumerate(bingo_cards):
            if bingo_card.mark_number(number):
                # Only print first and last boards.
                if len(bingo_cards) in (1, board_count):
                    part = 'Two' if len(bingo_cards) == 1 else 'One'
                    # print(f'Bingo in card: {bingo_card_number}\n')
                    # print(f'{str(bingo_card)}\n')
                    print(f'Part {part}: Score: {bingo_card.score()}')
                boards_to_remove.append(bingo_card_number)
        for bingo_card_number in sorted(boards_to_remove, key=int,
                                        reverse=True):
            del bingo_cards[bingo_card_number]
        boards_to_remove = []


main()

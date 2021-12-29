#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Advent of Code 2021, day twenty one."""

from typing import List, Tuple

# First index is for minimal three dice roll (3)
# Last for maximum three dice roll (9)
UNIVERSE_MULTIPLIER = [1, 3, 6, 7, 6, 3, 1]


class GameState:
    """State of a game."""
    cache = {}

    def __init__(self, space_index: List[int]) -> None:
        """Initialize game state."""
        self.player_up = 0
        self.space_index = [space_index[0], space_index[1]]
        self.score = [0, 0]

    def roll(self, roll: int) -> 'GameState':
        """Roll dice."""
        new_state = GameState([self.space_index[0], self.space_index[1]])
        new_state.space_index[self.player_up] = \
            (new_state.space_index[self.player_up] + roll) % 10
        new_state.score[0] = self.score[0]
        new_state.score[1] = self.score[1]
        new_state.score[self.player_up] += \
            new_state.space_index[self.player_up] + 1
        new_state.player_up = 0 if self.player_up else 1
        return new_state

    def is_over(self) -> bool:
        """Whether it is a final state or not."""
        return self.score[0] >= 21 or self.score[1] >= 21

    def __hash__(self) -> int:
        """Return the state as an index for a cache table."""
        bits = (
            f'{self.player_up}'
            f'{self.space_index[0]:04b}{self.space_index[1]:04b}'
            f'{self.score[0]:05b}{self.score[1]:05b}'
        )
        return int(bits, 2)

    def __str__(self) -> str:
        """Provide a user description of the state of the game."""
        return (
            f'Player 1 at {self.space_index[0] + 1}, score: {self.score[0]}, '
            f'Player 2 at {self.space_index[1] + 1}, score: {self.score[1]}. '
            f'Player up: {self.player_up + 1}.'
        )

    def go_deep(self) -> Tuple[int, int]:
        """Go a deeper game state."""
        index = hash(self)
        if index in self.cache:
            return self.cache[index]

        if not self.is_over():
            player_1_acc_wins = 0
            player_2_acc_wins = 0
            for dice in range(3, 10):
                next_state = self.roll(dice)
                player_1_wins, player_2_wins = next_state.go_deep()
                player_1_acc_wins += (
                    player_1_wins * UNIVERSE_MULTIPLIER[dice - 3]
                )
                player_2_acc_wins += (
                    player_2_wins * UNIVERSE_MULTIPLIER[dice - 3]
                )
                self.cache[index] = (player_1_acc_wins, player_2_acc_wins)
        else:
            if self.score[0] >= 21:
                self.cache[index] = (1, 0)
            else:
                self.cache[index] = (0, 1)
        return self.cache[index]


def deterministic_practice() -> None:
    """Deterministic die practice."""
    space_index = [4, 5]  # Input data
    score = [0, 0]

    die = list(range(1, 101))
    die_index = 0
    die_rolled = 0

    while score[0] < 1000 and score[1] < 1000:
        for player in (0, 1):
            roll = [
                die[die_index],
                die[(die_index + 1) % 100],
                die[(die_index + 2) % 100]
            ]
            die_index = (die_index + 3) % 100
            die_rolled += 3
            space_index[player] = (space_index[player] + sum(roll)) % 10
            score[player] += space_index[player] + 1
            if score[player] >= 1000:
                break
    losing_score = min(score[0], score[1])
    print(f'Part One: Losing score multiplied by number of rolls: '
          f'{losing_score * die_rolled}')


def multiple_universe_game() -> None:
    """Playing board game with Dirac Die."""
    game = GameState([4, 5])  # Game Input
    player_1_wins, player_2_wins = game.go_deep()
    if player_1_wins >= player_2_wins:
        wins_in_more_universes = player_1_wins
    else:
        wins_in_more_universes = player_2_wins
    print(f'Part Two: Player wins in most universes: {wins_in_more_universes}')


deterministic_practice()
multiple_universe_game()

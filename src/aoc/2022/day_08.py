#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Advent of Code 2022, day eight."""

INPUT_FILE = 'data/day_08.txt'


def main() -> None:
    """Calculate best tree house location."""
    matrix = []
    with open(INPUT_FILE, encoding='utf-8') as input_file:
        for line in input_file:
            matrix.append(list(line.strip()))
    hidden_count = 0
    best_scenic_score = 0
    for row in range(1, len(matrix) - 1):
        for col in range(1, len(matrix) - 1):
            tree = matrix[row][col]
            score_up = 0
            visible_up = True
            for work_row in range(row - 1, -1, -1):
                if visible_up:
                    score_up += 1
                visible_up = matrix[work_row][col] < tree and visible_up
            score_down = 0
            visible_down = True
            for work_row in range(row + 1, len(matrix)):
                if visible_down:
                    score_down += 1
                visible_down = matrix[work_row][col] < tree and visible_down
            score_left = 0
            visible_left = True
            for work_col in range(col - 1, -1, -1):
                if visible_left:
                    score_left += 1
                visible_left = matrix[row][work_col] < tree and visible_left
            score_right = 0
            visible_right = True
            for work_col in range(col + 1, len(matrix)):
                if visible_right:
                    score_right += 1
                visible_right = matrix[row][work_col] < tree and visible_right
            if visible_up or visible_down or visible_right or visible_left:
                best_scenic_score = max(
                    score_up * score_down * score_right * score_left,
                    best_scenic_score
                )
            else:
                hidden_count += 1

    visible_count = len(matrix) * len(matrix) - hidden_count
    print(f'Part One: Number of visible trees: {visible_count}')
    print(f'Part Two: Best Tree scenic score: {best_scenic_score}')


main()

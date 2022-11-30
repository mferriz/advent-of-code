#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Advent of Code 2021, day ten."""

INPUT_FILE = 'data/day_10.txt'


def main() -> None:
    """Get corrupted and incomplete scores."""
    with open(INPUT_FILE, encoding='utf-8') as input_file:
        corrupted_score = 0
        completer_scores = []

        chunk_open = {'(': ')', '[': ']', '{': '}', '<': '>'}
        chunk_close = {')': '(', ']': '[', '}': '{', '>': '<'}
        corrupted_scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
        completion_scores = {'(': 1, '[': 2, '{': 3, '<': 4}

        for line in input_file:
            tracker = []
            for elem in line.strip():
                if elem in chunk_open:
                    tracker.append(elem)
                elif not tracker or chunk_close[elem] != tracker.pop():
                    corrupted_score += corrupted_scores[elem]
                    break
            else:
                score = 0
                while tracker:
                    score = score * 5 + completion_scores[tracker.pop()]
                completer_scores.append(score)

        completer_scores = sorted(completer_scores)
        print(f'Part One: Total Score: {corrupted_score}')
        print(f'Part Two: Middle completion score: '
              f'{completer_scores[len(completer_scores) // 2]}')


main()

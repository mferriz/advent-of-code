#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Advent of Code 2021, day eight."""

INPUT_FILE = 'data/day_08.txt'


def main() -> None:
    """Decoding numbers."""
    part_one_number = 0
    part_two_number = 0
    with open(INPUT_FILE, encoding='utf-8') as input_file:
        for line in input_file:
            signal_pattern_str, digital_output_str = line.strip().split(' | ')
            signal_pattern_list = signal_pattern_str.split()
            signal_map = {}
            unclassified = []
            for signal_pattern in signal_pattern_list:
                signal_pattern = ''.join(sorted(signal_pattern))
                if len(signal_pattern) == 7:
                    signal_map[signal_pattern] = 8
                elif len(signal_pattern) == 2:
                    signal_map[signal_pattern] = 1
                    one_set = set(signal_pattern)
                elif len(signal_pattern) == 4:
                    signal_map[signal_pattern] = 4
                    four_set = set(signal_pattern)
                elif len(signal_pattern) == 3:
                    signal_map[signal_pattern] = 7
                else:
                    unclassified.append(signal_pattern)
            # Determine unclassified
            for signal_pattern in unclassified:
                signal_set = set(signal_pattern)
                # Only digits 0, 3 and 9 have same segments lit than digit 1.
                if signal_set & one_set == one_set:
                    if len(signal_set) == 5:
                        signal_map[signal_pattern] = 3
                    elif signal_set & four_set == four_set:
                        signal_map[signal_pattern] = 9
                    else:
                        signal_map[signal_pattern] = 0
                elif len(signal_pattern) == 6:
                    signal_map[signal_pattern] = 6
                # Pattern of number five matches three segments of
                # number four pattern.
                elif len(signal_set & four_set) == 3:
                    signal_map[signal_pattern] = 5
                else:
                    signal_map[signal_pattern] = 2

            # All digits are matched.
            digital_output_list = digital_output_str.split()
            number = 0
            for number_str in digital_output_list:
                if len(number_str) in (2, 3, 4, 7):
                    part_one_number += 1
                number = number * 10 + signal_map[''.join(sorted(number_str))]
            part_two_number += number

        print(f'Part One: Number occurrences of 1, 4, 7, 8: {part_one_number}')
        print(f'Part Two: Sum of all numbers decoded: {part_two_number}')


main()

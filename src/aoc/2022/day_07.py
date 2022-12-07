#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Advent of Code 2022, day seven."""

import re
from typing import Dict

INPUT_FILE = 'data/day_07.txt'
FILE_ENTRY = re.compile(r'(\d+)\s(\S+)')
TOTAL_DISK_SPACE = 70000000
MIN_UNUSED_SPACE = 30000000


def main() -> None:
    """Calculate directories sizes."""
    directory_sizes: Dict[str, int] = {}
    current_dir: str = '/'
    with open(INPUT_FILE, encoding='utf-8') as input_file:
        for line in input_file:
            line = line.strip()
            if line.startswith('$ cd '):  # Change directory
                directory = line[5:]
                if directory.startswith('/'):  # Absolute change
                    current_dir = directory
                elif directory == '..':
                    current_dir = current_dir.rsplit('/', 2)[0] + '/'
                else:
                    current_dir = f'{current_dir}{directory}/'
            elif (match := FILE_ENTRY.match(line)) is not None:
                file_size = int(match.group(1))
                temp_dir = current_dir
                while temp_dir != '/':
                    directory_sizes[temp_dir] = (
                        directory_sizes.setdefault(temp_dir, 0) + file_size
                    )
                    temp_dir = temp_dir.rsplit('/', 2)[0] + '/'
                directory_sizes[temp_dir] = (
                    directory_sizes.setdefault(temp_dir, 0) + file_size
                )
        sum_dir = 0
        for dir_size in directory_sizes.values():
            if dir_size < 100000:
                sum_dir += dir_size
        print(f'Part One: Sum of directory sizes of at most 100K: {sum_dir}')

        # Find the directory with just about the space needed.
        space_needed = (
            MIN_UNUSED_SPACE - (TOTAL_DISK_SPACE - directory_sizes['/'])
        )
        candidate_dir = ''
        candidate_size = TOTAL_DISK_SPACE
        for dir_name, dir_size in directory_sizes.items():
            if space_needed <= dir_size <= candidate_size:
                candidate_dir = dir_name
                candidate_size = dir_size
        print(f'Part Two: Candidate directory {candidate_dir}; '
              f'size: {candidate_size}')


main()

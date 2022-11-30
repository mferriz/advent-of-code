#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Execute scripts to recreate the solution of Advent of Code puzzles."""

import pathlib
import re
import subprocess
import sys

PUZZLE = re.compile(r'(?P<year>\d{4})\.(?P<day>\d{2})')
USAGE = """ \
Usage: aoc <YYYY.DD>

Execute a program that will solve the puzzle for Advent of Code of year YYYY
and day DD.

(C) 2021-2002 Mario A. Ferriz. All rights reserved.
"""


def main() -> None:
    """Main program to recreate solutions."""
    if len(sys.argv) != 2:
        print(f'{USAGE}')
        sys.exit(1)

    # Validate input
    if (match := PUZZLE.match(sys.argv[1])) is None:
        print(f'{USAGE}\nPlease provide the puzzle number in the '
              f'format YYYY.DD')
        sys.exit(1)

    # Obtain the base directory of the puzzle.
    cwd = pathlib.Path(__file__).expanduser().parent \
        / f"{match.group('year')}"
    executable = cwd / f"day_{match.group('day')}.py"

    # Execute program
    program = subprocess.run(executable, cwd=cwd, check=True)
    sys.exit(program.returncode)

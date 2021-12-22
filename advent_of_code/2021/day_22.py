#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Advent of Code 2021, day twenty two."""

import re
from typing import List, Tuple, Optional

INPUT_FILE = 'data/day_22.txt'
INSTRUCTION = re.compile(r'^(?P<action>off|on)\s'
                         r'x=(?P<x0>-?\d+)\.\.(?P<x1>-?\d+),'
                         r'y=(?P<y0>-?\d+)\.\.(?P<y1>-?\d+),'
                         r'z=(?P<z0>-?\d+)\.\.(?P<z1>-?\d+)$')


class Cuboid:
    """Model a cuboid."""

    def __init__(self, x: range, y: range, z: range) -> None:
        """Initialize a cuboid."""
        self.x = x
        self.y = y
        self.z = z
        self.cube_count = (
            abs(x.stop - x.start) * abs(y.stop - y.start)
            * abs(z.stop - z.start)
        )

    def __str__(self) -> str:
        """Produce a string representation of a cuboid."""
        return (f'X: ({self.x.start}, {self.x.stop - 1}) '
                f'Y: ({self.y.start}, {self.y.stop - 1}) '
                f'Z: ({self.z.start}, {self.z.stop - 1}) '
                f'Count: {self.cube_count}')

    @staticmethod
    def _dimension_overlap(dim_1: range,
                           dim_2: range) -> Optional[range]:
        """Find overlap in a dimension of a cuboid (x, y, or z)."""
        overlap = None
        # 1. Check if one dimensions contains the other
        if dim_1.start <= dim_2.start and dim_1.stop >= dim_2.stop:
            overlap = dim_2
        elif dim_2.start <= dim_1.start and dim_2.stop >= dim_1.stop:
            overlap = dim_1
        # 2. Check if one dimension starts in another dimension
        elif dim_1.start in dim_2:
            overlap = range(dim_1.start, dim_2.stop)
        elif dim_2.start in dim_1:
            overlap = range(dim_2.start, dim_1.stop)
        return overlap

    def intersection(self, cuboid: "Cuboid") -> Optional["Cuboid"]:
        """Find if there is any intersection between cuboids."""
        intersection_cuboid = None
        x_overlap = self._dimension_overlap(self.x, cuboid.x)
        if x_overlap is not None:
            y_overlap = self._dimension_overlap(self.y, cuboid.y)
            if y_overlap is not None:
                z_overlap = self._dimension_overlap(self.z, cuboid.z)
                if z_overlap is not None:
                    intersection_cuboid = Cuboid(x_overlap,
                                                 y_overlap,
                                                 z_overlap)
        # pdb.set_trace()
        return intersection_cuboid


def lit_cube_count(instructions: List[Tuple[str, Cuboid]],
                   initialization_cuboid: Cuboid = None) -> int:
    """Count the number of lit cubes after all instructions execute."""
    lit_count = 0
    lit_cuboids = []
    dark_cuboids = []
    for action, cuboid in instructions:
        if initialization_cuboid is not None:
            cuboid = cuboid.intersection(initialization_cuboid)
            if cuboid is None:
                continue
        new_lit_cuboids = []
        new_dark_cuboids = []
        if action == 'on':
            new_lit_cuboids.append(cuboid)
            lit_count += cuboid.cube_count
        # For all lit cuboids that intersect, create a compensation cuboid.
        for lit_cuboid in lit_cuboids:
            compensation_cuboid = cuboid.intersection(lit_cuboid)
            if compensation_cuboid is not None:
                # pdb.set_trace()
                # This is for compensate double counting.
                lit_count -= compensation_cuboid.cube_count
                new_dark_cuboids.append(compensation_cuboid)
        # For all dark cuboids that intersect, create a compensation cuboid
        for dark_cuboid in dark_cuboids:
            compensation_cuboid = cuboid.intersection(dark_cuboid)
            if compensation_cuboid is not None:
                # pdb.set_trace()
                # Compensate double counting
                lit_count += compensation_cuboid.cube_count
                new_lit_cuboids.append(compensation_cuboid)
        lit_cuboids.extend(new_lit_cuboids)
        dark_cuboids.extend(new_dark_cuboids)
    return lit_count


def main() -> None:
    """Reboot sequences for reactor. Need to count cubes lit."""
    initialization_cuboid = Cuboid(range(-50, 51),
                                   range(-50, 51),
                                   range(-50, 51))
    instructions = []

    with open(INPUT_FILE, encoding='utf-8') as input_file:
        for line in input_file:
            match = INSTRUCTION.match(line.strip())
            if match is not None:
                x = range(int(match.group('x0')), int(match.group('x1')) + 1)
                y = range(int(match.group('y0')), int(match.group('y1')) + 1)
                z = range(int(match.group('z0')), int(match.group('z1')) + 1)
                cuboid = Cuboid(x, y, z)
                instructions.append((match.group('action'), cuboid))

    print(f'Part One: Lit cubes in initialization cuboid: '
          f'{lit_cube_count(instructions, initialization_cuboid)}')
    print(f'Part Two: Total lit cubes: '
          f'{lit_cube_count(instructions)}')


main()

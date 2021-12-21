#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Advent of Code 2021, day nineteen."""

from typing import List, Optional, Tuple

from bitarray import bitarray

INPUT_FILE = 'data/day_19.txt'
MIN_BEACONS = 10
MAX_UNITS = 1000


def correlate(dimension_a: bitarray,
              dimension_b: bitarray) -> Optional[int]:
    """Correlate two lists. If they can correlate, an offset is returned.

    Args:
        dimension_a (bitarray): The reference.
        dimension_b (bitarray): The list to correlate.

    Returns:
        int: If both lists can correlate the offset of dimension_b to
        dimension_a, or None if they don't.

    """
    offset = 0
    best_count = 0
    best_offset = 0
    # Most fortunate case: both bitarrays are aligned.
    if (dimension_a & dimension_b).count() >= MIN_BEACONS:
        return offset
    work = dimension_b.copy()
    # Shift bits to left
    while work.count():
        work <<= 1
        offset -= 1
        if (dimension_a & work).count() >= best_count:
            best_offset = offset
            best_count = (dimension_a & work).count()
    if best_count >= MIN_BEACONS:
        return best_offset
    work = dimension_b.copy()
    offset = 0
    best_count = 0
    best_offset = 0
    # Shift bits to right
    while work.count():
        work >>= 1
        offset += 1
        if (dimension_a & work).count() >= best_count:
            best_offset = offset
            best_count = (dimension_a & work).count()
    return best_offset if best_count >= MIN_BEACONS else None


def correlate_scanners(
        scanner_a: List[bitarray],
        scanner_b: List[bitarray]) -> Tuple[Tuple[int, int, int],
                                            Tuple[str, str, str]]:
    """Correlate two scanners. Return x, y z if any."""
    axis = ['x', 'y', 'z']
    # Have handy axis reversal.
    scanner_b_reverse = [scanner_b[0].copy(),
                         scanner_b[1].copy(),
                         scanner_b[2].copy()]
    scanner_b_reverse[0].reverse()
    scanner_b_reverse[1].reverse()
    scanner_b_reverse[2].reverse()
    # Prepare results
    offsets = [None, None, None]
    offsets_type = [None, None, None]
    for axis0 in range(3):
        for axis1 in range(3):
            offset = correlate(scanner_a[axis0],
                               scanner_b[axis1])
            if offset is not None:
                offsets[axis0] = offset
                offsets_type[axis0] = axis[axis1]
            else:
                offset = correlate(scanner_a[axis0],
                                   scanner_b_reverse[axis1])
                if offset is not None:
                    offsets[axis0] = -offset
                    offsets_type[axis0] = f'r{axis[axis1]}'
    return (offsets, offsets_type)


def transform(beacon_pos: list, offsets: list, offsets_types: list) -> None:
    """Transform beacon positions relative to a scanner."""
    x_prime: int = 0
    y_prime: int = 0
    z_prime: int = 0
    new_positions = []

    for x, y, z in beacon_pos:
        if offsets_types[0] == 'x':
            x_prime = x + offsets[0]
        elif offsets_types[0] == 'rx':
            x_prime = -x - offsets[0]
        elif offsets_types[0] == 'y':
            x_prime = y + offsets[0]
        elif offsets_types[0] == 'ry':
            x_prime = -y - offsets[0]
        elif offsets_types[0] == 'z':
            x_prime = z + offsets[0]
        else:
            x_prime = -z - offsets[0]

        if offsets_types[1] == 'x':
            y_prime = x + offsets[1]
        elif offsets_types[1] == 'rx':
            y_prime = -x - offsets[1]
        elif offsets_types[1] == 'y':
            y_prime = y + offsets[1]
        elif offsets_types[1] == 'ry':
            y_prime = -y - offsets[1]
        elif offsets_types[1] == 'z':
            y_prime = z + offsets[1]
        else:
            y_prime = -z - offsets[1]

        if offsets_types[2] == 'x':
            z_prime = x + offsets[2]
        elif offsets_types[2] == 'rx':
            z_prime = -x - offsets[2]
        elif offsets_types[2] == 'y':
            z_prime = y + offsets[2]
        elif offsets_types[2] == 'ry':
            z_prime = -y - offsets[2]
        elif offsets_types[2] == 'z':
            z_prime = z + offsets[2]
        else:
            z_prime = -z - offsets[2]
        new_positions.append((x_prime, y_prime, z_prime))
    return new_positions


def correlate_all(beacon_pos: list, scanner_reports: list,
                  scanner_pos: list) -> Tuple[list, int]:
    """Correlate and normalize scanner reports."""
    correlated = [0]
    not_correlated = [x for x in range(1, len(beacon_pos))]
    correlation_offsets = {0: [0, 0, 0]}
    correlation_offsets_types = {0: ['x', 'y', 'z']}
    correlation_base = {0: 0}
    change = True
    correlation_cache = []
    scanner_pos[0] = (0, 0, 0)
    for scanner in range(len(beacon_pos)):
        correlation_cache.append([False for _x in range(len(beacon_pos))])
    while len(not_correlated) and change:
        change = False
        for index_a in range(len(correlated)):
            a = correlated[index_a]
            new_correlated = []
            for b in sorted(not_correlated):
                if correlation_cache[a][b]:
                    continue
                correlation_cache[a][b] = True
                offsets, offsets_types = correlate_scanners(scanner_reports[a],
                                                            scanner_reports[b])
                if offsets[0] is not None and offsets[1] is not None \
                   and offsets[2] is not None:
                    correlation_offsets[b] = [
                        offsets[0],
                        offsets[1],
                        offsets[2]
                    ]
                    correlation_offsets_types[b] = [
                        offsets_types[0],
                        offsets_types[1],
                        offsets_types[2]
                    ]
                    correlation_base[b] = a
                    base = b
                    scanner_position = [(0, 0, 0)]
                    new_positions = beacon_pos[b]
                    while base:
                        new_positions = transform(new_positions,
                                                  offsets, offsets_types)
                        scanner_position = transform(scanner_position,
                                                     offsets, offsets_types)
                        base = correlation_base[base]
                        offsets = correlation_offsets[base]
                        offsets_types = correlation_offsets_types[base]
                    # Store transformed positions
                    beacon_pos[b] = new_positions
                    scanner_pos[b] = scanner_position[0]
                    change = True
                    new_correlated.append(b)
            for scanner in new_correlated:
                correlated.append(scanner)
                not_correlated.remove(scanner)


def main() -> None:
    """Scanner correlator."""
    scanner_report = []
    beacon_pos = []
    positions = []
    x_readings = bitarray(2 * MAX_UNITS + 1)
    y_readings = bitarray(2 * MAX_UNITS + 1)
    z_readings = bitarray(2 * MAX_UNITS + 1)
    x_readings.setall(0)
    y_readings.setall(0)
    z_readings.setall(0)
    with open(INPUT_FILE, encoding='utf-8') as input_file:
        for line in input_file:
            line = line.strip()
            if not line:
                scanner_report.append([
                    x_readings.copy(),
                    y_readings.copy(),
                    z_readings.copy()
                ])
                beacon_pos.append(positions)
                positions = []
                x_readings.setall(0)
                y_readings.setall(0)
                z_readings.setall(0)
                continue
            if line.startswith('--- scanner'):
                continue
            x, y, z = [int(number) for number in line.split(',')]
            positions.append((x, y, z))
            x_readings[x + MAX_UNITS] = 1
            y_readings[y + MAX_UNITS] = 1
            z_readings[z + MAX_UNITS] = 1
        scanner_report.append([
            x_readings,
            y_readings,
            z_readings
        ])
        beacon_pos.append(positions)

    scanner_positions = []
    for _scanner in range(len(beacon_pos)):
        scanner_positions.append(None)
    correlate_all(beacon_pos, scanner_report, scanner_positions)
    beacons = set()
    for positions in beacon_pos:
        beacons.update(set(positions))
    print(f'Part One: Number of beacons: {len(beacons)}')

    largest_manhattan_number = 0
    for scanner_a in scanner_positions:
        for scanner_b in scanner_positions:
            manhattan = (
                abs(scanner_a[0] - scanner_b[0])
                + abs(scanner_a[1] - scanner_b[1])
                + abs(scanner_a[2] - scanner_b[2])
            )
            if manhattan > largest_manhattan_number:
                largest_manhattan_number = manhattan
    print(f'Part Two: Largest Manhattan Number {largest_manhattan_number}')


main()

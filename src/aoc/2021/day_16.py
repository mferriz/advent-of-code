#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Advent of Code 2021, day sixteen."""

from enum import Enum
from typing import Tuple

import bitarray
from bitarray.util import ba2int, hex2ba

INPUT_FILE = 'data/day_16.txt'
CONTINUATION_NUMBER = 0x10


class BITS(Enum):
    """Operations defined as part of the BITS language."""

    SUM = 0
    PRODUCT = 1
    MINIMUM = 2
    MAXIMUM = 3
    LITERAL = 4
    GREATER_THAN = 5
    LESS_THAN = 6
    EQUAL_TO = 7


def parse_packet(
        program: list,
        packet: bitarray.bitarray,
        count: int = 0) -> int:
    """Parse packet and return the final index offset."""
    # Extract the version
    index = 0
    while index < len(packet):
        if packet[index:] in bitarray.frozenbitarray('0000000'):
            # Padding
            index += len(packet[index:])
            break
        version = ba2int(packet[index:index + 3])
        type_id = BITS(ba2int(packet[index + 3:index + 6]))
        index += 6  # Placed after the type id.
        if type_id == BITS.LITERAL:
            literal_value = 0
            number = ba2int(packet[index:index + 5])
            literal_value = number & 0xF
            index += 5
            while number & CONTINUATION_NUMBER:
                number = ba2int(packet[index:index + 5])
                literal_value = (literal_value << 4) | number & 0xF
                index += 5
            program.append((version, type_id, literal_value))
        else:  # Must be an operator
            length_type_id = packet[index]
            index += 1
            if length_type_id == 0:
                length = ba2int(packet[index:index + 15])
                index += 15
                sub_program = []
                _ = (
                    parse_packet(sub_program,
                                 packet[index:index + length])
                )
                program.append((version, type_id, sub_program))
                index += length
            else:  # Must be one
                number_of_subpackets = ba2int(packet[index:index + 11])
                index += 11
                sub_program = []
                index_adv = (
                    parse_packet(sub_program,
                                 packet[index:],
                                 count=number_of_subpackets)
                )
                program.append((version, type_id, sub_program))
                index += index_adv
        if count:
            count = count - 1
            if not count:
                break
    return index


def sum_versions(program: list) -> int:
    """Sum all versions of all packets."""
    accumulator = 0
    for version, data_type, data in program:
        accumulator += version
        if data_type != BITS.LITERAL:
            accumulator += sum_versions(data)
    return accumulator


def run_program(type_id: BITS, data: Tuple[int, BITS, int]) -> int:
    """Run a BITS program and return the result."""
    literals = []
    return_value = 0
    for _version, datum_type, datum in data:
        if datum_type == BITS.LITERAL:
            literals.append(datum)
        else:
            literals.append(run_program(datum_type, datum))
    if type_id == BITS.SUM:
        return_value = sum(literals)
    elif type_id == BITS.PRODUCT:
        accumulator = 1
        for literal in literals:
            accumulator *= literal
        return_value = accumulator
    elif type_id == BITS.MINIMUM:
        return_value = min(literals)
    elif type_id == BITS.MAXIMUM:
        return_value = max(literals)
    elif type_id == BITS.GREATER_THAN:
        return_value = 1 if literals[0] > literals[1] else 0
    elif type_id == BITS.LESS_THAN:
        return_value = 1 if literals[0] < literals[1] else 0
    elif type_id == BITS.EQUAL_TO:
        return_value = 1 if literals[0] == literals[1] else 0
    else:
        return_value = literals[0]
    return return_value


def main() -> None:
    """Read hexadecimal string and converted to binary string."""
    with open(INPUT_FILE, encoding='utf-8') as input_file:
        packet = hex2ba(input_file.readline().strip())
    program = []
    parse_packet(program, packet)
    print(f'Part One: Sum of all versions parsed: {sum_versions(program)}')
    result = run_program(program[0][1], program[0][2])
    print(f'Part Two: Result of all operations: {result}')


main()

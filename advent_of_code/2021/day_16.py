#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Advent of Code 2021, day sixteen."""

from enum import Enum

INPUT_FILE = 'data/day_16.txt'
HEX_TO_BIN = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}
CONTINUATION_NUMBER = 0x10


class BITS(Enum):
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
        packet: str,
        level: str,
        count: int = 0) -> int:
    """Parse packet and return the final index offset."""
    # print(f'{level}Packet: {packet}, {len(packet)}')
    # Extract the version
    index = 0
    while index < len(packet):
        if packet[index:] in '0000000':
            # Padding
            # print(f'{level}Padding: {len(packet[index:])}')
            index += len(packet[index:])
            break
        version = int(packet[index:index+3], 2)
        type_id = BITS(int(packet[index+3:index+6], 2))
        index += 6  # Placed after the type id.
        if type_id == BITS.LITERAL:
            literal_value = 0
            number = int(packet[index:index+5], 2)
            literal_value = number & 0xF
            index += 5
            while number & CONTINUATION_NUMBER:
                number = int(packet[index:index+5], 2)
                literal_value = (literal_value << 4) | number & 0xF
                index += 5
                # print(f'Index: {index}')
            program.append((version, type_id, literal_value))
            # print(f'{level}Version: {version}, Type ID: {type_id}, '
            #       f'Literal: {literal_value}')
        else:  # Must be an operator
            length_type_id = packet[index]
            index += 1
            if length_type_id == '0':
                length = int(packet[index:index+15], 2)
                # print(f'{level}Version: {version}, Type ID: {type_id}, '
                #       f'Length {length}')
                index += 15
                # pdb.set_trace()
                sub_program = []
                _ = (
                    parse_packet(sub_program,
                                 packet[index:index+length],
                                 level=level + ' ')
                )
                program.append((version, type_id, sub_program))
                index += length
            else:  # Must be one
                number_of_subpackets = int(packet[index:index+11], 2)
                # print(f'{level}Version: {version}, Type ID: {type_id}, '
                #       f'Subpackets {number_of_subpackets}')
                index += 11
                sub_program = []
                index_adv = (
                    parse_packet(sub_program,
                                 packet[index:],
                                 level=level + ' ',
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


def run_program(type_id: BITS, data) -> int:
    """Run a BITS program and return the result."""
    literals = []
    for _version, datum_type, datum in data:
        if datum_type == BITS.LITERAL:
            literals.append(datum)
        else:
            literals.append(run_program(datum_type, datum))
    if type_id == BITS.SUM:
        return sum(literals)
    if type_id == BITS.PRODUCT:
        accumulator = 1
        for literal in literals:
            accumulator *= literal
        return accumulator
    if type_id == BITS.MINIMUM:
        return min(literals)
    if type_id == BITS.MAXIMUM:
        return max(literals)
    if type_id == BITS.GREATER_THAN:
        return 1 if literals[0] > literals[1] else 0
    if type_id == BITS.LESS_THAN:
        return 1 if literals[0] < literals[1] else 0
    if type_id == BITS.EQUAL_TO:
        return 1 if literals[0] == literals[1] else 0
    return literals[0]


def main() -> None:
    """Read hexadecimal string and converted to binary string."""
    with open(INPUT_FILE, encoding='utf-8') as input_file:
        line = input_file.readline().strip()
    packet = ''.join([HEX_TO_BIN[x] for x in list(line)])
    program = []
    parse_packet(program, packet, level='')
    print(f'Part One: Sum of all versions parsed: {sum_versions(program)}')
    result = run_program(program[0][1], program[0][2])
    print(f'Part Two: Result of all operations: {result}')


main()

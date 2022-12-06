#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Advent of Code 2022, day six."""

INPUT_FILE = 'data/day_06.txt'


def main() -> None:
    """Find and report start-of-packet and start-of-message."""
    start_of_packet_buffer = ''
    start_of_message_buffer = ''
    start_of_packet_found = False
    with open(INPUT_FILE, encoding='utf-8') as input_file:
        # Get all file content
        data = input_file.read()
    for index in range(len(data)):
        if not start_of_packet_found:
            start_of_packet_buffer += data[index]
            if len(start_of_packet_buffer) > 4:
                start_of_packet_buffer = start_of_packet_buffer[1:]
            if len(set(start_of_packet_buffer)) == 4:
                print(f'Part One: Start of packet: {index + 1}')
                start_of_packet_found = True
        start_of_message_buffer += data[index]
        if len(start_of_message_buffer) > 14:
            start_of_message_buffer = start_of_message_buffer[1:]
        if len(set(start_of_message_buffer)) == 14:
            print(f'Part Two: Start of message: {index + 1}')
            break


main()

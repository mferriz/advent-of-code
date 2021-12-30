#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Advent of Code 2020, day four."""

import re

INPUT_FILE = 'data/day_04.txt'
HEIGHT = re.compile(r'^(\d+)(cm|in)$')
HAIR_COLOR = re.compile(r'^#[0-9a-f]{6}$')
PASSPORT_NUMBER = re.compile(r'^[0-9]{9}$')


def main() -> None:
    """Passport processing."""
    expected_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    field = {}
    with open(INPUT_FILE, encoding='utf-8') as input_file:
        passports_with_req_fields = 0
        valid_passports = 0
        for passport_data in input_file.read().split('\n\n'):
            passport = {}
            for field in passport_data.split():
                key, value = field.split(':')
                passport[key] = value
            if expected_fields & set(passport.keys()) == expected_fields:
                passports_with_req_fields += 1
                if (match := HEIGHT.match(passport['hgt'])) is None:
                    continue
                hgt_value, hgt_units = int(match.group(1)), match.group(2)
                if (len(passport['byr']) == 4
                    and 1920 <= int(passport['byr']) <= 2002
                    and len(passport['iyr']) == 4
                    and 2010 <= int(passport['iyr']) <= 2020
                    and len(passport['eyr']) == 4
                    and 2020 <= int(passport['eyr']) <= 2030
                    and ((hgt_units == 'cm' and 150 <= hgt_value <= 193)
                         or (hgt_units == 'in' and 59 <= hgt_value <= 76))
                    and HAIR_COLOR.match(passport['hcl']) is not None
                    and PASSPORT_NUMBER.match(passport['pid']) is not None
                    and passport['ecl'] in ['amb', 'blu', 'brn', 'gry',
                                            'grn', 'hzl', 'oth']):
                    valid_passports += 1

    print(f'Part One: Passports with required fields: '
          f'{passports_with_req_fields}')
    print(f'Part Two: Valid Passports: {valid_passports}')


main()

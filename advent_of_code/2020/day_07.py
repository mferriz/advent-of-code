#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Advent of Code 2020, day seven."""

import collections
from typing import Dict, List, Set

INPUT_FILE = 'data/day_07.txt'


def bags_colors_contained(contained: List[str], color: str) -> Set[str]:
    """Determine bags colors that can contain a bag of a color."""
    bags = set()
    if color in contained:
        for contained_bag in contained[color]:
            bags.add(contained_bag)
            bags |= bags_colors_contained(contained, contained_bag)
    return bags


def quantity_contained(container: Dict[str, collections.Counter],
                       color: str) -> int:
    """Quantity of bags contained."""
    counter = 0
    if color in container and container[color] is not None:
        for bag_color, quantity in container[color].items():
            counter += (
                quantity * (1 + quantity_contained(container, bag_color))
            )
    return counter


def main() -> None:
    """Process luggage."""
    with open(INPUT_FILE, encoding='utf-8') as input_file:
        container = {}
        contained = {}
        for line in input_file:
            container_bag, contains = line.strip().split(' bags contain ')
            if contains == 'no other bags.':
                container[container_bag] = None
            else:
                contains_list = (
                    contains.replace(' bags', '').replace(' bag', '')
                    .replace('.', '')
                ).split(', ')
                container[container_bag] = collections.Counter()
                for detail in contains_list:
                    quantity, color = detail.split(maxsplit=1)
                    container[container_bag][color] = int(quantity)
                    if color not in contained:
                        contained[color] = []
                    contained[color].append(container_bag)

    print(f'Part One: Bags that have at least one shiny gold bag: '
          f'{len(bags_colors_contained(contained, "shiny gold"))}')
    print(f'Part Two: Quantity of individual bags in shiny gold bags: '
          f'{quantity_contained(container, "shiny gold")}')


main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Advent of Code 2021, day twelve."""

import copy

INPUT_FILE = 'data/day_12.txt'


def find_routes(segments, route, rule):
    """Find complete routes from start to finish."""
    routes = []
    for next_segment in segments[route[-1]]:
        work_route = copy.deepcopy(route)
        work_route.append(next_segment)
        if next_segment == 'end':
            routes.extend([work_route])
        elif rule == 'part one':  # One small cave can be visited once.
            if next_segment[0].islower() and next_segment in route:
                continue
            routes.extend(find_routes(segments, work_route, rule))
        else:
            # One small cave can be visited twice,
            # Rest of small caves only once.
            small_caves = set()
            twice_occurrence = False
            for cave in work_route:
                if cave[0].islower():  # Small cave
                    if cave not in small_caves:
                        small_caves.add(cave)
                    elif twice_occurrence:
                        break
                    else:
                        twice_occurrence = True
            else:
                routes.extend(find_routes(segments, work_route, rule))
    return routes


def main() -> None:
    """Find all paths."""
    segments = {}
    with open(INPUT_FILE, encoding='utf-8') as input_file:
        for line in input_file:
            start, end = line.strip().split('-')
            if start != 'end' and end != 'start':
                if start not in segments:
                    segments[start] = [end]
                else:
                    segments[start].append(end)
            if start != 'start' and end != 'end' \
               or end == 'start' or start == 'end':
                if end not in segments:
                    segments[end] = [start]
                else:
                    segments[end].append(start)

    routes = find_routes(segments, ['start'], 'part one')
    print(f'Part One: Number of paths: {len(routes)}')
    routes = find_routes(segments, ['start'], 'part two')
    print(f'Part Two: Number of paths: {len(routes)}')


main()

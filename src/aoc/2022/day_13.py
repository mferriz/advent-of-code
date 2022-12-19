#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Advent of Code 2022, day thirteen."""

INPUT_FILE = 'data/day_13.txt'


def compare(arg_a, arg_b) -> int:  # noqa: ANN001
    """Compare two arguments. Arguments can be list or integer.

    Args:
        arg_a (Union[List, int]): List of integers or lists.
        arg_b (Union[List, int]): List of integers or lists.

    Returns:
        Negative if right order; positive if not in right order;
        Zero if inconclusive.

    """
    # Compare right away if arguments are integers.
    if isinstance(arg_a, int) and isinstance(arg_b, int):
        return arg_a - arg_b

    # Both sides must be lists to continue.
    list_a = [arg_a] if isinstance(arg_a, int) else arg_a
    list_b = [arg_b] if isinstance(arg_b, int) else arg_b

    result = 0
    while list_a or list_b:
        if not list_a:  # No elements in A. They are in right order.
            return -1
        if not list_b:
            return 1  # No elements in B. They are not in right order.
        if result := compare(list_a.pop(0), list_b.pop(0)):
            break
    return result


def main() -> None:
    """Indices of pairs."""
    with open(INPUT_FILE, encoding='utf-8') as input_file:
        pairs = input_file.read().strip().split('\n\n')
    sum_of_indices = 0
    for index, pair in enumerate(pairs, start=1):
        side_a, side_b = pair.split('\n')
        # pylint: disable=eval-used
        if compare(eval(side_a), eval(side_b)) <= 0:  # noqa: SCS101
            sum_of_indices += index

    print(f'Part One: Sum of indices: {sum_of_indices}')


main()

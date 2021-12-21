#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Advent of Code 2021, day twenty."""

from typing import List, Tuple

from bitarray import bitarray


INPUT_FILE = 'data/day_20.txt'


def obtain_spot_enhancing_index(image: List[bitarray],
                                row: int, col: int) -> int:
    """Obtain the enhancing index for the enhancing algorithm."""
    spot = ''
    for pixel_row in range(row - 1, row + 2):
        for pixel_col in range(col - 1, col + 2):
            spot += f'{image[pixel_row][pixel_col]}'
    return int(spot, 2)


def enhance_image(image: List[bitarray], border: int,
                  algorithm: bitarray) -> Tuple[List[bitarray], int]:
    """Enhance an image presented as a list of bitarrays."""

    work_image = []
    # Encase new image in border of two pixels.
    # Start adding top border.
    border_line = f'{border}' * (len(image[0].to01()) + 4)
    work_image.append(bitarray(border_line))
    work_image.append(bitarray(border_line))
    for pixel_line in image:
        bits = pixel_line.copy()
        bits.insert(0, border)  # Adding two pixels of border to left
        bits.insert(0, border)
        bits.append(border)  # Adding two pixels of border to right
        bits.append(border)
        work_image.append(bits)
    # Bottom border
    work_image.append(bitarray(border_line))
    work_image.append(bitarray(border_line))
    new_image = []
    for line_number in range(1, len(work_image) - 1):
        new_image_line = ''
        for pixel_number in range(1, len(work_image[0].to01()) - 1):
            index = obtain_spot_enhancing_index(work_image,
                                                line_number, pixel_number)
            new_image_line += f'{algorithm[index]}'
        new_image.append(bitarray(new_image_line))
    new_border = algorithm[border]
    return new_image, new_border


with open(INPUT_FILE, encoding='utf-8') as input_file:
    algorithm, input_image = input_file.read().split('\n\n')
    # Remove carriage returns in algorithm; replace dots for zeroes
    # and # to ones.
    algorithm = algorithm.replace('\n', '').replace('.', '0').replace('#', '1')
enhancing_algorithm = bitarray(algorithm)

image = [bitarray(x.replace('.', '0').replace('#', '1'))
         for x in input_image.splitlines()]
border = 0
for enhance_steps in range(50):
    new_image, border = enhance_image(image, border, enhancing_algorithm)
    if enhance_steps == 1:
        count_lit = 0
        for line in new_image:
            count_lit += line.count()
        print(f'Part One: Count of pixels lit after enhancing twice: '
              f'{count_lit}')
    image = new_image
count_lit = 0
for line in new_image:
    count_lit += line.count()
print(f'Part Two: Count of pixels lit after enhancing fifty times: '
      f'{count_lit}')

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Advent of Code 2021, day fifteen."""

import numpy

INPUT_FILE = 'data/day_15.txt'
HIGH_RISK = 1000000


class PathFinder:
    """Class that finds the lowest total risk path."""

    def __init__(self, matrix: numpy.ndarray) -> None:
        """Initialize."""
        self.matrix = matrix
        # Risk Cache
        self.risk = numpy.full(self.matrix.shape, HIGH_RISK, dtype=int)
        self.risk[0][0] = 0
        # Mark all nodes as unvisited
        self.visited = numpy.full(self.matrix.shape, False, dtype=bool)

    def calculate_risk(self, row: int, col: int) -> None:
        """Implementation of Dijkstra shortest path in a matrix."""
        # Obtain unvisited neighbors with same row or same column
        neighbors = []
        for neighbor_row in range(row - 1, row + 2):
            for neighbor_col in range(col - 1, col + 2):
                if (0 <= neighbor_row < self.matrix.shape[0]
                    and 0 <= neighbor_col < self.matrix.shape[1]
                    and ((neighbor_row == row) != (neighbor_col == col))
                        and not self.visited[neighbor_row][neighbor_col]):
                    neighbors.append((neighbor_row, neighbor_col))

        cell_risk = self.risk[row][col] if row or col else 0
        for neighbor_row, neighbor_col in neighbors:
            risk = cell_risk + self.matrix[neighbor_row][neighbor_col]
            if risk < self.risk[neighbor_row][neighbor_col]:
                self.risk[neighbor_row][neighbor_col] = risk

        self.visited[row][col] = True

    def least_risk(self) -> int:
        """Obtain least risk."""
        dest_row = self.matrix.shape[0] - 1
        dest_col = self.matrix.shape[1] - 1
        while (not numpy.all(self.visited)
               and not self.visited[dest_row][dest_col]):
            # Get candidates for next iteration.
            candidates = \
                numpy.argwhere((self.risk < HIGH_RISK) & ~self.visited)
            least_risk = HIGH_RISK
            for candidate in candidates:
                row = candidate[0]
                col = candidate[1]
                risk = self.risk[row][col]
                if risk < least_risk:
                    least_risk = risk
                    candidate_row = row
                    candidate_col = col

            self.calculate_risk(candidate_row, candidate_col)

        return self.risk[dest_row][dest_col]


def main() -> None:
    """Assess risk level."""
    input_rows = []
    with open(INPUT_FILE, encoding='utf-8') as input_file:
        for line in input_file:
            input_rows.append([int(x) for x in list(line.strip())])
    matrix = numpy.array(input_rows, dtype=int)
    path_finder = PathFinder(matrix)
    risk = path_finder.least_risk()
    print(f'Part One: Risk: {risk}')

    # Create 5x5 matrix
    new_matrix = numpy.tile(matrix, [5, 5])
    for row in range(0, new_matrix.shape[0]):
        for col in range(0, new_matrix.shape[1]):
            new_matrix[row][col] += (
                row // matrix.shape[0] + col // matrix.shape[1]
            )
            if new_matrix[row][col] > 9:
                new_matrix[row][col] -= 9
    path_finder = PathFinder(new_matrix)
    risk = path_finder.least_risk()
    print(f'Part Two: Risk: {risk}')


main()

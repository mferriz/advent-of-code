#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Advent of Code 2021, day twenty three."""

import copy
from typing import Dict

EMPTY_HALL = '...........'
VERY_EXPENSIVE = 1000000


class AmphipodDiagram:
    """Diagram of amphipods."""

    # Dictionary of a hash and energy cost.
    cache: Dict[int, int] = {}

    def __init__(self, groups: Dict[str, str]) -> None:
        """Initialize an amphipod diagram with input state."""
        self.group = groups
        self.group_depth = len(self.group['A'])
        self.hall = EMPTY_HALL
        self.energy_per_step = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
        self.hall_intersection = {'A': 2, 'B': 4, 'C': 6, 'D': 8}

    def is_final(self) -> bool:
        """Report whether the amphipod diagram is final."""
        for name in ['A', 'B', 'C', 'D']:
            if self.group[name] != name * self.group_depth:
                return False
        return True

    def perform_forced_moves(self) -> int:
        """Perform a series of moves that are forced because of least cost.

           Some times there are moves of least cost, like moving an amphipod
           from the hall to its group or moving an amphipod from a group
           to its final group. The moves have to be made right away to clear
           space.
        """
        energy_spent = 0
        keep_moving = True
        move_count = 0

        while keep_moving:
            # 1. Performing moves from hall to final group.
            keep_moving = False
            for position, amphipod in enumerate(self.hall):
                if amphipod == '.':
                    continue
                # Amphipod group must be empty or only containing same elements.
                if self.group[amphipod] == amphipod * len(self.group[amphipod]):
                    # Make sure the amphipod has a clear path to intersection
                    intersection = self.hall_intersection[amphipod]
                    if intersection > position:
                        hall_segment = self.hall[position + 1:intersection + 1]
                    else:
                        hall_segment = self.hall[intersection:position]
                    if hall_segment == '.' * len(hall_segment):
                        steps = (
                            len(hall_segment)
                            + self.group_depth - len(self.group[amphipod])
                        )
                        energy_spent += (
                            self.energy_per_step[amphipod] * steps
                        )
                        self.hall = (
                            self.hall[0:position] + '.'
                            + self.hall[position+1:]
                        )
                        self.group[amphipod] += amphipod
                        keep_moving = True
                        move_count += 1
                        break
            if keep_moving:  # Move all amphipods in hall first
                continue

            # 2. Performing moves with amphipods in incorrect groups
            #    to final group.
            for group_name in ['A', 'B', 'C', 'D']:
                if self.group[group_name]:  # Must have elements in group
                    amphipod = self.group[group_name][-1]
                    # Final group must be empty or contain same elements
                    if (amphipod != group_name
                        and self.group[amphipod] ==
                        amphipod * len(self.group[amphipod])):
                        # There must be a clear path between intersections
                        src_inter = self.hall_intersection[group_name]
                        dst_inter = self.hall_intersection[amphipod]
                        if src_inter < dst_inter:
                            hall_segment = self.hall[src_inter:dst_inter + 1]
                        else:
                            hall_segment = self.hall[dst_inter:src_inter + 1]
                        if hall_segment == '.' * len(hall_segment):
                            keep_moving = True
                            move_count += 1
                            steps = (
                                len(hall_segment)
                                + self.group_depth - len(self.group[group_name])
                                + self.group_depth - len(self.group[amphipod])
                            )
                            self.group[group_name] = self.group[group_name][:-1]
                            self.group[amphipod] += amphipod
                            energy_spent += (
                                self.energy_per_step[amphipod] * steps
                            )
        return energy_spent

    def next_move(self) -> int:
        """Perform next move from diagram."""
        hall_candidates = [0, 1, 3, 5, 7, 9, 10]

        # If position is already in cache, return cache
        diagram_hash = hash(self)
        if diagram_hash in self.cache:
            return self.cache[diagram_hash]
        elif self.is_final():
            self.cache[diagram_hash] = 0
            return 0

        # Candidates can only be moves from group to hall.
        least_energy_spent = VERY_EXPENSIVE
        for name in ['A', 'B', 'C', 'D']:
            # Only consider moving from group if there are elements that do
            # not belong.
            if self.group[name] != name * len(self.group[name]):
                for candidate in hall_candidates:
                    # Segment between intersection and final hall location
                    # must be empty
                    inter = self.hall_intersection[name]
                    if candidate < inter:
                        hall_segment = self.hall[candidate:inter + 1]
                    else:
                        hall_segment = self.hall[inter:candidate + 1]
                    if hall_segment == '.' * len(hall_segment):
                        steps = (
                            len(hall_segment)
                            + self.group_depth - len(self.group[name])
                        )
                        new_diagram = copy.deepcopy(self)
                        amphipod = new_diagram.group[name][-1]
                        new_diagram.hall = (
                            self.hall[0:candidate] + amphipod
                            + self.hall[candidate+1:]
                        )
                        new_diagram.group[name] = new_diagram.group[name][:-1]
                        energy_spent = (
                            self.energy_per_step[amphipod] * steps
                            + new_diagram.perform_forced_moves()
                            + new_diagram.next_move()
                        )
                        if energy_spent < least_energy_spent:
                            least_energy_spent = energy_spent
                       
        self.cache[hash(self)] = least_energy_spent
        return least_energy_spent

                    
    def __hash__(self) -> int:
        """Hash of a diagram object."""
        string = (
            f"{self.group['A']:4}"
            f"{self.group['B']:4}"
            f"{self.group['C']:4}"
            f"{self.group['D']:4}"
            f"{self.hall}"
        )
        return hash(string)
        
    def __str__(self) -> str:
        """Return the string representation of the diagram."""
        group_section = ''
        is_first = True
        group_A = f"{self.group['A']:4}"
        group_B = f"{self.group['B']:4}"
        group_C = f"{self.group['C']:4}"
        group_D = f"{self.group['D']:4}"
        for group_element in range(self.group_depth - 1, -1, -1):
            if is_first:
                pad = '##'
                is_first = False
            else:
                pad = '  '
            group_section += (
                f"{pad}#{group_A[group_element]}"
                f"#{group_B[group_element]}"
                f"#{group_C[group_element]}"
                f"#{group_D[group_element]}#{pad}\n"
            )

        diagram = (
            f'#############\n'
            f'#{self.hall}#\n'
            f'{group_section}'
            f'  #########'
        ).strip()
        return diagram
            

diagram = AmphipodDiagram(groups={'A': 'BC', 'B': 'CB', 'C': 'AD', 'D': 'AD'})
print(f'Part One: Least energy for diagram: {diagram.next_move()}')
diagram = AmphipodDiagram(groups={'A': 'BDDC', 'B': 'CBCB',
                                  'C': 'AABD', 'D': 'ACAD'})
print(f'Part Two: Least energy for diagram: {diagram.next_move()}')

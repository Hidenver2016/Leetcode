# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 00:24:06 2020

@author: hjiang

https://www.interviewcake.com/question/python3/find-duplicate-optimize-for-space?course=fc1&section=sorting-searching-logarithms
二分法： 找出两次出现的数字，就是287题
O(nlgn) time and O(1)O(1) space.
"""


def find_repeat(numbers):
    floor = 1
    ceiling = len(numbers) - 1

    while floor < ceiling:
        # Divide our range 1..n into an upper range and lower range
        # (such that they don't overlap)
        # Lower range is floor..midpoint
        # Upper range is midpoint+1..ceiling
        midpoint = floor + ((ceiling - floor) // 2)
        lower_range_floor, lower_range_ceiling = floor, midpoint
        upper_range_floor, upper_range_ceiling = midpoint+1, ceiling

        # Count number of items in lower range
        items_in_lower_range = 0
        for item in numbers:
            # Is it in the lower range?
            if item >= lower_range_floor and item <= lower_range_ceiling:
                items_in_lower_range += 1

        distinct_possible_integers_in_lower_range = (
            lower_range_ceiling
            - lower_range_floor
            + 1
        )
        if items_in_lower_range > distinct_possible_integers_in_lower_range:
            # There must be a duplicate in the lower range
            # so use the same approach iteratively on that range
            floor, ceiling = lower_range_floor, lower_range_ceiling
        else:
            # There must be a duplicate in the upper range
            # so use the same approach iteratively on that range
            floor, ceiling = upper_range_floor, upper_range_ceiling

    # Floor and ceiling have converged
    # We found a number that repeats!
    return floor

#O(n) time and O(1)O(1) space.
#https://www.interviewcake.com/question/python3/find-duplicate-optimize-for-space-beast-mode

def find_duplicate(int_list):
    n = len(int_list) - 1

    # STEP 1: GET INSIDE A CYCLE
    # Start at position n+1 and walk n steps to
    # find a position guaranteed to be in a cycle
    position_in_cycle = n + 1
    for _ in range(n):
        position_in_cycle = int_list[position_in_cycle - 1]
        # we subtract 1 from the current position to step ahead:
        # the 2nd *position* in a list is *index* 1

    # STEP 2: FIND THE LENGTH OF THE CYCLE
    # Find the length of the cycle by remembering a position in the cycle
    # and counting the steps it takes to get back to that position
    remembered_position_in_cycle = position_in_cycle
    current_position_in_cycle = int_list[position_in_cycle - 1]  # 1 step ahead
    cycle_step_count = 1

    while current_position_in_cycle != remembered_position_in_cycle:
        current_position_in_cycle = int_list[current_position_in_cycle - 1]
        cycle_step_count += 1

    # STEP 3: FIND THE FIRST NODE OF THE CYCLE
    # Start two pointers
    #   (1) at position n+1
    #   (2) ahead of position n+1 as many steps as the cycle's length
    pointer_start = n + 1
    pointer_ahead = n + 1
    for _ in range(cycle_step_count):
        pointer_ahead = int_list[pointer_ahead - 1]

    # Advance until the pointers are in the same position
    # which is the first node in the cycle
    while pointer_start != pointer_ahead:
        pointer_start = int_list[pointer_start - 1]
        pointer_ahead = int_list[pointer_ahead - 1]

    # Since there are multiple values pointing to the first node
    # in the cycle, its position is a duplicate in our list
    return pointer_start

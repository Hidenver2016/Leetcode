# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 17:06:57 2018

@author: hjiang
"""

#Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
#
#Find all the elements of [1, n] inclusive that do not appear in this array.
#
#Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
#
#Example:
#
#Input:
#[4,3,2,7,8,2,3,1]
#
#Output:
#[5,6]

import numpy as np
def find_number(list1):
    max_number = max(list1)
    temp_list = list(np.arange(1,max_number+1))
    set_temp_list = set(temp_list)
    set_list = set(list1)
    missing_number  = set_temp_list -  set_list
    return list(missing_number)

def find_number1(nums):
    return list(set(range(1, len(nums) + 1)) - set(nums))

if __name__ == "__main__":
    print (find_number1([4,3,2,7,8,2,3,1]))
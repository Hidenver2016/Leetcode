# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 11:14:03 2019

@author: hjiang
"""

"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

这个更好
"""
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        num_sum = sum(nums)
        return n * (n + 1) / 2 - num_sum
    
    def missingNumber1(self, nums):#因为本身就少一个
        res = len(nums)#注意因为是要全部相加，所以最后这个值必须先放进去，要不是少一个missing data
#        res = 0
        for i in range(res):
            res ^= i
            res ^= nums[i]
            
        return res

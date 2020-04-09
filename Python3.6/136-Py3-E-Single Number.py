# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 12:11:48 2019

@author: hjiang
"""

"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""
import collections
class Solution:
    def singleNumber(self, nums):# 这个很经典，记住，非常快
        code = 0
        for ch in nums:
            code ^= ch
        return code
    
    def singleNumber1(self, nums):
        count = collections.Counter(nums)
        return count.most_common()[-1][0]
    
if __name__ == "__main__":
    test1 = [2,2,1]
    print(Solution().singleNumber(test1))
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 17:19:28 2018

@author: hjiang
"""
"""

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
# Time (n^2) Space (1)
class Solution(object):
    def twoSum(self, s, t):
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if s[i] + s[j] == t:
                    return [i, j]
                
# Time (n) Space(n)                
class Solution1:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashMap=dict()
        for i, x in enumerate(nums):
            if target-x in hashMap:
                return [i, hashMap[target-x]] #亮点
            hashMap[x] = i #亮点
                
if __name__ == "__main__":
    print(Solution().twoSum([2, 7, 11, 15],9))
    
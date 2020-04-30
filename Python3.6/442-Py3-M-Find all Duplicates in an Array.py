# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 00:18:56 2020

@author: hjiang
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""

class Solution(object):
    def findDuplicates(self, nums):
        """ #强行构造hash，因为全是正数，就把遇到过的数字当成序号，把序号位置上的数字搞成负数，因为所有数字都是小于长度的
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for x in nums:
            if nums[abs(x)-1] < 0:
                res.append(abs(x))
            else:
                nums[abs(x)-1] *= -1
        return res
    
nums = [4,3,2,7,8,2,3,1]
print(Solution().findDuplicates(nums))
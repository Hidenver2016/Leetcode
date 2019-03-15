# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 22:12:24 2019

@author: hjiang
"""

"""
Given an array nums of n integers and an integer target, 
find three integers in nums such that the sum is closest to target. 
Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
https://leetcode.com/problems/3sum-closest/discuss/7871/Python-O(N2)-solution
# Time:  O(n^2)
# Space: O(1)
"""
class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        num.sort()
        result = num[0] + num[1] + num[2] #排序之后肯定是最小值
        for i in range(len(num) - 2):
            j, k = i+1, len(num) - 1
            while j < k:
                sum = num[i] + num[j] + num[k]
                if sum == target:
                    return sum
                
                if abs(sum - target) < abs(result - target):#如果小于就更新，那么最后肯定是最小的是result
                    result = sum
                
                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1
            
        return result
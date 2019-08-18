# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 14:35:23 2019

@author: hjiang
"""

"""
Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Example 1:

Input: nums = [1, 5, 1, 1, 6, 4]
Output: One possible answer is [1, 4, 1, 5, 1, 6].
Example 2:

Input: nums = [1, 3, 2, 2, 3, 1]
Output: One possible answer is [2, 3, 1, 3, 1, 2]. 
Note:
You may assume all input has valid answer.

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?

这个题和280相比主要是有了重复数字，跟进的问题比较难，暂时先不关注
"""
# Time:  O(nlogn)
# Space: O(n)
#https://leetcode.com/problems/wiggle-sort-ii/discuss/77678/3-lines-Python-with-Explanation-Proof
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        med = (len(nums) - 1) // 2# 这个套路要记牢
        nums[::2], nums[1::2] = nums[med::-1], nums[:med:-1]
        
"""
nums = [1,2,3,4,5,6,7,8,9,10]
med = 4
nums[::2] = [1,3,5,7,9]
nums[1::2] = [2,4,6,8,10]
nums[med::-1] = [5,4,3,2,1]
nums[:med:-1] = [10,9,8,7,6]

nums = [5, 10, 4, 9, 3, 8, 2, 7, 1, 6]

因为后一半 nums[:med:-1]明显比前一半 nums[med::-1]要大， 那么这样（而且还是反向，就更加避免了后一半的最小值比前一半的最大值大的问题）
交错放置，即是符合要求的nums[0] < nums[1] （暗示了nums[::2]要小一些，所以是nums[med::-1]） > nums[2] < nums[3]....

"""
#http://www.cnblogs.com/grandyang/p/5139057.html        
#https://leetcode.com/problems/wiggle-sort-ii/discuss/77677/O(n)%2BO(1)-after-median-Virtual-Indexing
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 15:18:09 2019

@author: hjiang
"""

"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:

Input: [1,3,5]
Output: 1
Example 2:

Input: [2,2,2,0,1]
Output: 0
Note:

This is a follow up problem to Find Minimum in Rotated Sorted Array.
Would allow duplicates affect the run-time complexity? How and why?
https://blog.csdn.net/fuxuemingzhu/article/details/79536203
思想就是如果出现了重复数字，那么二分查找就没有作用了，必须使用顺序查找了。

这个题目意义不大，考得也很少
"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p1, p2 = 0, len(nums) - 1
        mid = p1
        while nums[p1] >= nums[p2]:
            if p2 - p1 == 1:
                mid = p2
                break
            mid = (p1 + p2) / 2
            if nums[mid] == nums[p1] and nums[mid] == nums[p2]:
                return self.minInOrder(nums, p1, p2)
            if nums[mid] >= nums[p1]:
                p1 = mid
            elif nums[mid] <= nums[p2]:
                p2 = mid
        return nums[mid]

    def minInOrder(self, nums, index1, index2):
        n1 = nums[index1]
        for i in range(index1 + 1, index2):
            if n1 > nums[i]:
                return nums[i]
        return n1

# -*- coding: utf-8 -*-
"""
Created on Wed May 22 15:18:09 2019

@author: hjiang
"""

"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2])

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
https://blog.csdn.net/fuxuemingzhu/article/details/79533470
看图描述
"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return nums[0]
        left, right = 0, len(nums) - 1
        mid = left
        while nums[left] >= nums[right]:#满足这个条件必然是已经转动过的数列了
            if left + 1 == right:#最小值必然在最大值之后一位
                mid = right
                break
            mid = (left + right) // 2
            if nums[mid] >= nums[left]:#如果左边是有顺序的
                left = mid#最小的数在右边
            elif nums[mid] <= nums[right]:#如果右边是有顺序的
                right = mid
        return nums[mid]


# -*- coding: utf-8 -*-
"""
Created on Wed May 22 15:17:36 2019

@author: hjiang
"""

"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?

33, 81一起做

此题是有重复数字的33题

这样的话，如果直接进行左右指针的比较就不知道向哪个方向搜索了，所以，需要在正式比较之前，
先移动左指针，是他指向一个和右指针不同的数字上。然后再做33题的查找

https://blog.csdn.net/fuxuemingzhu/article/details/83214278
"""
class Solution(object):
    def search(self, nums, target):#就这么写好了，验证了也是对的
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        N = len(nums)
        l, r = 0, N - 1
        while l <= r:
            while l < r and nums[l] == nums[r]:
                l += 1
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return True
            if nums[mid] <= nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return False
#            if nums[mid] >= nums[l]:
#                if nums[l] <= target < nums[mid]:
#                    r = mid - 1
#                else:
#                    l = mid + 1
#            elif nums[mid] <= nums[r]:
#                if nums[mid] < target <= nums[r]:
#                    l = mid + 1
#                else:
#                    r = mid - 1
#        return False
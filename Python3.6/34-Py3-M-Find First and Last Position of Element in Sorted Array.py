# -*- coding: utf-8 -*-
"""
Created on Thu May 23 15:54:39 2019

@author: hjiang
"""

"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
https://blog.csdn.net/fuxuemingzhu/article/details/83273084

https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/discuss/14707/9-11-lines-O(log-n)

Here, my helper function is a simple binary search, 
telling me the first index where I could insert a number n into nums to keep it sorted. 
Thus, if nums contains target, I can find the first occurrence with search(target). 
I do that, and if target isn't actually there, then I return [-1, -1]. 
Otherwise, I ask search(target+1), which tells me the first index where I could insert target+1, 
which of course is one index behind the last index containing target, so all I have left to do is subtract 1.
"""


class Solution:
    def searchRange(self, nums, target):
        def search(n):# 记住，这个找到左边第一个
            l, r = 0, len(nums)
            while l < r:
                mid = (l + r) // 2
                if nums[mid] >= n:
                    r = mid
                else:
                    l = mid + 1
            return l
        l = search(target)
        print(l)
        return [l, search(target+1)-1] if target in nums[l:] else [-1, -1]
        

import bisect
class Solution1(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target)
        if left == right:
            return [-1, -1]
        return [left, right - 1]

if __name__ == "__main__":
    print(Solution().searchRange([5,7,7,8,8,8,8,10], 8))

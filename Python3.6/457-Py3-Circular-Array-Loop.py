# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 17:30:45 2018

@author: hjiang
"""

"""
You are given an array of positive and negative integers. 
If a number n at an index is positive, then move forward n steps. 
Conversely, if it's negative (-n), move backward n steps. 
Assume the first element of the array is forward next to the last element, 
and the last element is backward next to the first element. 
Determine if there is a loop in this array. 
A loop starts and ends at a particular index with more than 1 element along the loop. 
The loop must be "forward" or "backward'.

Example 1: Given the array [2, -1, 1, 2, 2], there is a loop, from index 0 -> 2 -> 3 -> 0.

Example 2: Given the array [-1, 2], there is no loop.

Note: The given array is guaranteed to contain no element "0".

Can you do it in O(n) time complexity and O(1) space complexity?
"""
# Time:  O(n)
# Space: O(1)
import copy

class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or len(nums) < 2:#边界条件
            return False
        nums1 = copy.copy(nums)
        n = len(nums)
        for i in range(n):           
#            if type(nums[i]) != int: # visited element
#                continue
#            if nums[i] % n == 0: # self-loop 一定要找多于一步的
#                continue
            
            direction = (nums1[i] > 0) # loop direction, cannot be changed midway
            
            mark = str(i)
            while (type(nums[i]) == int) and (direction ^ (nums1[i] < 0)) and (nums[i] % n != 0):
                jump = nums[i]
                nums[i] = mark
                i = (i + jump) % n
                
            if nums[i] == mark: #跳到任何一个标记上了的都可以
                return True
            
        return False

if __name__ == "__main__":
    print(Solution().circularArrayLoop([2, -1, 1, 2, 2,-1,-1,-1]))     

    
class Solution0(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def next_index(nums, i):
            return (i + nums[i]) % len(nums)

        for i in range(len(nums)):
            if nums[i] == 0:
                continue

            slow, fast = i, i
            while nums[next_index(nums, slow)] * nums[i] > 0 and \
                  nums[next_index(nums, fast)] * nums[i] > 0 and \
                  nums[next_index(nums, next_index(nums, fast))] * nums[i] > 0:
                slow = next_index(nums, slow)
                fast = next_index(nums, next_index(nums, fast))
                if slow == fast:
                    if slow == next_index(nums, slow):
                        break
                    return True

            slow, val = i, nums[i]
            while nums[slow] * val > 0:
                tmp = next_index(nums, slow)
                nums[slow] = 0
                slow = tmp

        return False

  
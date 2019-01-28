# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 22:13:16 2019

@author: hjiang
"""

"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Note:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""
# Time:  O(n)
# Space: O(1)
class Solution(object):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """

    def rotate(self, nums, k):
        k %= len(nums)
        self.reverse(nums, 0, len(nums)) #[7,6,5,4,3,2,1]
        self.reverse(nums, 0, k)# [5,6,7,4,3,2,1]
        self.reverse(nums, k, len(nums))# [5,6,7,1,2,3,4]

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end - 1] = nums[end - 1], nums[start]
            start += 1
            end -= 1

# Time:  O(n)
# Space: O(n)
class Solution4(object):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]
        
if __name__ == "__main__":
    print(Solution().rotate([1,2,3,4,5,6,7], 3))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
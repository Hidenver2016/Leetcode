# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 14:29:35 2019

@author: hjiang
"""

"""
Given an array nums, write a function to move all 0's to the end of it while 
maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

class Solution:#自己写的ａｃ不了
    def moveZeroes(self, nums):
        for i in range(len(nums)):
            if nums[i] == 0:
                j = i + 1
                while nums[j] == 0: 
                    if j == len(nums) -1 : return nums
                    j += 1
                nums[i], nums[j] = nums[j], nums[i]
        return nums
#https://blog.csdn.net/fuxuemingzhu/article/details/51284981    
class Solution1(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        i = 0#表示第一个0的位置
        for j in range(N):
            if nums[j] != 0: #[1,3,12,0,0]
#            if nums[j] == 0: #[0,0,1,3,12]
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return nums
    
if __name__ == "__main__":
    print(Solution1().moveZeroes([0,1,0,3,12]))
            
            
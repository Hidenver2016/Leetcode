# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 14:33:48 2019

@author: hjiang
"""

"""
Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

Example:

Input: nums = [3,5,2,1,6,4]
Output: One possible answer is [3,5,1,6,2,4]
"""
# Time:  O(n)
# Space: O(1) 
"""


只需要swap需要更改的地方，根据条件nums[0] <= nums[1] >= nums[2] <= nums[3]....
i为奇数时，如果nums[i - 1] > nums[i]: 交换
i为偶数时，如果nums[i - 1] < nums[i]: 交换
"""

class Solution(object):#只操作需要换的部分
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(1, len(nums)):
            if ((i % 2 == 1) and nums[i - 1] > nums[i]) or ((i % 2 == 0) and nums[i - 1] < nums[i]):
#            if ((i % 2) and nums[i - 1] > nums[i]) or (not (i % 2) and nums[i - 1] < nums[i]): 一样的
                # Swap unordered elements.
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
        return nums
                
                
#http://www.cnblogs.com/grandyang/p/5177285.html
class Solution1:
    def wiggleSort(self, nums):
        if len(nums) <= 2: return
        nums.sort()
        for i in range(2, len(nums), 2):
            nums[i], nums[i-1] = nums[i-1], nums[i]
            
if __name__ == "__main__":
    print(Solution().wiggleSort([3,5,2,1,6,4]))
                    
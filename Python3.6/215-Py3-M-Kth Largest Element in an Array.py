# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 16:10:20 2019

@author: hjiang
"""

"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, 
not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.

原文：https://blog.csdn.net/fuxuemingzhu/article/details/79264797 
"""
class Solution(object):#每一次都移出最大值
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        for i in range(k - 1):#实际上是排序之后倒数第k个，那么可以理解成移出后面k-1个即可
            nums.remove(max(nums))
        return max(nums)
    
  
    def findKthLargest1(self, nums, k):#排序
        nums.sort()
        return nums[len(nums) - k]
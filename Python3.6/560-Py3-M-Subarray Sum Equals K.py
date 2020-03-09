# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 22:16:33 2020

@author: hjiang
"""

"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
https://leetcode.com/problems/subarray-sum-equals-k/discuss/341399/Python-clear-explanation-with-code-and-example

[1,2,1,3] k=3

0->3
1->4
4->7
Hence, 3 sub arrays of sums=k
"""
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        sums = 0
        d = dict()
        d[0] = 1#初始化为0， 要不是第一个不会被计算在内
        
        for i in range(len(nums)):
            sums += nums[i]
            count += d.get(sums-k,0)
            d[sums] = d.get(sums,0) + 1# 对于之前的累加计数，在后面是用来算sums-k的，看有多少个
        
        return(count)
    
print(Solution().subarraySum([1,2,1,3], 3))
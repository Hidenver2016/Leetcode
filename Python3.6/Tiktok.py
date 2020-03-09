# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 14:45:10 2020

@author: hjiang

划分一个list, 让两部分的方差和最小
"""

class Solution:
    """
    @param nums: 数组
    @return: 最小方差划分的数组索引和最小方差
    """
    def minVariancePartition(self, nums):
        left = self.subVariance(nums[:])
        right = self.subVariance(nums[::-1])[::-1]
        minVariance, index = float("inf"), 0
        for i in range(1, len(right)):
            if left[i-1] + right[i] < minVariance:
                minVariance = left[i-1] + right[i]
                index = i - 1  # 更新划分的索引
        return index, minVariance

    def subVariance(self, nums):
        subVar = []
        subSum = subSquare = 0
        for i in range(len(nums)):
            subSum += nums[i]
            subSquare += nums[i] * nums[i]
            subVar.append(subSquare/(i+1) - (subSum/(i+1))**2) # 子数组方差
        return subVar
    
a = Solution()
b = [4,3,1,2]
print(a.minVariancePartition(b))

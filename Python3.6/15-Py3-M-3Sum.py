# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 15:35:44 2019

@author: hjiang
"""

"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]


这个方法就是上面说的对原数组排序的做法，这个做法思路比较简单，对于排序后的数组遍历，
对每个位置都从它的后一个元素和末尾一个元素向中间集中，如果和为0就添加到结果数组中。
这里需要注意的地方是需要跳过相同的数字，因为同样的数字组合只能出现一次嘛。
也就是两个while，注意判断相等的条件：i是向前面判断，j是向后面判断。

这个方法不用使用set来保存已经遍历过的数字组合，因为对于原数组来说每次向后遍历的过程中，
同样的组合只能出现一次。

时间复杂度是O(N^2)，空间复杂度是O(1)。
--------------------- 

原文：https://blog.csdn.net/fuxuemingzhu/article/details/83115850 

"""
#import numpy as np
import random
class Solution(object):
    def threeSum(self, nums):# Quora的题，不同位置的数字看成不一样的数
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        N = len(nums)
        nums.sort()
        res = []
        for t in range(N - 2):
#            if t > 0 and nums[t] == nums[t - 1]:#从小的数开始，如果是一样的直接过
#                    continue
            i, j = t + 1, N - 1
            while i < j:
                _sum = nums[t] + nums[i] + nums[j]
                if _sum == 0:
                    res.append([nums[t], nums[i], nums[j]])
                    i += 1
                    j -= 1
#                    while i < j and nums[i] == nums[i - 1]:#i 不能和前面的（i-1）一样
#                        i += 1
#                    while i < j and nums[j] == nums[j + 1]:#j 不能和后面的（j+1）一样
#                        j -= 1
                elif _sum < 0:#这里还调整了前进方向，程序会更加高效
                    i += 1
                else:
                    j -= 1
        return res
    
    def threeSum1(self, nums):#这个是对的，看这个很简单
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        N = len(nums)
        nums.sort()
        res = []
        for t in range(N - 2):
            if t > 0 and nums[t] == nums[t - 1]:#从小的数开始，如果是一样的直接过,而且如果t>0，那么就没必要算了，因为后面都是正数，必然挂
                    continue
            i, j = t + 1, N - 1
            while i < j:
                _sum = nums[t] + nums[i] + nums[j]
                if _sum == 0:
                    res.append([nums[t], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]:#i 不能和前面的（i-1）一样
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:#j 不能和后面的（j+1）一样
                        j -= 1
                elif _sum < 0:#这里还调整了前进方向，程序会更加高效
                    i += 1
                else:
                    j -= 1
        return res
    
if __name__ == "__main__":
#    nums = 100000
#    A = [int(nums*random.uniform(-1, 1)) for i in range(nums)]
#    res = Solution().threeSum(A)
    print(Solution().threeSum1([-1, 0, 1, 2, -1, -4, -1, -1]))

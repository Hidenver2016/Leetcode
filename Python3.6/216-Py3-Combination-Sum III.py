# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 15:57:02 2019

@author: hjiang
"""

"""
Find all possible combinations of k numbers that add up to a number n, 
given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
"""


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(range(1, 10), k, n, 0, res, [])
        return res
        
    def dfs(self, nums, k, n, index, res, path):
        if k < 0 or n < 0:
            return 
        elif k == 0 and n == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            self.dfs(nums, k - 1, n - nums[i], i + 1, res, path + [nums[i]])


# Time:  O(k * C(n, k))
# Space: O(k)

class Solution1(object):
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        res = []
        self.helper(res, [], 1, k, n)
        return res

    def helper(self, res, path, start, k, target):
        if k == 0 and target == 0:#同时满足结果target和数量k
            res.append(list(path))
        elif k < 0:
            return
#        while start < 10 and start * k + k * (k - 1) / 2 <= target:#因为是1到9，此处用等差数列求和粗略估计一下，看看行不行
        while start <10:#其实不用那么高级的方法也可以，底下的start+=就保证了不会取同一个数
            path.append(start)
            self.helper(res, path, start + 1, k - 1, target - start)
            path.pop()
            start += 1
            
            
            
            
            
            
            
            
            
            
            
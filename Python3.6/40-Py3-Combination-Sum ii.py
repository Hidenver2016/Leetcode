# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 15:03:11 2019

@author: hjiang
"""

"""
Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""

#dfs
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        print(candidates)
        res = []
        self.dfs(candidates, target, 0, res, [])
        return res

    def dfs(self, nums, target, index, res, path):
        if target < 0:
            return
        elif target == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            self.dfs(nums, target - nums[i], i + 1, res, path + [nums[i]])


#backtracking
# Time:  O(k * C(n, k))
# Space: O(k)

class Solution1(object):
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        res = []
        self.helper(sorted(candidates), res, 0, [], target)
        return res

    def helper(self, candidates, res, start, path, target):
        if target == 0:
            res.append(list(path))
        prev = 0 # 初始化，因为所有candiates都是正数
        while start < len(candidates) and candidates[start] <= target:
# 本题的目的是不能重复取一个位置上的数，不同的位置上的相同数可以取。之后有一个start+=1,意思是 candidates[i] ！= candidates[i - 1],不能取一样位置的数
            if prev != candidates[start]: 
                path.append(candidates[start])
                self.helper(candidates, res, start + 1, path, target - candidates[start])
                path.pop()
                prev = candidates[start]
            start += 1
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 15:38:40 2019

@author: hjiang
"""

"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""

# Time:  O(n * 2^n) ~ O((n * 2^n)^2)
# Space: O(1)
class Solution3(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.subsetsWithDupRecu(result, [], sorted(nums))
        return result

    def subsetsWithDupRecu(self, result, cur, nums):
        if not nums:
            if cur not in result:
                result.append(cur)
        else:
            self.subsetsWithDupRecu(result, cur, nums[1:])
            self.subsetsWithDupRecu(result, cur + [nums[0]], nums[1:])
#https://blog.csdn.net/fuxuemingzhu/article/details/79785548

#这道题和78subsets 非常像，加了约束而已
#我们在进行循环的时候加入一个判断，即新加入的元素是否和刚刚加入的元素相同，如果相同就不加入了。
#这样就可以屏蔽掉了重复元素的问题。            
class Solution1(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        self.dfs(nums, 0, res, [])
        return res
        
    def dfs(self, nums, index, res, path):
        if path not in res:#注意not in 这个操作
            res.append(path)
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            self.dfs(nums, i + 1, res, path + [nums[i]])
            
            
            
            
            
            
            
            
            
            

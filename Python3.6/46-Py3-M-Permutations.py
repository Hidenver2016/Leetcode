# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 16:44:29 2019

@author: hjiang
"""

"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

https://blog.csdn.net/fuxuemingzhu/article/details/79363903
"""
# Time: O(n!)
# Space: O(n)
#dfs
#类似于subsets。这个题的递归没有使用index作为变量，因为要求的是全排列，而不是某种组合。
class Solution(object):#重点掌握这个！！！
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums, res, [])
        return res
        
    def dfs(self, nums, res, path):
        if not nums:#这一行是 nums没了之后再加上结果path
            res.append(path)
        else:
            for i in range(len(nums)):#因为这个把所有数都遍历了一遍，所以出现的是全排列
                self.dfs(nums[:i] + nums[i + 1:], res, path + [nums[i]])

#仍使用回溯法，不过不像上面那样使用切片，而是使用了visited数组来保存是否经历过这个位置。应该是更常用的一个方法，速度也能明显加快。
    
# Time:  O(n * n!)
# Space: O(n)

class Solution2(object):
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        res = []
        visited = [0] * len(num)
        self.helper(res, visited, [], num)
        return res

    def helper(self, res, visited, path, num):
        if len(path) == len(num):
            res.append(list(path))
#            return
        for i in range(len(num)):
            if not visited[i]:
                visited[i] = 1
                path.append(num[i])
                self.helper(res, visited, path, num)
                path.pop()
                visited[i] = 0
                
if __name__ == "__main__":
    print(Solution2().permute([1,2,3]))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
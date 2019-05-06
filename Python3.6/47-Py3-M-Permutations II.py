# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 16:55:55 2019

@author: hjiang
"""

"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""
#https://blog.csdn.net/fuxuemingzhu/article/details/79513261
#是没有重复数字的，这个题有重复数字。我的做法很简单，就是在以前的基础上加了一个判断条件：path not in res。
#这样的做法是在每个path生成之后才去做的判断，因此效率一点都不高。最后竟然也能通过了。
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.helper(nums, res, [])
        return res
    
    def helper(self, nums, res, path):
        if not nums and path not in res:
            res.append(path)
        else:
            for i in range(len(nums)):
                self.helper(nums[:i] + nums[i+1:], res, path + [nums[i]])


# Time:  O(n * n!)
# Space: O(n)

"""
这种写法是backtracking,遇到这种unique的，最好先排个序
"""
class Solution1(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()# 
        res = []
        visited = [0] * len(nums)
        self.helper(res, visited, [], nums)
        return res

    def helper(self, res, visited, path, nums):
        if len(path) == len(nums):
            res.append(list(path))
            return
        for i in range(len(nums)):#这个是取排列数，如果是组合数，需要for i in range(index, len(nums))见40题
            if visited[i] or (i > 0 and nums[i-1] == nums[i] and not visited[i-1]):#因为在完成一个dfs之后visited[i-1]=0，
                continue#                                                           这里如果读到visited[i-1]=0，意味着访问过，就不必再次访问了
            visited[i] = 1
            path.append(nums[i])
            self.helper(res, visited, path, nums)
            path.pop()
            visited[i] = 0

if __name__ == "__main__":
    print(Solution1().permuteUnique([1,1,2]))












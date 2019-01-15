# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 11:26:34 2019

@author: hjiang
"""

"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

# Time:  O(n * 2^n)
# Space: O(1), 应该是

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = [[]]
        for i in range(len(nums)):# O(n)
            size = len(result)
            for j in range(size):# O(2^n)?
                result.append(list(result[j]))# 这个地方两行是亮点，这一行表示加上之前的结果
                result[-1].append(nums[i])#这一行表示加上新的元素，组成新的subset
        return result


class Solution1:#dfs比较难想,这个实际上是backtracking
    def subsets(self,nums):
        self.res = []
        def dfs(nums, i, tmp):
            self.res.append(tmp[:])#此行是将累计的tmp 加到一起
            for i in range(i,len(nums)):
                tmp.append(nums[i])#此行是加新的元素
                dfs(nums,i+1,tmp)#向前dfs，注意此处是i+1,但是真正的for循环还是要对应到外面的i才可以
                tmp.pop()
        dfs(nums,0,[])
        return self.res
#backtracking
#https://blog.csdn.net/fuxuemingzhu/article/details/79359540
# 无限制条件，直接就是dfs        
class Solution2(object):# 这个是最好的方法
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums, 0, res, [])
        return res
    
    def dfs(self, nums, index, res, path):
        res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i + 1, res, path + [nums[i]])

    
if __name__ == "__main__":
    print(Solution2().subsets([1,2,3]))    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
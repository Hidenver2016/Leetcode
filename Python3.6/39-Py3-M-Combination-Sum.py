# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 15:01:12 2019

@author: hjiang
"""

"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""
"""
https://blog.csdn.net/fuxuemingzhu/article/details/79322462
方法一：DFS
dfs搜索，先对所有的值进行排序，然后对每个元素进行dfs搜索，判断能否得到target。用了几个条件判断进行提前终止，这样能加速。
"""

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, res, [])
        return res
    
    
    def dfs(self, nums, target, index, res, path):
        if target < 0: return
        elif target == 0:
            res.append(path)#这个append才是append子集
            return
        for i in range(index, len(nums)):#这样找才有效，不要重复往前找，浪费资源
            if nums[index] > target: return
#注意，这里的path + [nums[i]] 也不能写到外面来，这样子会先加上已经有的值
            self.dfs(nums, target - nums[i], i, res, path + [nums[i]])#这个加号是加一个个的元素,因为[]+3 或者[]+[3]都是[]空集



"""
方法二：回溯法
上面的DFS虽说也是递归，但是和回溯还是有区别的。因为回溯的含义，此路不通就倒着走回去，
而上面的DFS是进行了全集的搜索。

这个回溯还是很好写的，需要一个新的函数，含义是从候选集的start位置开始向后寻找和为target的路径.
如果target等于0了就是我们终止的一个条件，即正好搜索到了一条合适的路径。

需要注意的是res要用引用传递，而path是使用的传值（复制）。这样子那个的每次路径才是不一样的。
另外就是题目允许每个数字使用多次，所以循环开始的地方是start，而往递归函数里面传递的也是start.
"""
# Time:  O(k * n^k)
# Space: O(k)
class Solution1:# 自己写的，优先看
    def combinationSum(self, candidates, target):
        res = []
        candidates.sort()
        self.helper(candidates, res, 0, [], target)
        return res
    
    def helper(self, nums, res, k, path, target):
        if target < 0: return
        if target == 0: 
            res.append(list(path))#这个地方要加list的关键在于后面有一个path.pop()，这种操作也会改变之前按的res,所以要加list隔开
        for i in range(k, len(nums)):
#            if nums[k] > target: return
#            path.append(nums[i])
#            path = path + [nums[i]] 与此句等效，也可以写成 path += [nums[i]]
            path += [nums[i]] #不能写到下面的函数里面，因为如果需要后面的pop弹出的话，会直接连函数里面的path+ [nums[i]]都不计算了，相当于path中一次弹出去两个值
            self.helper(nums, res, i, path, target - nums[i])#这里不能写path + [nums[i]], target -[nums[i]],因为是同时计算的，target 会保留上次计算的结果，这样会不对
            path.pop()
            
            
class Solution2(object):
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        res = []
        self.helper(sorted(candidates), res, 0, [], target)
        return res

    def helper(self, nums, res, start, path, target):
        if target == 0:
            res.append(list(path))
        while start < len(nums) and nums[start] <= target:#不能超过candidates的种类数
            path.append(nums[start])
            self.helper(nums, res, start, path, target - nums[start])
            path.pop()#这里可以理解成走不通了再回去，backtracking,其实和上面的dfs（solution, solution1） 差不多的
            start += 1            
            
if __name__ == "__main__":
    print(Solution().combinationSum([2,3,6,7],7))
    print(Solution1().combinationSum([2,3,5],8))              
            
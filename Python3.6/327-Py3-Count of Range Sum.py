# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 17:19:24 2019

@author: hjiang
"""

"""
Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i ≤ j), inclusive.

Note:
A naive algorithm of O(n2) is trivial. You MUST do better than that.

Example:

Input: nums = [-2,5,-1], lower = -2, upper = 2,
Output: 3 
Explanation: The three ranges are : [0,0], [2,2], [0,2] and their respective sums are: -2, -1, 2.
"""

#https://leetcode.com/problems/count-of-range-sum/discuss/77991/Short-and-simple-O(n-log-n)
#https://www.hrwhisper.me/leetcode-count-of-range-sum/
#Time: O(n log n)
"""
因为是要计算区间, 因此我们可以将其前n个元素求和放到一个数组中, 这样当我们我计算区间[i, j]的和时, 只要用sum[j+1] - sum[i]即可, 
这样就可以在O(1)的时间取得任意区间的和. 
"""


class FenwickTree(object):
    def __init__(self, n):
        self.sum_array = [0] * (n + 1)
        self.n = n
 
    def lowbit(self, x):
        return x & -x
 
    def add(self, x, val):
        while x <= self.n:
            self.sum_array[x] += val
            x += self.lowbit(x)
 
    def sum(self, x):
        res = 0
        while x > 0:
            res += self.sum_array[x]
            x -= self.lowbit(x)
        return res
  
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        if not nums: return 0
        sum_array = [upper, lower - 1]
        total = 0
        for num in nums:
            total += num
            sum_array += [total, total + lower - 1, total + upper]
 
        index = {}
        for i, x in enumerate(sorted(set(sum_array))):
            index[x] = i + 1
 
        tree = FenwickTree(len(index))
        ans = 0
        for i in range(len(nums) - 1, -1, -1):
            tree.add(index[total], 1)
            total -= nums[i]
            ans += tree.sum(index[upper + total]) - tree.sum(index[lower + total - 1])
        return ans
    
import bisect
class Solution1(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        prefix,thisSum,ans = [0],0,0
        for n in nums:
            thisSum += n
            ans += bisect.bisect_right(prefix, thisSum-lower) - bisect.bisect_left(prefix, thisSum-upper)
            bisect.insort(prefix, thisSum)
        return ans
    
if __name__ == "__main__":
    print(Solution().countRangeSum([-2,5,-1],-2,2))
    
    

    
    
    
    
    
    
    
    
    
    
    
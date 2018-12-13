# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 15:23:50 2018

@author: hjiang
"""

"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.

Example:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:

The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.

https://leetcode.com/problems/range-sum-query-mutable/discuss/75730/148ms-Python-solution-Binary-Indexed-Tree
http://www.cnblogs.com/grandyang/p/4985506.html
"""
#Time: O(logn)
# Space： O(2n)

class NumArray(object):
    def __init__(self, nums):
        self.n = len(nums)
        self.a, self.c = nums, [0] * (self.n + 1)
        for i in range(self.n):
            k = i + 1#此题中的求和是指到这个数，所以下面的index都有加一（+1）
            while k <= self.n:
                self.c[k] += nums[i]
                k += (k & -k)

    def update(self, i, val):
        diff, self.a[i] = val - self.a[i], val
        i += 1
        while i <= self.n:
            self.c[i] += diff
            i += (i & -i) #往前走，算到list[-1],因为只影响前面的点

    def sumRange(self, i, j):
        res, j = 0, j + 1
        while j:
            res += self.c[j]
            j -= (j & -j) # 往后走
        while i:
            res -= self.c[i]
            i -= (i & -i) #往后走，就是算到list的开始list[0]
        return res
    
class NumArray1(object):
    def __init__(self, nums):
        self.nums = nums

    def update(self, i, val):
        self.nums[i] = val

    def sumRange(self, i, j):
        res = sum(self.nums[i:j])
        return res
    

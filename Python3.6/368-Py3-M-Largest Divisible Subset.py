# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 21:26:02 2019

@author: hjiang
"""

"""
Given a set of distinct positive integers, find the largest subset such that 
every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)
Example 2:

Input: [1,2,4,8]
Output: [1,2,4,8]


https://blog.csdn.net/fuxuemingzhu/article/details/83027364
是否想起了Longest Increase Sequence？这两个题非常相似啊，所以做题一定要把融会贯通才行。

首先需要对题目给出的数组进行排序，这样的作用是我们从左到右遍历一次，每次只看后面的数字能不能被前面的整除就行。

问题分成了两个部分：

寻找最长的满足题目的数组
输出整个结果
使用一个一维DP，其含义是题目要求的数组，DP[i]的含义是，从0~i位置满足题目的最长数组。先用i遍历每个数字，
然后用j从后向前寻找能被nums[i]整除的数字，这样如果判断能整除的时候，再判断dp[i] < dp[j] + 1，
即对于以i索引结尾的最长的数组是否变长了。在变长的情况下，需要更新dp[i]，同时使用parent[i]更新i的前面能整除的数字。
另外还要统计对于整个数组最长的子数组长度。

知道了对于每个位置最长的子数组之后，我们也就知道了对于0~n区间内最长的满足题目条件的数组，最后需要再次遍历，
使用parent就能把正儿个数组统计输出出来。因为这个最大的索引mx_index是对n而言的，所以输出是逆序的。

时间复杂度是O(N^2)，空间复杂度是O(N).
--------------------- 

原文：https://blog.csdn.net/fuxuemingzhu/article/details/83027364 

"""
class Solution:
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums: return []
        N = len(nums)
        nums.sort()
        dp = [0] * N #LDS
        parent = [0] * N
        mx = 0
        mx_index = -1
        for i in range(N):
            for j in range(i - 1, -1 , -1):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    parent[i] = j
                    if dp[i] > mx:
                        mx = dp[i]
                        mx_index = i
        res = list()
        for k in range(mx + 1):
            res.append(nums[mx_index])
            mx_index = parent[mx_index]
        return res[::-1]



# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 14:44:12 2020

@author: hjiang
"""

"""
Given an array which consists of non-negative integers and an integer m, 
you can split the array into m non-empty continuous subarrays. 
Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
https://leetcode.com/problems/split-array-largest-sum/discuss/89846/Python-solution-with-detailed-explanation
"""

class Solution0(object):#暴力递归，考试能写出来这个就行了
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        return self.helper(nums, m)
    
    def helper(self, nums, m):
        if nums == []:
            return 0
        elif m == 1:
            return sum(nums)
        else:
            min_result = float('inf')
            for j in range(1,len(nums)+1):
                left, right = sum(nums[:j]), self.helper(nums[j:], m-1)
                min_result = min(min_result, max(left, right))
            return min_result
    
from collections import defaultdict    
class Solution1(object):#暴力递归加记忆
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        cache = defaultdict(dict)
        return self.helper(0, nums, m, cache)   
    
    
    def helper(self, i, nums, m, cache):
        if i == len(nums):
            return 0
        elif m == 1:
            return sum(nums[i:])
        else:
            if i in cache and m in cache[i]:#注意这里建立了一个双重dict, 第一个key是i, 里面第二个key是m
                return cache[i][m]
            cache[i][m] = float('inf')
            for j in range(1,len(nums)+1):
                left, right = sum(nums[i:i+j]), self.helper(i+j, nums, m-1, cache)
                cache[i][m] = min(cache[i][m], max(left, right))#注意这里建立了一个双重dict, 第一个key是i, 里面第二个key是m
                if left > right:
                    break
            return cache[i][m]
    
a = Solution1()
num = [7,2,5,10,8]
print(Solution1().splitArray(num, 2))
    
    
    
    
class Solution2(object):#这个最猛啊
    def is_valid(self, nums, m, mid):
        # assume mid is < max(nums)
        cuts, curr_sum  = 0, 0
        for x in nums:
            curr_sum += x
            if curr_sum > mid:
                cuts, curr_sum = cuts+1, x
        subs = cuts + 1
        return (subs <= m)
    
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        low, high, ans = max(nums), sum(nums), -1
        while low <= high:
            mid = (low+high)//2
            if self.is_valid(nums, m, mid): # can you make at-most m sub-arrays with maximum sum atmost mid 
                ans, high = mid, mid-1
            else:
                low = mid + 1
        return ans
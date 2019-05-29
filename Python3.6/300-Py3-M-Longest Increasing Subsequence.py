# -*- coding: utf-8 -*-
"""
Created on Thu May 23 16:06:56 2019

@author: hjiang
"""

"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?

https://blog.csdn.net/fuxuemingzhu/article/details/79820919
Time: O(n^2)
"""
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        dp = [0] * len(nums)
        dp[0] = 1
        for i in range(1, len(nums)):
            tmax = 1
            for j in range(0, i):
                if nums[i] > nums[j]:
                    tmax = max(tmax, dp[j] + 1)
            dp[i] = tmax
        return max(dp)


#https://leetcode.com/problems/longest-increasing-subsequence/discuss/74824/JavaPython-Binary-search-O(nlogn)-time-with-explanation
#https://blog.csdn.net/jiary5201314/article/details/51169602
class Solution1:
    def lengthOfLIS(self, nums):
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) // 2
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            size = max(i + 1, size)
        return size
    
import bisect    
class Solution2:
    def lengthOfLIS(self, nums):#这个是自己写的
        h = []
        for x in nums:
            j = bisect.bisect_left(h, x)
            if j < len(h): h[j] = x
            else: h.append(x)
        return len(h)
    
    def lengthOfLIS1(self, nums):#这个也是自己写的
        h = []
        def helper(h, x):
            l, r = 0, len(h)
            while l < r:
                mid = (l + r) // 2
                if h[mid] >= x:#是找最左
                    r = mid
                else:
                    l = mid + 1
            return l
        for x in nums:
            j = helper(h, x)
            if j < len(h): h[j] = x
            else: h.append(x)
        return len(h)
        
            
    
#if __name__ == "__main__":
#    Input = [10,9,2,5,3,7,101,18]
#    Input1 = [2,2]
#    print(Solution2().lengthOfLIS(Input1))
#def helper(h, x):
#    l, r = 0, len(h)
#    while l < r:
#        mid = (l + r) // 2
#        if h[mid] > x:#这里明显是找最右
#            r = mid
#        else:
#            l = mid + 1
#    return l
#h = [2, 2]
#x = 2
#print(helper(h, x))

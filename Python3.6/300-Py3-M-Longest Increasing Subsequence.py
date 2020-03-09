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
"""
此题体现了二分法的另一个用途，左侧插入法的用处
1. tail最终是个有序数列，记录了最长的递增序列到底是什么
2. tail的新数字从左边插入的好处就是，一旦有比较小的数字就会把右侧大的数字原味置代替，
除非有新的更大的数字进来，否则tail这个数组的大小是不会增加的(实际上是l,r之间的长度不会增加)
3. 每次二分法都是在寻找新数字从左侧插入（有重复数字，就从左边插入）tail的位置， 

"""
class Solution1:
    def lengthOfLIS(self, nums):#看这个
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            l, r = 0, size
            while l < r:#从左边插入的好处就是，一旦有比较小的数字就会把右侧大的数字原味置代替，除非有新的更大的数字进来，否则tail这个数组的大小是不会增加的
                m = (l + r) // 2
                if tails[m] >= x:
                    r = m
                else:
                    l = m + 1
            tails[l] = x #这个size实际上是tail的size,那么上面那个二分法实际上也是在找x在tails中的位置（有重复数字，就从左边插入）
            size = max(l + 1, size)
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
            if j < len(h): h[j] = x#这时候意味着当前数字不是最大的，小于之前的数，对于长度增加没有直接作用，可以先行替换，以便以后遇到合适的
            else: h.append(x)#当前就可以增加
        return len(h)
        
            
    
if __name__ == "__main__":
    Input = [10,9,2,5,3,7,101,18]
    Input1 = [2,2]
    print(Solution1().lengthOfLIS(Input))
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

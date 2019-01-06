# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 15:11:19 2018

@author: hjiang
"""

"""
Given n balloons, indexed from 0 to n-1. 
Each balloon is painted with a number on it represented by array nums. 
You are asked to burst all the balloons. If the you burst balloon i you will get 
nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. 
After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:

You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
Example:

Input: [3,1,5,8]
Output: 167 
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
             
http://www.cnblogs.com/grandyang/p/5006441.html
https://www.youtube.com/watch?v=z3hu2Be92UA 花花巨清楚

重点就是这个状态转移方程： 
dp[left][right] 其实就是假设中间i不动，那么左右就是dp[left][i-1]和dp[i+1][right] 以及中间nums[left-1]*nums[i]*nums[right+1]
"""

# Time:  O(n^3)
# Space: O(n^2)


#class Solution0(object):
#    def maxCoins(self, nums):
#        """
#        :type nums: List[int]
#        :rtype: int
#        """
#        coins = [1] + [i for i in nums if i > 0] + [1]
#        n = len(coins)
#        dp = [[0 for _ in range(n)] for _ in range(n)]
#
#        for k in range(2, n):
#            for left in range(n - k):
#                right = left + k
#                for i in range(left + 1, right):
#                    dp[left][right] = max(dp[left][right],
#                            coins[left] * coins[i] * coins[right] + dp[left][i] + dp[i][right])
#
#        return dp[0][-1]
    
# Time:  O(n^3)
# Space: O(n^2)
class Solution1(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums.insert(0, 1)
        nums.append(1)
        dp = [[0] * (n + 2) for _ in range(n + 2)]#前后都加了一个虚拟气球，变成n+2
        for len_ in range(1, n + 1):#这个地方表示气球序列的长度[1, n]
            for left in range(1, n - len_ + 2):#左边left 是从[1, n-len+1],最左边留一个，然后因为右边加了一个所以是n-len+1
                right = left + len_ - 1 # 这个就是一般长为len_的序列，右边的值
                for k in range(left, right + 1): # 最后搞这个k, k在left和right之间
                    dp[left][right] = max(dp[left][right], \
                      dp[left][k - 1] + nums[left - 1] * nums[k] * nums[right + 1] + dp[k + 1][right])
        return dp[1][n]
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

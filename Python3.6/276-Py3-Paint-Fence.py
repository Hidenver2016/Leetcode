# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 16:15:09 2019

@author: hjiang
"""

"""
There is a fence with n posts, each post can be painted with one of the k colors.

You have to paint all the posts such that no more than two adjacent fence posts have the same color.

Return the total number of ways you can paint the fence.

Note:
n and k are non-negative integers.

Example:

Input: n = 3, k = 2
Output: 6
Explanation: Take c1 as color 1, c2 as color 2. All possible ways are:

            post1  post2  post3      
 -----      -----  -----  -----       
   1         c1     c1     c2 
   2         c1     c2     c1 
   3         c1     c2     c2 
   4         c2     c1     c1  
   5         c2     c1     c2
   6         c2     c2     c1
https://blog.csdn.net/starstar1992/article/details/56286264
可以至多连续两根柱子是同一个颜色
根据题意，不能有超过连续两根柱子是一个颜色，也就意味着第三根柱子要么根第一个柱子不是一个颜色，
要么跟第二根柱子不是一个颜色。如果不是同一个颜色，计算可能性的时候就要去掉之前的颜色，
也就是k-1种可能性。假设dp[1]是第一根柱子及之前涂色的可能性数量，dp[2]是第二根柱子及之前涂色的可能性数量，
则dp[3]=(k-1)*dp[1] + (k-1)*dp[2]。

"""
# Time:  O(n)
# Space: O(n)
# DP solution.
class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return k
        dp = [0] * n
        dp[0] = k
        dp[1] = (k - 1) * dp[0] + k# 第一项是不同的，第二项是相同的
        for i in range(2, n):
            dp[i] = (k - 1) * (dp[i - 1] + dp[i - 2])#要不和第一根不一样，要不就和第二根不一样
        return dp[- 1]

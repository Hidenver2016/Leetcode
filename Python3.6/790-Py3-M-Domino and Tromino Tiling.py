# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 21:32:38 2019

@author: hjiang
"""

"""
We have two types of tiles: a 2x1 domino shape, and an "L" tromino shape. These shapes may be rotated.

XX  <- domino

XX  <- "L" tromino
X
Given N, how many ways are there to tile a 2 x N board? Return your answer modulo 10^9 + 7.

(In a tiling, every square must be covered by a tile. 
Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that 
exactly one of the tilings has both squares occupied by a tile.)

Example:
Input: 3
Output: 5
Explanation: 
The five different ways are listed below, different letters indicates different tiles:
XYZ XXZ XYY XXY XYY
XYZ YYZ XZZ XYY XXY
Note:

N  will be in range [1, 1000].
https://zxi.mytechroad.com/blog/dynamic-programming/leetcode-790-domino-and-tromino-tiling/
"""
class Solution:
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        dp = [[0] * 2 for _ in range(N + 1)]
        dp[0][0] = 1
        dp[1][0] = 1
        for i in range(2, N + 1):
            dp[i][0] = (dp[i - 1][0] + dp[i - 2][0] + 2 * dp[i - 1][1]) % (10 ** 9 + 7)#注意取余数
            dp[i][1] = (dp[i - 2][0] + dp[i - 1][1]) % (10 ** 9 + 7)
        return dp[-1][0]#因为是要返回一个完整的方形
    
    
    
    
    
    
    
    
    
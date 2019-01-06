# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 17:08:45 2019

@author: hjiang
"""

"""
Given a 2D binary matrix filled with 0's and 1's, 
find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""
# Time: O(m*n)
# Space: O(m*n)

#http://bookshadow.com/weblog/2015/06/03/leetcode-maximal-square/
#http://www.cnblogs.com/grandyang/p/4550604.html
class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        if matrix == []:return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                dp[i][j] = int(matrix[i][j])
                if i and j and dp[i][j]: # 这一行避开了下面前面两个循环中的边界条件
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
                ans = max(ans, dp[i][j])
        return ans * ans


#https://blog.csdn.net/fuxuemingzhu/article/details/82992233    
#class Solution1(object):
#    def maximalSquare(self, matrix):
#        """
#        :type matrix: List[List[str]]
#        :rtype: int
#        """
#        if not matrix: return 0
#        M = len(matrix)
#        N = len(matrix[0])
#        dp = [[0] * N for _ in range(M)]
#        for i in range(M):
#            dp[i][0] = int(matrix[i][0])
#        for j in range(N):
#            dp[0][j] = int(matrix[0][j])
#        for i in range(1, M):
#            for j in range(1, N):
#                if int(matrix[i][j]) == 1:
#                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
#        return max(map(max, dp)) ** 2
  
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

dp[i][j] 表示到达 (i, j) 位置所能组成的最大正方形的边长。
对于任意一点 dp[i][j]，由于该点是正方形的右下角，所以该点的右边，下边，右下边都不用考虑，关心的就是左边，上边，和左上边。
这三个位置的dp值 suppose 都应该算好的，还有就是要知道一点，只有当前 (i, j) 位置为1，dp[i][j] 才有可能大于0，否则 dp[i][j] 一定为0。
当 (i, j) 位置为1，此时要看 dp[i-1][j-1], dp[i][j-1]，和 dp[i-1][j] 这三个位置，我们找其中最小的值，并加上1，就是 dp[i][j] 的当前值了，
这个并不难想，毕竟不能有0存在，所以只能取交集，最后再用 dp[i][j] 的值来更新结果 res 的值即可，参见代码如下：
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
  
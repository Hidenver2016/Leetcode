# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 16:27:22 2018

@author: hjiang
"""

"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
当遇到为1的点，将该位置的dp数组中的值清零
"""

class Solution:
# @param obstacleGrid, a list of lists of integers
# @return an integer
#   Time: O(m*n)
#   Space: O((m+1)*(n+1))    
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        ResGrid = [[0 for x in range(n+1)] for x in range(m+1)]
        ResGrid[0][1] = 1#注意！！！！
    
        for i in range(1, m+1):
            for j in range(1, n+1):
                if not obstacleGrid[i-1][j-1]:# 注意下一行的递推关系，这也是上一行为什么需要m+1, n+1了
                    ResGrid[i][j] = ResGrid[i][j-1]+ResGrid[i-1][j]
    
        return ResGrid[m][n]
#   Time: O(m*n)
#   Space: O(n)
    
    def uniquePathsWithObstacles1(self, obstacleGrid):
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        dp = [1] + [0] * (N-1)
        for i in range(M):
            for j in range(N):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j-1]
        return dp[N-1]
    
if __name__ == "__main__":
    A = [[0,0,0],
         [0,1,0],
         [0,0,0]]
    print(Solution().uniquePathsWithObstacles(A))    
    


    
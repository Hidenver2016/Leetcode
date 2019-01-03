# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 15:52:39 2019

@author: hjiang
"""

"""
Given a m x n grid filled with non-negative numbers, 
find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.

关键递推式：grid[i][j] += min(grid[i-1][j], grid[i][j-1])
"""

# Time:  O(m * n)
# Space: O(1)
class Solution:
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        for i in range(1, n):
            grid[0][i] += grid[0][i-1] #边界条件
        for i in range(1, m):
            grid[i][0] += grid[i-1][0] #边界条件
        for i in range(1, m):# 注意，最左边的列和最上面的行都算过了，所以这里i,j就是从1开始
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]
    
if __name__ == "__main__":
    a = [[1,3,1],
         [1,5,1],
         [4,2,1]]
    print(Solution().minPathSum(a))
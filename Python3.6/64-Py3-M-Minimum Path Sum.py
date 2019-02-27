# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 15:31:26 2019

@author: hjiang
"""

"""
Given a m x n grid filled with non-negative numbers, find a path from top left to 
bottom right which minimizes the sum of all numbers along its path.

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
"""

# Time:  O(m * n)
# Space: O(1)

#https://leetcode.com/problems/minimum-path-sum/discuss/23466/Simple-python-dp-70ms
#记住这个套路    
class Solution1:#这个好理解
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        for i in range(1, n):#第一行边界问题
            grid[0][i] += grid[0][i-1]
        for i in range(1, m):#第一列边界问题
            grid[i][0] += grid[i-1][0]
        for i in range(1, m):
            for j in range(1, n):#dp,只有可能来自上面或者右边中间最小的之一
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]
    

# Time:  O(m * n)
# Space: O(m + n)

class Solution(object):#这个高级的以后理解
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        sum = list(grid[0])
        for j in range(1, len(grid[0])):
            sum[j] = sum[j - 1] + grid[0][j]

        for i in range(1, len(grid)):
            sum[0] += grid[i][0]
            for j in range(1, len(grid[0])):
                sum[j] = min(sum[j - 1], sum[j]) + grid[i][j]

        return sum[-1]
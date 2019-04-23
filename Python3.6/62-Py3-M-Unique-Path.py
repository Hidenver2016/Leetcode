# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 15:28:52 2018

@author: hjiang
"""

"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28
采用动态规划。动态规划要求利用到上一次的结果，是一种特殊的迭代思想，动态规划的关键是要得到递推关系式。
对于本题，到达某一点的路径数等于到达它上一点的路径数与它左边的路径数之和。
也即，起点到点(i, j)的路径总数：ways[i][j] = 起点到点(i, j-1)的总数：ways[i][j-1] + 起点到点(i-1, j)总数：ways[i-1][j]。
于是我们就得到递推关系式：ways[i][j] = ways[i][j-1] + ways[i-1][j]

"""

# Time: O(m*n)
# Space: O(m*n)

class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        aux = [[1 for x in range(n)] for x in range(m)]# l里面是n (列),外面是m（行） 注意初始化为1！！！
        for i in range(1, m):
            for j in range(1, n):
                aux[i][j] = aux[i][j-1]+aux[i-1][j]
        return aux[-1][-1]
    
    def uniquePaths1(self, m, n):#这里因为行列对称，所以无所谓
        dp = [[1]*m]*n
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
    
if __name__ == "__main__":
    print(Solution().uniquePaths(7,3))
    print(Solution().uniquePaths1(7,3))
    
    
    
    
    
    
    
    
    
    
    
    
    
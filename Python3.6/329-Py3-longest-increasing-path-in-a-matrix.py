# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 15:12:53 2018

@author: hjiang
"""

"""
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. 
You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

Input: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
Output: 4 
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:

Input: nums = 
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
Output: 4 
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

http://www.cnblogs.com/grandyang/p/5148030.html
关键：用DP， 此题中其实就是DFS加memory, 此题中max_length 矩阵就是dp矩阵
也需要注意这种题目中间函数的定义方法，可以参考题目684 redundant connection
"""
# Time:  O(m * n)
# Space: O(m * n)

#class Solution(object):
#    def longestIncreasingPath(self, matrix):
#        """
#        :type matrix: List[List[int]]
#        :rtype: int
#        """
#        if not matrix:
#            return 0
#
#
#
#        res = 0#           此处表示里面的，或者说列               此处表示外面的， 行     其他以后也是类似，括号越多越里面
#        max_lengths = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
#        for i in range(len(matrix)):
#            for j in range(len(matrix[0])):
#                res = max(res, self.longestpath(matrix, i, j, max_lengths))
#
#        return res
#    def longestpath(self, matrix, i, j, max_lengths):
#        if max_lengths[i][j]:
#            return max_lengths[i][j]
#
#        max_depth = 0
#        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
#        for d in directions:
#            x, y = i + d[0], j + d[1]
#            if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] < matrix[i][j]:
#                max_depth = max(max_depth, self.longestpath(matrix, x, y, max_lengths));
#        max_lengths[i][j] = max_depth + 1
#        return max_lengths[i][j]

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0

        def longestpath(matrix, i, j, max_lengths):
            if max_lengths[i][j]:
                return max_lengths[i][j]

            max_depth = 0
            directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
            for d in directions:
                x, y = i + d[0], j + d[1]
                if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] > matrix[i][j]:
                    max_depth = max(max_depth, longestpath(matrix, x, y, max_lengths));
            max_lengths[i][j] = max_depth + 1
            return max_lengths[i][j]

        res = 0#           此处表示里面的，或者说列               此处表示外面的， 行     其他以后也是类似，括号越多越里面
        max_lengths = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(res, longestpath(matrix, i, j, max_lengths))

        return res    
    
if __name__ == "__main__":
    nums = [[3,4,5],
            [3,2,6],
            [2,2,1]]
    print(Solution().longestIncreasingPath(nums))     
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    

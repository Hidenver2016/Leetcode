# -*- coding: utf-8 -*-
"""
Created on Tue May 28 23:20:02 2019

@author: hjiang
"""

"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false

这个方法好，充分利用二分查找！
先把矩阵拉成一行，确定left和right, 然后取值的时候注意一下矩阵的位置matrix[mid // n][mid % n]
其他都是基本操作
"""
# Time:  O(logm + logn)
# Space: O(1)

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n #不能搞（(m-1)*(n-1)）是错的，m*n只是多算了一个
        while left < right:
            mid = left + (right - left) // 2
            if matrix[mid // n][mid % n] >= target:#这里用最左
                right = mid
            else:
                left = mid + 1

        return left < m * n and matrix[left // n][left % n] == target
    
    
    
    
    
    
    
    
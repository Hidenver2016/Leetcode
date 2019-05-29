# -*- coding: utf-8 -*-
"""
Created on Thu May 23 16:09:18 2019

@author: hjiang
"""

"""
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
# Time:  O(n^2)
# Space: O(1)
#
"""
class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        
        left, right, top, bottom, num = 0, n - 1, 0, n - 1, 1
        
        while left <= right and top <= bottom:
            for j in range(left, right + 1):
                matrix[top][j] = num
                num += 1
            for i in range(top + 1, bottom):
                matrix[i][right] = num
                num += 1
            for j in reversed(range(left, right + 1)):
                if top < bottom:
                    matrix[bottom][j] = num
                    num += 1
            for i in reversed(range(top + 1, bottom)):
                if left < right:
                    matrix[i][left] = num
                    num += 1
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
            
        return matrix
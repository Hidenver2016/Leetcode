# -*- coding: utf-8 -*-
"""
Created on Tue May 28 23:15:34 2019

@author: hjiang
"""

"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

Time: O(m*n*(m+n))
Space: O(1)

技巧：先找到0，对应的非零行列都搞成字母'a'， 这样确保不会覆盖多了
然后只要替换'a'变成0即可。
"""

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        height = len(matrix)
        if(height ==0): return
        width = len(matrix[0])
        for i in range(height):
            for j in range(width):
                if matrix[i][j] == 0:
                    for tmp in range(height):
                        if matrix[tmp][j] != 0:
                            matrix[tmp][j] = 'a'
                    for tmp in range(width):
                        if matrix[i][tmp] != 0: 
                            matrix[i][tmp] = 'a'
    
        for i in range(height):
            for j in range(width):
                if matrix[i][j] == 'a':
                    matrix[i][j] = 0
                
                
                
                
                
                
                
                
                
                
                
                
                
                
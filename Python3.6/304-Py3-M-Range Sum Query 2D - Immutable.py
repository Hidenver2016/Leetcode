# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 11:24:45 2019

@author: hjiang
"""

"""
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by 
its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
Note:
You may assume that the matrix does not change.
There are many calls to sumRegion function.
You may assume that row1 ≤ row2 and col1 ≤ col2.
"""

class NumMatrix:
    def __init__(self, matrix):
        if not matrix:
            return 
        n, m = len(matrix), len(matrix[0])
        self.sum = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                self.sum[i+1][j+1] = self.sum[i+1][j] + self.sum[i][j+1] + matrix[i][j] - self.sum[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        return self.sum[row2+1][col2+1]- self.sum[row1][col2+1] - self.sum[row2+1][col1] + self.sum[row1][col1]
    
    
class NumMatrix1:#看这个
    def __init__(self, matrix):
        self.matrix = matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.matrix[i][j]=self.matrix[i][j]+(self.matrix[i-1][j] if i>0 else 0)+\
                (self.matrix[i][j-1] if j>0 else 0)-(self.matrix[i-1][j-1] if i>0 and j>0 else 0)
    
    def sumRegion(self, row1, col1, row2, col2):
        return self.matrix[row2][col2]+(self.matrix[row1-1][col1-1] if row1>0 and col1>0 else 0)-\
        (self.matrix[row2][col1-1] if col1>0 else 0)-(self.matrix[row1-1][col2] if row1>0 else 0)
        
class NumMatrix2:
    def __init__(self, matrix):
        self.matrix = matrix
        if not matrix: return
        n, m = len(matrix), len(matrix[0])
        self.sum = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                self.sum[i][j] = self.matrix[i][j]+(self.sum[i-1][j] if i>0 else 0)+\
                (self.sum[i][j-1] if j>0 else 0)-(self.sum[i-1][j-1] if i>0 and j>0 else 0)
                
    def sumRegion(self, row1, col1, row2, col2):
        return self.sum[row2][col2] + (self.sum[row1-1][col1-1] if row1 > 0 and col1 > 0 else 0)-\
        (self.sum[row2][col1-1] if col1 > 0 else 0) - (self.sum[row1-1][col2] if row1 > 0 else 0)
        
        
if __name__ == "__main__":
    matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]]

#    A = NumMatrix1(matrix)
    B = NumMatrix2(matrix)
#    print(A.sumRegion(2,1,4,3))
    print(B.sumRegion(2,1,4,3))      
        
        
        
        
        
        
        
        
        
        
        
        
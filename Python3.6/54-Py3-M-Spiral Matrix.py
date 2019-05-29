# -*- coding: utf-8 -*-
"""
Created on Thu May 23 16:08:57 2019

@author: hjiang
"""

"""
Given a matrix of m x n elements (m rows, n columns), 
return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""
class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        result = []
        if matrix == []:
            return result
        
        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        
        while left <= right and top <= bottom:
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            for i in range(top + 1, bottom):
                result.append(matrix[i][right])#上面搞减一加一很复杂主要是为了这里不越界
            for j in reversed(range(left, right + 1)):
                if top < bottom:
                    result.append(matrix[bottom][j])
            for i in reversed(range(top + 1, bottom)):
                if left < right:
                    result.append(matrix[i][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
            
        return result
    
if __name__ == "__main__":
    Input = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]]
    print(Solution().spiralOrder(Input))
    
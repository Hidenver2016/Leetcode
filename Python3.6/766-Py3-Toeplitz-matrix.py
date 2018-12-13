# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 16:22:25 2018

@author: hjiang
"""
"""
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
 

Example 1:

Input:
matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
Output: True
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
Example 2:

Input:
matrix = [
  [1,2],
  [2,2]
]
Output: False
Explanation:
The diagonal "[1, 2]" has different elements.

Note:

matrix will be a 2D array of integers.
matrix will have a number of rows and columns in range [1, 20].
matrix[i][j] will be integers in range [0, 99].

Follow up:

What if the matrix is stored on disk, and the memory is limited such that you can 
only load at most one row of the matrix into the memory at once?
What if the matrix is so large that you can only load up a partial row into the memory at once?
"""
# Time:  O(m * n)
# Space: O(1)

class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for row_index, row in enumerate(matrix):
            for digit_index, digit in enumerate(row):
                if not row_index or not digit_index:
                    continue
                if matrix[row_index - 1][digit_index - 1] != digit:
                    return False
        return True
    
    def anti_diagoanl(self, matrix):
        for row_index, row in enumerate(matrix):
            for digit_index, digit in enumerate(row):
                if not row_index:
                    continue
                if (digit_index + 1)< len(matrix[0]) and (row_index-1)>=0 and matrix[row_index - 1][digit_index + 1] != digit:
                    return False
        return True
    
if __name__ == "__main__":
    m = [[1,2,3,4],
         [5,1,2,3],
         [9,5,1,2]] 
    m1 = [[1,2,3,4],
          [5,1,2,3],
          [9,5,1,2]] 
    m2 = [[1,1,9,2],
          [1,9,2,3],
          [9,2,3,2]]    
    print(Solution().isToeplitzMatrix(m))
    print(Solution().anti_diagoanl(m1))
    print(Solution().anti_diagoanl(m2))    

    
    
    
    
    
    
    
    
    
    
        
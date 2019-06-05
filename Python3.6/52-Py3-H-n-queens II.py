# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 22:03:59 2019

@author: hjiang
"""

"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:

Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""
#
# Time:  O(n!)
# Space: O(n)

class Solution(object):#自带的答案
    # @return an integer
    def totalNQueens(self, n):
        self.cols = [False] * n
        self.main_diag = [False] * (2 * n)
        self.anti_diag = [False] * (2 * n)
        return self.totalNQueensRecu([], 0, n)

    def totalNQueensRecu(self, solution, row, n):
        if row == n:
            return 1#注意
        result = 0
        for i in range(n):
            if not self.cols[i] and not self.main_diag[row + i] and not self.anti_diag[row - i + n]:
                self.cols[i] = self.main_diag[row + i] = self.anti_diag[row - i + n] = True
                result += self.totalNQueensRecu(solution + [i], row + 1, n)#注意
                self.cols[i] = self.main_diag[row + i] = self.anti_diag[row - i + n] = False
        return result
    
    
    
    
    
    
    
    
    
    
    
    
    
    

# -*- coding: utf-8 -*-
"""
Created on Wed May 29 22:54:44 2019

@author: hjiang
"""

"""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
Example 2:

Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being 
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
The given board contain only digits 1-9 and the character '.'.
The given board size is always 9x9.
https://leetcode.com/problems/valid-sudoku/discuss/15460/1-7-lines-Python-4-solutions
此题要点： 
第一： tuple相加很好seen += [(c,j),(i,c),(i//3,j//3,c)]
第二： (c, j)扫描的是第j列有没有重复数字，(i,c)扫描的是第i行有没有重复数字
第三： (i//3,j//3,c)这个是亮点，按照顺序扫描3*3的格子里面有没有重复数字。不是任意的，是按顺序的

"""
class Solution:
    def isValidSudoku(self, board):
        seen = []
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c != '.':
                    seen += [(c,j),(i,c),(i//3,j//3,c)]
#        if len(seen) != len(set(seen)):
#            for i, item in enumerate(seen):
#                for j, temp in enumerate(seen):
#                    if item == temp and j > i:
#                        print(j, temp)
        return len(seen) == len(set(seen))
    
if __name__ == "__main__":
    Input = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]]
    print(Solution().isValidSudoku(Input))
    
    
    
    
    
    
    
    
    


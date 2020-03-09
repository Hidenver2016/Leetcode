# -*- coding: utf-8 -*-
"""
Created on Wed May 29 23:00:58 2019

@author: hjiang
"""

"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.


A sudoku puzzle...


...and its solution numbers marked in red.

Note:

The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9.
"""

class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        self.board = board
        self.solve()
    
    def findUnassigned(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == ".":
                    return row, col
        return -1, -1
    
    def solve(self):
        row, col = self.findUnassigned()
        #no unassigned position is found, puzzle solved
        if row == -1 and col == -1:
            return True
        for num in ["1","2","3","4","5","6","7","8","9"]:
            if self.isSafe(row, col, num):
                self.board[row][col] = num
                if self.solve():
                    return True
                self.board[row][col] = "."
        return False
            
    def isSafe(self, row, col, ch):
        boxrow = row - row%3
        boxcol = col - col%3
        if self.checkrow(row,ch) and self.checkcol(col,ch) and self.checksquare(boxrow, boxcol, ch):
            return True
        return False
    
    def checkrow(self, row, ch):
        for col in range(9):
            if self.board[row][col] == ch:
                return False
        return True
    
    def checkcol(self, col, ch):
        for row in range(9):
            if self.board[row][col] == ch:
                return False
        return True
       
    def checksquare(self, row, col, ch):
        for r in range(row, row+3):
            for c in range(col, col+3):
                if self.board[r][c] == ch:
                    return False
        return True
    
    
    
# Time:  ((9!)^9)
# Space: (1)
#
# Write a program to solve a Sudoku puzzle by filling the empty cells.
# 
# Empty cells are indicated by the character '.'.
# 
# You may assume that there will be only one unique solution.
# 和n queens 一起做

class Solution1:#思路还是backtracking
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        def isValid(board, x, y):
            for i in range(9):
                if i != x and board[i][y] == board[x][y]:
                    return False
            for j in range(9):
                if j != y and board[x][j] == board[x][y]:
                    return False
            i = 3 * (x // 3)
            while i < 3 * (x // 3 + 1):
                j = 3 * (y // 3)
                while j < 3 * (y // 3 + 1):
                    if (i != x or j != y) and board[i][j] == board[x][y]:
                        return False
                    j += 1
                i += 1
            return True
        def isValidSudoku(board):# 这个超时了，但是还是过了三个case, 比较叫容易理解
            seen = []
            for i, row in enumerate(board):
                for j, c in enumerate(row):
                    if c != '.':
                        seen += [(c,j),(i,c),(i//3,j//3,c)]
            return len(seen) == len(set(seen))
        
        def solver(board):
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if(board[i][j] == '.'):
                        for k in range(9):
                            board[i][j] = chr(ord('1') + k)
#                            if isValid(board, i, j) and solver(board):
                            if isValidSudoku(board) and solver(board):
                                return True
                            board[i][j] = '.'
                        return False
            return True

        solver(board)
        
        
        
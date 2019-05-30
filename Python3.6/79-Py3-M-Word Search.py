# -*- coding: utf-8 -*-
"""
Created on Tue May 28 23:36:14 2019

@author: hjiang
"""
"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, 
where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
https://blog.csdn.net/fuxuemingzhu/article/details/79386066
"""
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for y in range(len(board)):
            for x in range(len(board[0])):
                if self.helper(board, word, x, y, 0):
                    return True
        return False
    
    def helper(self, board, word, x, y, i):
        if i == len(word):
            return True
        if x < 0 or x >= len(board[0]) or y < 0 or y >= len(board):
            return False
        if board[y][x] != word[i]:
            return False
        board[y][x] = board[y][x].swapcase()#大小写转换 this IS 变成 THIS is, 这里实际上是一个标记，表示已经访问过了！下次不用再访问！
        ishelper =  self.helper(board, word, x + 1, y, i + 1) or self.helper(board, word, x, y + 1, i + 1) \
                    or self.helper(board, word, x - 1, y, i + 1) or self.helper(board, word, x, y - 1, i + 1)
        board[y][x] = board[y][x].swapcase()#在还原回去，相当于backtracking
        return ishelper

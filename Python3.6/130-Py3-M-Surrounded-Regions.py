# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 15:28:47 2019

@author: hjiang
"""

"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border 
of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not 
connected to an 'O' on the border will be flipped to 'X'. Two cells are connected 
if they are adjacent cells connected horizontally or vertically.
"""

#https://www.cnblogs.com/zuoyuan/p/3765434.html
#http://www.cnblogs.com/grandyang/p/4555831.html

"""
解题思路：这道题可以使用BFS和DFS两种方法来解决。DFS会超时。BFS可以AC。从矩阵的四条边上开始搜索，如果是'O'，
那么搜索'O'周围的元素，并将'O'置换为'D'，这样每条边都DFS或者BFS一遍。而内部的'O'是不会改变的。
这样下来，没有被围住的'O'全都被置换成了'D'，被围住的'O'还是'O'，没有改变。然后遍历一遍，将'O'置换为'X'，将'D'置换为'O'。

我的理解：先找出与四边连着的‘O', 用dfs或bfs找到底，然后改成‘D’。然后剩下的就是被包围的 ”O“, 把这些变成 ”X“.
再把之前的”D“, 变回来即可

"""



# BFS
class Solution2:
    def solve(self, board):
        queue = []
        for row in range(len(board)):
            for col in range(len(board[0])):
                if (row in [0, len(board)-1] or col in [0, len(board[0])-1]) and board[row][col] == "O":
                    queue.append((row, col))
        while queue:
            row, col = queue.pop(0)
            if 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == "O":
                board[row][col] = "D"
    #            queue.append((r-1, c)); queue.append((r+1, c))
    #            queue.append((r, c-1)); queue.append((r, c+1))
                queue += [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
            
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O": board[row][col] = "X"
                elif board[row][col] == "D": board[row][col] = "O"
#        return board
# DFS 爆栈，不建议用              
class Solution3:#
    def solve(self, board):
        m, n = len(board), len(board[0])
        for row in range(m):
            for col in range(n):
                if (row in [0, m - 1] or col in [0, n - 1]) and board[row][col] == 'O':
                    self.helper(board, row, col, m, n)
                    
        for row in range(m):
            for col in range(n):
                if board[row][col] == 'O': board[row][col] = 'X'
                elif board[row][col] == 'D': board[row][col] = 'O'
#        return board
    
    def helper(self, board, row, col, m, n):
        if row < 0 or row >= m or col < 0 or col >= n or board[row][col] != 'O': return
        board[row][col] = 'D'
        self.helper(board, row + 1, col, m, n)
        self.helper(board, row - 1, col, m, n)
        self.helper(board, row, col + 1, m, n)
        self.helper(board, row, col + 1, m, n)
        
if __name__ == "__main__":
    Input = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    print(Solution2().solve(Input))
        
    
        


































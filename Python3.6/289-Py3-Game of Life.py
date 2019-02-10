# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 17:23:15 2019

@author: hjiang
"""

"""
According to the Wikipedia's article: "The Game of Life, also known simply as Life, 
is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). 
Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) 
using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. 
The next state is created by applying the above rules simultaneously to every cell in the current state, 
where births and deaths occur simultaneously.

Example:

Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the same time:
You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, 
which would cause problems when the active area encroaches the border of the array. How would you address these problems?
如果一个活着的部落，其周围少于2个部落，这个部落会死
如果一个活着的部落，其周围部落数在2或者3，这个部落活到下一个迭代中
如果一个活着的部落，其周围多于3个部落，这个部落会死
如果一个死了的部落，其周围多于3个部落，这个部落会活
"""

# Time:  O(m * n)
# Space: O(1)

class Solution(object):#就看这个吧，文西
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0]) if m else 0
        for i in range(m):
            for j in range(n):
                count = 0
                ## Count live cells in 3x3 block.
                for I in range(max(i-1, 0), min(i+2, m)):#三个，考虑边界问题
                    for J in range(max(j-1, 0), min(j+2, n)):#同理三个，考虑边界问题
                        count += board[I][J] & 1

                # if (count == 4 && board[i][j]) means:
                #     Any live cell with three live neighbors lives.
                # if (count == 3) means:
                #     Any live cell with two live neighbors.
                #     Any dead cell with exactly three live neighbors lives.
                if (count == 4 and board[i][j]) or count == 3:#会活的情况
                    board[i][j] |= 2  # Mark as live.就是+2

        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1  # Update to the next state.#其他情况，都是死，这个地方有技巧，上面搞了个+2，那么移位之后自动变成1，感觉机智的不行
                
                
                
#https://blog.csdn.net/fuxuemingzhu/article/details/82809923
#方法很简单暴力，直接求每个位置的8-连通分量并统计部落数就好了，我的做法是先复制了一份，这样使用原始的board去判断部落数，
#更新放在了新的board_next上不会影响之前的board。最后再把数值复制过来。
#
#时间复杂度是O(MN)，空间复杂度是O(MN).
import copy
class Solution1(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if board and board[0]:
            M, N = len(board), len(board[0])
            board_next = copy.deepcopy(board)
            for m in range(M):
                for n in range(N):
                    lod = self.liveOrDead(board, m, n)
                    if lod == 2:
                        board_next[m][n] = 0
                    elif lod == 1:
                        board_next[m][n] = 1
            for m in range(M):
                for n in range(N):
                    board[m][n] = board_next[m][n]
            
    def liveOrDead(self, board, i, j):# return 0-nothing,1-live,2-dead
        ds = [(1, 1), (1, -1), (1, 0), (-1, 1), (-1, 0), (-1, -1), (0, 1), (0, -1)]
        live_count = 0
        M, N = len(board), len(board[0])
        for d in ds:
            r, c = i + d[0], j + d[1]
            if 0 <= r < M and 0 <= c < N:
                if board[r][c] == 1:
                    live_count += 1
        if live_count < 2 or live_count > 3:
            return 2
        elif board[i][j] == 1 or (live_count == 3 and board[i][j] ==0):
            return 1
        else:
            return 0
               
                
                
                
                
                
                
                
                
                
                
                
                
                
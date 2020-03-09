# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 13:17:17 2019

@author: hjiang
"""

"""
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to represent INF 
as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. 
If it is impossible to reach a gate, it should be filled with INF.

Example: 

Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
这个题要找的是最小距离,所有空房间距离门的最小距离
"""

#DFS
#https://leetcode.com/problems/walls-and-gates/discuss/72759/python-dfs-like-number-of-islands
class Solution:
    def wallsAndGates(self, a):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        for i in range(len(a)):
            for j in range(len(a[0])):
                if a[i][j] == 0:#反向来找，从终点找起点，考虑门距离每一个空房间最小的距离
                    self.helper(i,j,a,0)
                       
    def helper(self,x,y,a,dist):  #因为空房间都初始化为最大距离，会被更新，-1是障碍，不会更新
        if x < 0 or y < 0 or x >= len(a) or y >= len(a[0]) or a[x][y] < dist:#小于距离的话就不用再找了，
                return
        a[x][y] = dist
        self.helper(x + 1, y, a,dist + 1)
        self.helper(x - 1, y, a,dist + 1)
        self.helper(x, y + 1, a,dist + 1)
        self.helper(x, y - 1, a,dist + 1)
# Time:  O(m * n)
# Space: O(g)        
#BFS
# BFS
#https://leetcode.com/problems/walls-and-gates/discuss/72764/Python-bfs-solution.
class Solution1:#此题是我自己改的，一定要注意在bfs中关于stack的操作。下面是人家原式，用的是collection中的双向deque        
    def wallsAndGates(self, rooms):#bfs更快
        if not rooms:return 
        r, c= len(rooms), len(rooms[0])
        for i in range(r):
            for j in range(c):
                if rooms[i][j] == 0:
                    queue = [(i+1, j, 1), (i-1, j, 1), (i, j+1, 1), (i, j-1, 1)]
                    while queue:
                        x, y, val = queue.pop(0)
                        if x < 0 or x >= r or y < 0 or y >= c or rooms[x][y] <= val:
                            continue
                        rooms[x][y] = val
                        queue += [(x+1, y, val+1), (x-1, y, val+1), (x, y+1, val+1), (x, y-1, val+1)] 
                        
#import collections
#class Solution1:        
#    def wallsAndGates(self, rooms):
#        if not rooms:return 
#        r, c= len(rooms), len(rooms[0])
#        for i in range(r):
#            for j in range(c):
#                if rooms[i][j] == 0:
#                    queue = collections.deque([(i+1, j, 1), (i-1, j, 1), (i, j+1, 1), (i, j-1, 1)])
#                    while queue:
#                        x, y, val = queue.popleft()
#                        if x < 0 or x >= r or y < 0 or y >= c or rooms[x][y] <= val:
#                            continue
#                        rooms[x][y] = val
#                        queue.extend([(x+1, y, val+1), (x-1, y, val+1), (x, y+1, val+1), (x, y-1, val+1)])













                        
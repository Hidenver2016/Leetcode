# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 00:01:23 2018

@author: hjiang
"""
#
#Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
#An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
#You may assume all four edges of the grid are all surrounded by water.

#Example 1:
#
#Input:
#11110
#11010
#11000
#00000
#
#Output: 1
#Example 2:
#
#Input:
#11000
#11000
#00100
#00011
#
#Output: 3

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        if m == 0: return 0
        n = len(grid[0])
        
        ans = 0
        for y in range(m):
            for x in range(n):
                if grid[y][x] == 1:
                    ans += 1
                    self.__dfs(grid, x, y, n, m) #找遍所有符合要求的点
        return ans, grid
    
    def __dfs(self, grid, x, y, n, m):
        if x < 0 or y < 0 or x >=n or y >= m or grid[y][x] == 0:
            return
        grid[y][x] = 0 # 找过以后置0避免重复查找
        self.__dfs(grid, x + 1, y, n, m) #上下左右循坏查找
        self.__dfs(grid, x - 1, y, n, m)
        self.__dfs(grid, x, y + 1, n, m)
        self.__dfs(grid, x, y - 1, n, m)
        
        
        
class Solution1(object):
    def numIslands(self, grid):
        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count += 1
                    self.dfs(grid, i, j)
                    
        return count, grid

    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != 1:
            return
        grid[i][j] = '#'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
        

        
if __name__ == "__main__":
    grid1 = [[1, 1, 1, 1, 0], [1, 1, 0, 1, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]]
    grid2 = [[1, 1, 1, 1, 0], [1, 1, 0, 1, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]]
    print (Solution1().numIslands(grid1))
    print (Solution1().numIslands(grid2))
    
    
    
    
    
    
    
    
    
    
    
    
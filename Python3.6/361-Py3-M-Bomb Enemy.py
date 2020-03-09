# -*- coding: utf-8 -*-
"""
Created on Wed May 29 22:54:43 2019

@author: hjiang
"""

"""
Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), 
return the maximum enemies you can kill using one bomb.
The bomb kills all the enemies in the same row and column from the planted point 
until it hits the wall since the wall is too strong to be destroyed.
Note: You can only put the bomb at an empty cell.

Example:

Input: [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
Output: 3 
Explanation: For the given grid,

0 E 0 0 
E 0 W E 
0 E 0 0

Placing a bomb at (1,1) kills 3 enemies.
"""

# Time:  O(m * n)
# Space: O(m * n)
#http://www.cnblogs.com/grandyang/p/5599289.html
#这个需要遍历,这个写法和grandyang 的差不多，稍微省一点空间，
#以后刷的时候干脆写成和grandyang一样的好了，四个矩阵，这样比较容易理解
class Solution(object):
    def maxKilledEnemies(self, grid):#看这个可以
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        result = 0
        if not grid or not grid[0]:
            return result

        down = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))] #计算每一个点的下面有多少敌人
        right = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]#计算每一个点的右边有多少敌人
        for i in reversed(range(len(grid))):#从后向前遍历，来填满down和right
            for j in reversed(range(len(grid[0]))):
                if grid[i][j] != 'W':
                    if i + 1 < len(grid):
                        down[i][j] = down[i + 1][j]
                    if j + 1 < len(grid[0]):
                        right[i][j] = right[i][j + 1]
                    if grid[i][j] == 'E':
                        down[i][j] += 1
                        right[i][j] += 1

                    
        up = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))] #计算每一个点的下面有多少敌人
        left = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]#计算每一个点的右边有多少敌人
        for i in range(len(grid)):#从后向前遍历，来填满down和right
            for j in range(len(grid[0])):
                if grid[i][j] != 'W':
                    if i - 1 >= 0:
                        up[i][j] = up[i - 1][j]
                    if j - 1 >= 0:
                        left[i][j] = left[i][j - 1]
                    if grid[i][j] == 'E':
                        up[i][j] += 1
                        left[i][j] += 1
                        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 'E' and grid[i][j] != 'W':
                    result = max(result, left[i][j] + up[i][j] + right[i][j] + down[i][j])

        return result


class Solution1(object):
    def maxKilledEnemies(self, grid):
        if len(grid) == 0:
            return 0
        max_hits = 0
        nums = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        left = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        
        #From Left
        for i in range(len(grid)):
            row_hits = 0
            for j in range(len(grid[0])):
                if grid[i][j] == 'E':
                    row_hits += 1
                elif grid[i][j] == 'W':
                    row_hits = 0
                else:
                    left[i][j] = row_hits
                    
        right = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
                
        #From Right
        for i in range(len(grid)):
            row_hits = 0
            for j in range(len(grid[0])-1, -1, -1):
                if grid[i][j] == 'W':
                    row_hits = 0
                elif grid[i][j] == 'E':
                    row_hits +=1
                else:
                    right[i][j] += row_hits
                    
        up = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]

        for i in range(len(nums[0])):
            col_hits = 0
            for col in range(len(nums)):
                if grid[col][i] == 'E':
                    col_hits += 1
                elif grid[col][i] == 'W':
                    col_hits = 0
                else:
                    up[col][i] += col_hits

        down = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        for i in range(len(nums[0])):
            col_hits = 0
            for col in range(len(nums)-1, -1, -1):
                if grid[col][i] == 'E':
                    col_hits +=1
                elif grid[col][i] == 'W':
                    col_hits = 0
                else:
                    down[col][i] += col_hits
                    # max_hits = max(max_hits, nums[col][i])

        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                result = max(result, left[i][j] + up[i][j] + right[i][j] + down[i][j])
        return result
if __name__ == "__main__":
    grid = [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
    print(Solution().maxKilledEnemies(grid))    
    
    
    
    
    
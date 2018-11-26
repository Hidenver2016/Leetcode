# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 17:26:49 2018

@author: hjiang
"""

"""
We have a grid of 1s and 0s; the 1s in a cell represent bricks.  
A brick will not drop if and only if it is directly connected to the top of the grid, 
or at least one of its (4-way) adjacent bricks will not drop.

We will do some erasures sequentially. Each time we want to do the erasure at the location (i, j), 
the brick (if it exists) on that location will disappear, and then some other bricks may drop because of that erasure.

Return an array representing the number of bricks that will drop after each erasure in sequence.

Example 1:
Input: 
grid = [[1,0,0,0],[1,1,1,0]]
hits = [[1,0]]
Output: [2]
Explanation: 
If we erase the brick at (1, 0), the brick at (1, 1) and (1, 2) will drop. So we should return 2.
Example 2:
Input: 
grid = [[1,0,0,0],[1,1,0,0]]
hits = [[1,1],[1,0]]
Output: [0,0]
Explanation: 
When we erase the brick at (1, 0), the brick at (1, 1) has already disappeared due to the last move. 
So each erasure will cause no bricks dropping.  Note that the erased brick (1, 0) will not be counted as a dropped brick.
 

Note:

The number of rows and columns in the grid will be in the range [1, 200].
The number of erasures will not exceed the area of the grid.
It is guaranteed that each erasure will be different from any other erasure, and located inside the grid.
An erasure may refer to a location with no brick - if it does, no bricks drop.


https://leetcode.com/problems/bricks-falling-when-hit/discuss/119829/Python-Solution-by-reversely-adding-hits-bricks-back
https://xingxingpark.com/Leetcode-803-Bricks-Falling-When-Hit/


将所有击落的砖块，先去除(在Grid矩阵中-1)，接着用DFS找出所有与顶部砖块连通的砖块，
并用一个矩阵connected记录(既表示已经访问过，又表示与顶部连通)。然后，从最后一块被击落的砖块向前逐一恢复。
每次恢复被击落砖块时，在Grid中+1，并且判断该位置是否原来有砖块存在，是否处于顶部或者四周有没有与顶部连通的砖块存在。
若满足这些条件，说明该被击落的砖块可以恢复，并且以它为起点做DFS，所有与他连通的砖块都可以被恢复，
恢复的数量即为该次击落后，落下砖块的数量。
"""


#class Solution0:
class Solution0(object):
    def check_valid(self, r, c, grid):
        if r < 0 or r >= len(grid) or c < 0  or c >= len(grid[0]) or grid[r][c] < 1: # grid[r][c] = 1，此地有砖
            return False
        else:
            return True
        
    def dfs_connect(self, grid, connected, r, c):
        num_connected = 1
        for rr, cc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if self.check_valid(rr, cc, grid) and not connected[rr][cc]: # 需要是之前没有connection的，下面置一才有意义
                connected[rr][cc] = 1
                num_connected += self.dfs_connect(grid, connected, rr, cc)
        return num_connected # 一个联通子图里面有多少块砖
    
    def build_connection(self, grid):
        connected = [[0 for c in range(len(grid[0]))] for r in range(len(grid))] #grid 的 行（elements 数） 和 列 （elements 数）
        for c in range(len(grid[0])):
            if self.check_valid(0, c, grid): # 顶部的砖有多少
                connected[0][c] = 1 #给顶部有砖的位置置一
                self.dfs_connect(grid, connected, 0, c) # 与顶部的砖直接相连的也置一，就是构成联通的都置一
        return connected
    
    def check_new_block_connection(self, r, c, grid, connected):
        if grid[r][c] < 1:
            return False
        if r == 0:
            return True
        for rr, cc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]: #原来有砖，被砸掉了，现在加回来之后grid[r][c] = 1
            if self.check_valid(rr, cc, grid) and connected[rr][cc] == 1:
                return True
        return False
    
    def hitBricks(self, grid, hits): # 主函数
        """
        :type grid: List[List[int]]
        :type hits: List[List[int]]
        :rtype: List[int]
        """
        ret = [0 for i in range(len(hits))]
        for hit in hits:
            grid[hit[0]][hit[1]] -= 1 # 把敲过的砖先去除
        connected = self.build_connection(grid) # 这个地方是建立砖敲掉之后的所有联通子图
        for idx in range(len(hits)):
            r, c = hits[-1 - idx] # 从最后一块砖开始恢复
            grid[r][c] += 1
            if self.check_new_block_connection(r, c, grid, connected):
                connected[r][c] = 1
                add_num = self.dfs_connect(grid, connected, r, c) - 1 #访问grid 和 connect, 看看原来的图里面有多少是可以加上的
                ret[-1 - idx] = add_num
                
        return ret

class Solution:
    def hitBricks(self, grid, hits):
        """
        :type grid: List[List[int]]
        :type hits: List[List[int]]
        :rtype: List[int]
        """

        m, n = len(grid), len(grid[0])
        
        # Connect unconnected bricks and 
        def dfs(i, j):
            if not (0<=i<m and 0<=j<n) or grid[i][j]!=1: # 敲到外面或者敲到没有砖的地方
                return 0
            ret = 1
            grid[i][j] = 2 #remaining unfallen bricks as 2
            ret += sum(dfs(x, y) for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)])
            return ret
        
        # Check whether (i, j) is connected to Not Falling Bricks
        def is_connected(i, j):
            return i==0 or any([0<=x<m and 0<=y<n and grid[x][y]==2 for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]])
        
        # Mark whether there is a brick at the each hit
        for i, j in hits:
            grid[i][j] -= 1
                
        # Get grid after all hits
        for i in range(n):
            dfs(0, i)
        
        # Reversely add the block of each hits and get count of newly add bricks
        ret = [0]*len(hits)
        for k in reversed(range(len(hits))):
            i, j = hits[k]
            grid[i][j] += 1
            if grid[i][j]==1 and is_connected(i, j):
                ret[k] = dfs(i, j)-1
            
        return ret
    
if __name__ == "__main__":
    print(Solution0().hitBricks([[1,0,0,0],[1,1,1,0]], [[1,0]]))
#    print(Solution().hitBricks([[1,0,0,0],[1,1,0,0]], [[1,0]]))
    
    
    
    
    
    
    
    
    
    
    
    
    
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 22:54:43 2019

@author: hjiang
"""

"""
You want to build a house on an empty land which reaches all buildings in the 
shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.
Example:

Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0
dists
[[0, 9, 0, 9, 0], 
 [9, 8, 7, 8, 9],
 [10, 9, 0, 9, 10]]
cnts
[[0, 3, 0, 3, 0],
 [3, 3, 3, 3, 3],
 [3, 3, 0, 3, 3]]

Output: 7 

Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2),
             the point (1,2) is an ideal empty land to build a house, as the total 
             travel distance of 3+3+1=7 is minimal. So return 7.
Note:
There will be at least one building. If it is not possible to build such house according to the above rules, return -1.

这个题就是多了一个障碍和296比较
先建立距离场（从每一个建筑开始，用BFS一遍遍（次数等于建筑的数目）的计算到0位置的距离的总和），然后再计算最小值
这个题目比较难，思想是以每一个楼为起点用BFS建立一个dist的距离场（每一个建筑到各个0位置的总和），直到遍历完所有的建筑物
cnts矩阵是说明对于每一个0位置，计算过几个建筑物。cnts[i][j] == cnt表示所有的建筑物都考虑了，才进行最小值求解
"""

# Time:  O(k * m * n), k is the number of the buildings
# Space: O(m * n)
# 用BFS比较好
#http://www.cnblogs.com/grandyang/p/5297683.html
class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def bfs(grid, dists, cnts, x, y):
            dist, m, n = 0, len(grid), len(grid[0])
            visited = [[False for _ in range(n)] for _ in range(m)]
    
            pre_level = [(x, y)]
            visited[x][y] = True
            while pre_level:
                dist += 1
                cur_level = []
                for i, j in pre_level:
                    for dir in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        I, J = i+dir[0], j+dir[1]
                        if 0 <= I < m and 0 <= J < n and grid[I][J] == 0 and not visited[I][J]:#自动避开2，1等不能够通过的点
                            cnts[I][J] += 1#这个地方满足if grid[i][j] == 1才进来bfs的，所以cnts矩阵中就是每一个零位置来访问的建筑的数量
                            dists[I][J] += dist
                            cur_level.append((I, J))
                            visited[I][J] = True
    
                pre_level = cur_level


        m, n, cnt = len(grid),  len(grid[0]), 0
        dists = [[0 for _ in range(n)] for _ in range(m)]#累计的距离
        cnts = [[0 for _ in range(n)] for _ in range(m)]#每个位置计算过的建筑数量
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:#从每一个建筑开始，计算到0位置的距离，这里也是为什么时间复杂度会有一个k
                    cnt += 1#总建筑数量
                    bfs(grid, dists, cnts, i, j)

        shortest = float("inf")
        for i in range(m):
            for j in range(n):
                if dists[i][j] < shortest and cnts[i][j] == cnt:#cnts[i][j] == cnt表示所有的建筑物都考虑了（对于当前0位置），才进行最小值求解
                    shortest = dists[i][j]

        return shortest if shortest != float("inf") else -1
    
    
if __name__ == "__main__":
    Input = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
    print(Solution().shortestDistance(Input))
    
    
    
    
    
    
    
    
    
    
    
    
    
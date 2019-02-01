# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 14:04:19 2018

@author: hjiang
"""
"""
Given an m x n matrix of positive integers representing the height of each 
unit cell in a 2D elevation map, compute the volume of water it is able to trap after raining.

 

Note:

Both m and n are less than 110. The height of each unit cell is greater than 0 
and is less than 20,000.

 

Example:

Given the following 3x6 height map:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

Return 4.

The above image represents the elevation map [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]] 
before the rain.

After the rain, water is trapped between the blocks. The total volume of water trapped is 4.
"""

# Time:  O(m * n * log(m + n)) ~ O(m * n * log(m * n))
# Space: O(m * n)

"""
The idea is that we maintain all the points of the current border in a min heap 
and always choose the point with the lowest length. This is actually an optimized 
searching strategy over the trivial brute force method: instead of dfs each point 
to find the lowest "border" of its connected component, we can always start 
a search from the lowest border and update the points adjacent to it.

result += max(0, height-heightMap[x][y])# 关键： height 本身在heapq中就已经最小了，而且是从外向内访问
如果heightMap[x][y],比他还小，就可以积水。同时，由于height之前遍历的都比自己大，所以水也不可能留到其他地方去。

http://www.cnblogs.com/grandyang/p/5928987.html 评论里面的解释.
"""
import heapq  
class Solution1(object):
    def trapRainWater(self, heightMap):
        if not heightMap or not heightMap[0]:return 0
          
        m, n = len(heightMap), len(heightMap[0])
        heap = []
        visited = [[0]*n for _ in range(m)]

        # Push all the block on the border into heap 访问最外围一圈，并用visited表示记住的
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m-1 or j == n-1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = 1
        
        result = 0
        while heap:
            height, i, j = heapq.heappop(heap) # 每次弹出最小的点 lowest border   
            for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)): #四个方向的其他点
                if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                    result += max(0, height-heightMap[x][y])# 关键： height 本身在heapq中就已经最小了，如果heightMap[x][y],比他还小，就可以积水，
                    heapq.heappush(heap, (max(heightMap[x][y], height), x, y))#更新
                    visited[x][y] = 1
        return result


    
if __name__ == "__main__":
    A = [
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]]
    print(Solution1().trapRainWater(A))
    
    
#from heapq import heappush, heappop
#
#class Solution0(object):
#    def trapRainWater(self, heightMap):
#        """
#        :type heightMap: List[List[int]]
#        :rtype: int
#        """
#        m = len(heightMap)
#        if not m:
#            return 0
#        n = len(heightMap[0])
#        if not n:
#            return 0
#
#        is_visited = [[False for i in range(n)] for j in range(m)]
#
#        heap = []
#        for i in range(m):
#            heappush(heap, [heightMap[i][0], i, 0])
#            is_visited[i][0] = True
#            heappush(heap, [heightMap[i][n-1], i, n-1])
#            is_visited[i][n-1] = True
#        for j in range(n):
#            heappush(heap, [heightMap[0][j], 0, j])
#            is_visited[0][j] = True
#            heappush(heap, [heightMap[m-1][j], m-1, j])
#            is_visited[m-1][j] = True
#
#        trap = 0
#        while heap:
#            height, i, j = heappop(heap)
#            for (dx, dy) in [(1,0), (-1,0), (0,1), (0,-1)]:
#                x, y = i+dx, j+dy
#                if 0 <= x < m and 0 <= y < n and not is_visited[x][y]:
#                    trap += max(0, height - heightMap[x][y])
#                    heappush(heap, [max(height, heightMap[x][y]), x, y])
#                    is_visited[x][y] = True
#
#        return trap
    
    
##import heapq    
#class Solution2:
#    def trapRainWater(self, heightMap):
#        m, n, heap, trapped = len(heightMap), len(heightMap and heightMap[0]), [], 0
#        for i in range(m):
#            for j in range(n):
#                if i in {0, m - 1} or j in {0, n - 1}:
#                    heapq.heappush(heap, (heightMap[i][j], i, j))
#                    heightMap[i][j] = -1          
#        while heap:
#            h, i, j = heapq.heappop(heap)
#            for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
#                if 0 < x < m - 1 and 0 < y < n - 1 and heightMap[x][y] != -1:
#                    trapped += max(h - heightMap[x][y], 0)
#                    heapq.heappush(heap, (max(heightMap[x][y], h), x, y))
#                    heightMap[x][y] = -1
#        return trapped


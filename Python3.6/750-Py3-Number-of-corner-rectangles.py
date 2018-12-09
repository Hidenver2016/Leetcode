# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 15:59:59 2018

@author: hjiang
"""

"""
Given a grid where each entry is only 0 or 1, find the number of corner rectangles.

A corner rectangle is 4 distinct 1s on the grid that form an axis-aligned rectangle. 
Note that only the corners need to have the value 1. Also, all four 1s used must be distinct.

 

Example 1:

Input: grid = 
[[1, 0, 0, 1, 0],
 [0, 0, 1, 0, 1],
 [0, 0, 0, 1, 0],
 [1, 0, 1, 0, 1]]
Output: 1
Explanation: There is only one corner rectangle, with corners grid[1][2], grid[1][4], grid[3][2], grid[3][4].
 

Example 2:

Input: grid = 
[[1, 1, 1],
 [1, 1, 1],
 [1, 1, 1]]
Output: 9
Explanation: There are four 2x2 rectangles, four 2x3 and 3x2 rectangles, and one 3x3 rectangle.
 

Example 3:

Input: grid = 
[[1, 1, 1, 1]]
Output: 0
Explanation: Rectangles must have four distinct corners.
 

Note:

The number of rows and columns of grid will each be in the range [1, 200].
Each grid[i][j] will be either 0 or 1.
The number of 1s in the grid will be at most 6000.

http://www.cnblogs.com/grandyang/p/8433813.html
https://leetcode.com/problems/number-of-corner-rectangles/discuss/188581/Google-follow-up-question.-A-general-case-solution.

"""

# Time:  O(n * m^2), n is the number of rows with 1s, m is the number of cols with 1s
# Space: O(n * m)

class Solution(object):
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = [[c for c, val in enumerate(row) if val] for row in grid] #把非零的位置标记出来
        result = 0
        for i in range(len(rows)):
            lookup = set(rows[i])
            for j in range(i):
                count = sum(1 for c in rows[j] if c in lookup)
                result += count*(count-1)//2
        return result
    
class Solution1:
    def countCornerRectangles(self, grid):
        m = len(grid)
        n = len(grid[0])
        res = 0
        for t in range(0, 10):#此处升级难度，改为任意数字
            for i in range(m):# 行遍历
                for j in range(i+1, m):#下面的行遍历
                    cnt = 0
                    for k in range(n):# 列遍历
                        if (grid[i][k] == t and grid[j][k] == t):
                            cnt += 1
                    res += cnt * (cnt - 1)//2#关键 列遍历完毕k, 实际是有cnt-1个格子，最后的rec是由cnt * (cnt - 1)//2，省了一个循环
        return res
            
    
if __name__ == "__main__":
    grid = [[1, 0, 0, 1, 0],
             [0, 0, 1, 0, 1],
             [0, 0, 0, 1, 0],
             [1, 0, 1, 0, 1]]
    grid1 = [[1, 1, 1],
             [0, 0, 0],
             [1, 1, 0]]
    grid2 =[[7, 9, 6, 1, 7],
            [8, 1, 0, 2, 1],
            [7, 0, 1, 0, 7],
            [1, 1, 6, 1, 1],
            [5, 2, 9, 7, 1]]
    print(Solution1().countCornerRectangles(grid2))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



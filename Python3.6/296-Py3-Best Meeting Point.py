# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 15:42:50 2019

@author: hjiang
"""

"""
A group of two or more people wants to meet and minimize the total travel distance. 
You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group. 
The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

Example:

Input: 

1 - 0 - 0 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 6 

Explanation: Given three people living at (0,0), (0,4), and (2,2):
             The point (0,2) is an ideal meeting point, as the total travel distance 
             of 2+2+2=6 is minimal. So return 6.
http://www.cnblogs.com/grandyang/p/5291058.html
______C_____A_____P_______B______D______

我们通过分析可以得出，P点的最佳位置就是在[A, B]区间内，这样和四个点的距离之和为AB距离加上CD距离，
在其他任意一点的距离都会大于这个距离，那么分析出来了上述规律，这题就变得很容易了，我们只要给位置排好序，
然后用最后一个坐标减去第一个坐标，即CD距离，倒数第二个坐标减去第二个坐标，即AB距离，以此类推，直到最中间停止，
那么一维的情况分析出来了，二维的情况就是两个一维相加即可，参见代码如下：
"""
#Time: O(m*n)
#Space: O(m+n)

class Solution:# 参考grandyang的答案自己写的
    def minTotalDistance(self, grid):
        rows = []
        cols = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    rows.append(i)
                    cols.append(j)
        
        return self.minDistance(rows) + self.minDistance(cols)
    
    def minDistance(self, list1):
        res = 0
        list1.sort()
        i, j = 0, len(list1) - 1
        while i < j:
            res += list1[j] - list1[i]
            j -= 1
            i += 1
        return res
    
        
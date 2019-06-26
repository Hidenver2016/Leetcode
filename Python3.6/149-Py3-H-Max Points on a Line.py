# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 15:12:23 2019

@author: hjiang
"""

"""
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Example 1:

Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o  
+------------->
0  1  2  3  4
Example 2:

Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6
NOTE: input types have been changed on April 15, 2019. 
Please reset to default code definition to get new method signature.
https://blog.csdn.net/fuxuemingzhu/article/details/83927183
我们不要直接计算斜率，而是相当于最简分式的形式，使用pair或者Python中的tuple，
保存已经化为最简分数的两个数值，然后使用字典来统计这个pair出现了多少次。

最后的结果是共线并且不重合的点的最大个数+重叠的点的个数。

时间复杂度是O(N^2)，空间复杂度是O(N)。
"""
import collections
# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        N = len(points)
        res = 0
        for i in range(N):
            lines = collections.defaultdict(int)
            duplicates = 1
            for j in range(i + 1, N):
                if points[i].x == points[j].x and points[i].y == points[j].y:
                    duplicates += 1
                    continue
                dx = points[i].x - points[j].x
                dy = points[i].y - points[j].y
                delta = self.gcd(dx, dy)
                lines[(dx / delta, dy / delta)] += 1
            res = max(res, (max(lines.values()) if lines else 0) + duplicates)
        return res
                
    def gcd(self, x, y):
        return x if y == 0 else self.gcd(y, x % y)





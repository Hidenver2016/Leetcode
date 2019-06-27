# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 15:13:14 2019

@author: hjiang
"""

"""
Given n points on a 2D plane, find if there is such a line parallel to y-axis that reflect the given points.

Example 1:

Input: [[1,1],[-1,1]]
Output: true
Example 2:

Input: [[1,1],[-1,-1]]
Output: false
Follow up:
Could you do better than O(n^2) ?
"""
import collections
# Time:  O(n)
# Space: O(n)

# Hash solution.
class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if not points:
            return True
        groups_by_y = collections.defaultdict(set)
        left, right = float("inf"), float("-inf")
        for p in points:
            groups_by_y[p[1]].add(p[0])# 用y为key,加上对应的x
            left, right = min(left, p[0]), max(right, p[0])
        mid = left + right
        for group in groups_by_y.values():#对于同一个y的所有x值， 如果x和mid-x都在，那么这两个点关于mid对称
            for x in group:
                if mid - x not in group:
                    return False
        return True
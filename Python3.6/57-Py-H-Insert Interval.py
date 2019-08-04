# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 15:28:29 2019

@author: hjiang
"""

"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
# Time:  O(n)
# Space: O(1)
#这个题的关键就是：第一intervals是按照顺序排列的，第二intervals之间本身没有交集，第三只有一个newIneterval
#第一，把intervals[i].end < newInterval.start的全部放入res
#第二，当intervals[i].start =< newInterval.end的时候， newInterval = Interval(min(intervals[i].start, newInterval.start), max(newInterval.end, intervals[i].end))
# res += newInterval; res += intervals[i:](加上剩下的)
"""



class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return "[{}, {}]".format(self.start, self.end)


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        result = []
        i = 0
        while i < len(intervals) and newInterval.start > intervals[i].end:#没有交集的，小的interval, 先都加进去
            result += intervals[i],
            i += 1
        while i < len(intervals) and newInterval.end >= intervals[i].start:#取并集, 
            newInterval = Interval(min(newInterval.start, intervals[i].start), max(newInterval.end, intervals[i].end))
            i += 1
        result += newInterval,
        result += intervals[i:]
        return result









# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 13:30:43 2018

@author: hjiang
"""
"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considerred overlapping.

关键：
Just go through the intervals sorted by start coordinate and 
either combine the current interval with the previous one if they overlap, 
or add it to the output by itself if they don't.
"""

# Time:  O(nlogn)
# Space: O(1)

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
        
    def __repr__(self):
        return "[{}, {}]".format(self.start, self.end)

#
class Solution1:
    def merge(self, intervals):
        out = []
        for i in sorted(intervals, key=lambda i: i.start):
            if out and i.start <= out[-1].end:
                out[-1].end = max(out[-1].end, i.end)
            else:
                out += i,
        return out
        
if __name__ == "__main__":
    print (Solution1().merge([Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15,18)]))
    
#
#
#class Solution(object):
#    def merge(self, intervals):
#        """
#        :type intervals: List[Interval]
#        :rtype: List[Interval]
#        """
#        if not intervals:
#            return intervals
#        intervals.sort(key=lambda x: x.start)
#        result = [intervals[0]]
#        for i in xrange(1, len(intervals)):
#            prev, current = result[-1], intervals[i]
#            if current.start <= prev.end: 
#                prev.end = max(prev.end, current.end)
#            else:
#                result.append(current)
#        return result
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

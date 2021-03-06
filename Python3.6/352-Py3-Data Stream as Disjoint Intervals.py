# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 17:04:37 2019

@author: hjiang
"""

"""
Given a data stream input of non-negative integers a1, a2, ..., an, ..., 
summarize the numbers seen so far as a list of disjoint intervals.

For example, suppose the integers from the data stream are 1, 3, 7, 2, 6, ..., then the summary will be:

[1, 1]
[1, 1], [3, 3]
[1, 1], [3, 3], [7, 7]
[1, 3], [7, 7]
[1, 3], [6, 7]

empty + 1 = [1,1]
[1,1] , [4,4] + 6 = [1,1], [4,4] , [6,6]
[1,1] , [3,3] + 2 = [1,3]
[1,1] , [4,4] + 5 = [1,1] , [4,5]
[1,1] , [4,4] + 3 = [1,1] , [3,4]
[1,2,3] + [5,6,7] + 4 = [1,2,3,4,5,6,7]
Follow up:
What if there are lots of merges and the number of disjoint intervals are small compared to the data stream's size?
https://leetcode.com/problems/data-stream-as-disjoint-intervals/discuss/82548/Share-my-python-solution-using-heap

Since there is no standard TreeMap library for python, I am implementing this structure with a min heap.
The idea is straight froward:
Append interval to heap when addNum called
Merge intervals when getIntervals called
比较好理解，就是格式感觉比较烦
"""
import heapq
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
        
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
        
class SummaryRanges(object):

  def __init__(self):
    self.intervals = []
    
  def addNum(self, val):
    heapq.heappush(self.intervals, (val, Interval(val, val)))
    
  def getIntervals(self):
    stack = []
    while self.intervals:
        idx, cur = heapq.heappop(self.intervals)
        if not stack:
            stack.append((idx, cur))
        else:
            _, prev = stack[-1]
            if prev.end + 1 >= cur.start:
                prev.end = max(prev.end, cur.end)
            else:
                stack.append((idx, cur))
    self.intervals = stack
    return list(map(lambda x: x[1], stack))














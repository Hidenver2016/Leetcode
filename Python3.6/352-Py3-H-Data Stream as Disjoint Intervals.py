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
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
        
class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.heap = []

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        if val not in (x[0] for x in self.heap): #check if have the same key before
            heapq.heappush(self.heap, (val, Interval(val, val)))

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        stack = []
        while self.heap:
            val, cur = heapq.heappop(self.heap)
            if not stack:
                stack.append((val,cur))
            else:
                _, prev = stack[-1]
                if cur.start <= prev.end+1:
                    prev.end = max(prev.end, cur.end)
                else:
                    stack.append((val,cur))
        self.heap = stack
        return list(map(lambda x: x[1], stack))
"""
土办法也work
nums = [1, 3, 7, 2, 6]
nums.sort()
res = []
temp = [nums[0], nums[0]]
for i in range(1, len(nums)):
    if nums[i] == nums[i-1] + 1 and temp:
	    temp[-1] = nums[i]
    elif nums[i] == nums[i-1]:
	    continue
    else:
	    res.append(temp)
	    temp = []
	    temp = [nums[i], nums[i]]
res.append(temp)
print(res)
"""










# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 16:41:07 2019

@author: hjiang
"""

"""
Given an array of meeting time intervals consisting of start and end times 
[[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
https://leetcode.com/problems/meeting-rooms-ii/discuss/67917/Python-heap-solution-with-comments.
heap里面存储的是截止时间，如果i.start>=heap[0] （最先结束会议的时间），那么就合并会议时间；否则压入heap。
最后返回heap长度
"""
import heapq
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def minMeetingRooms(self, intervals):
        intervals.sort(key=lambda x:x.start)
        heap = []  # stores the end time of intervals
        for i in intervals:
            if heap and i.start >= heap[0]: 
                # means two intervals can use the same room
                heapq.heapreplace(heap, i.end) #合并时间
            else:
                # a new room is allocated
                heapq.heappush(heap, i.end)
        return len(heap)

if __name__ == "__main__":
    print(Solution().minMeetingRooms([Interval(0, 30), Interval(5, 10), Interval(15, 20)]))
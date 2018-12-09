# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 14:29:52 2018

@author: hjiang
"""

"""
We are given a list of (axis-aligned) rectangles.  
Each rectangle[i] = [x1, y1, x2, y2] , where (x1, y1) are the coordinates of 
the bottom-left corner, and (x2, y2) are the coordinates of the top-right corner of the ith rectangle.

Find the total area covered by all rectangles in the plane.  
Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:

Input: [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
Output: 6
Explanation: As illustrated in the picture.
Example 2:

Input: [[0,0,1000000000,1000000000]]
Output: 49
Explanation: The answer is 10^18 modulo (10^9 + 7), which is (10^9)^2 = (-7)^2 = 49.
Note:

1 <= rectangles.length <= 200
rectanges[i].length = 4
0 <= rectangles[i][j] <= 10^9
The total area covered by all rectangles will never exceed 2^63 - 1 
and thus will fit in a 64-bit signed integer.
"""

#https://leetcode.com/articles/rectangle-area-ii/
    
#Complexity Analysis
#
#Time Complexity: O(N^2 log N) where N is the number of rectangles.
#
#Space Complexity: O(N). 
        
"""
For a rectangle like rec = [1,0,3,1], the first update is to add [1, 3] 
to the active set at y = 0, and the second update is to remove [1, 3] at y = 1. 
Note that adding and removing respects multiplicity - if we also added [0, 2] at y = 0, 
then removing [1, 3] at y = 1 will still leave us with [0, 2] active.

This gives us a plan: create these two events for each rectangle, 
then process all the events in sorted order of y. 
The issue now is deciding how to process the events add(x1, x2) and remove(x1, x2) 
such that we are able to query() the total horizontal length of our active intervals.

We can use the fact that our remove(...) operation will always be on an interval 
that was previously added. Let's store all the (x1, x2) intervals in sorted order. 
Then, we can query() in linear time using a technique similar to a classic LeetCode problem:
56 Merge Intervals.
思路：二维转一维：扫描y轴，遍历每个y范围，然后求出与改y范围有相交的x范围，merge这些x的interval
"""   
class Solution(object):
    def rectangleArea(self, rectangles):
        # Populate events
        OPEN, CLOSE = 0, 1
        events = []
        for x1, y1, x2, y2 in rectangles:
            events.append((y1, OPEN, x1, x2))
            events.append((y2, CLOSE, x1, x2))
        events.sort()

        def query():# 计算同一个高度，x 轴所覆盖的最大宽度，等价于多个x1, x2，如何求并集
            ans = 0
            cur = -1
            for x1, x2 in active:
                cur = max(cur, x1)
                ans += max(0, x2 - cur)
                cur = max(cur, x2)
            return ans

        active = []
        cur_y = events[0][0]
        ans = 0
        for y, typ, x1, x2 in events:
            # For all vertical ground covered, update answer
            ans += query() * (y - cur_y)

            # Update active intervals
            if typ is OPEN:#此处其实是根据typ来更新x1,x2的坐标
                active.append((x1, x2))
                active.sort()
            else:    
                active.remove((x1, x2))

            cur_y = y#更新y

        return ans % (10**9 + 7)
    
if __name__ == "__main__":
    print(Solution().rectangleArea([[0,0,2,2],[1,0,2,3],[1,0,3,1]]))
    
    
    
    
    
    
    
    
    
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 14:01:07 2018

@author: hjiang
"""
'''
Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. 
There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. 
For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

Example 1:

Input: "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.  
It is not 19:33, because this occurs 23 hours and 59 minutes later.
Example 2:

Input: "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. 
It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.
Time: O(1)
Space: O(1)
'''

class Solution(object):
    def nextClosestTime(self, time):
        num1 = time.split(":")
#        set1 = set("".join(num1))
        vec1 = int(num1[0]) * 60 + int(num1[1])
        result = None
        for i in range(1 + vec1, 60*24 +1+ vec1):
            t = i % 1440
            h, m = t // 60, t % 60
            result = "%02d:%02d" %(h,m)
            if set(result) <= set(time): # 这个地方表示集合从属关系
                return result
        
        
if __name__ == "__main__":
    print(Solution().nextClosestTime('19:34'))
    print(Solution().nextClosestTime('23:34'))
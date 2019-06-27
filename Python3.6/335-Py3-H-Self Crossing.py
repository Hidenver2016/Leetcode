# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 15:09:15 2019

@author: hjiang
"""

"""
You are given an array x of n positive numbers. You start at point (0,0) and moves x[0] metres to the north, 
then x[1] metres to the west, x[2] metres to the south, x[3] metres to the east and so on. 
In other words, after each move your direction changes counter-clockwise.

Write a one-pass algorithm with O(1) extra space to determine, if your path crosses itself, or not.

 

Example 1:

┌───┐
│   │
└───┼──>
    │

Input: [2,1,1,2]
Output: true
Example 2:

┌──────┐
│      │
│
│
└────────────>

Input: [1,2,3,4]
Output: false 
Example 3:

┌───┐
│   │
└───┼>

Input: [1,1,1,1]
Output: true 
https://leetcode.com/problems/self-crossing/discuss/79141/Another-python...
https://www.cnblogs.com/grandyang/p/5216856.html

这个感觉太扯淡了
"""

def isSelfCrossing(self, x):
    b = c = d = e = 0
    for a in x:
        if d >= b > 0 and (a >= c or a >= c-e >= 0 and f >= d-b):
            return True
        b, c, d, e, f = a, b, c, d, e
    return False
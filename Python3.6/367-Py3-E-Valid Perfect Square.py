# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 22:23:31 2019

@author: hjiang
"""

"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false
和69一模一样！
"""

class Solution:
    def isPerfectSquare(self, num):
        r = num
        while r*r > num:
            r = int((r + num/r) / 2)
        return r*r == num
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 11:14:35 2019

@author: hjiang
"""

"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed 
integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 
0 when the reversed integer overflows.
https://blog.csdn.net/fuxuemingzhu/article/details/79258815
"""
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0: sign = 1
        if x < 0: sign = -1
        n = sign * int(str(abs(x))[::-1])#注意，str才可以搞[::-1]
        return n if n.bit_length() < 32 else 0

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 22:39:07 2019

@author: hjiang
"""

"""
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example 1:

Input: 6
Output: true
Explanation: 6 = 2 × 3
Example 2:

Input: 8
Output: true
Explanation: 8 = 2 × 2 × 2
Example 3:

Input: 14
Output: false 
Explanation: 14 is not ugly since it includes another prime factor 7.
Note:

1 is typically treated as an ugly number.
Input is within the 32-bit signed integer range: [−231,  231 − 1].
#--------------------- 

#原文：https://blog.csdn.net/fuxuemingzhu/article/details/49183961 

"""
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0: return False
        while num % 2 == 0:
            num /= 2  #注意，这个地方由于上面限制了，所以/=没有关系，一般还是要写成//=
        while num % 3 == 0:
            num /= 3
        while num % 5 == 0:
            num /= 5
        return num == 1

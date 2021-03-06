# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 11:17:10 2019

@author: hjiang
"""

"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, 
and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        tmp = ""
        for i, d in enumerate(digits):
            tmp = tmp + str(d)
        
        num = str(int(tmp) + 1)
        
        return [int(d) for d in num]
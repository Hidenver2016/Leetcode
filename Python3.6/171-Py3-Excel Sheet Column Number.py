# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 15:58:43 2019

@author: hjiang
"""

"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701
"""
# Time:  O(n)
# Space: O(1)

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for i in range(len(s)):
            result *= 26
            result += ord(s[i]) - ord('A') + 1
        return result

# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 15:57:37 2019

@author: hjiang
"""

"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"
"""
# Time:  O(logn)
# Space: O(1)

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result, dvd = "", n

        while dvd:
            result += chr((dvd - 1) % 26 + ord('A'))
            dvd = (dvd - 1) // 26

        return result[::-1]
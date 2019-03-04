# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 15:40:56 2019

@author: hjiang
"""

"""
Given a string, determine if a permutation of the string could form a palindrome.

Example 1:

Input: "code"
Output: false
Example 2:

Input: "aab"
Output: true
Example 3:

Input: "carerac"
Output: true
"""
# Time:  O(n)
# Space: O(1)

import collections


class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return sum(v % 2 for v in collections.Counter(s).values()) < 2 #只能有一个字母是奇数
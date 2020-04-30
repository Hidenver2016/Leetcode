# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 15:54:37 2020

@author: hjiang
"""

"""
Given a string which consists of lowercase or uppercase letters, 
find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.

https://leetcode.com/problems/longest-palindrome/discuss/89614/python-simple-set-solution
"""

class Solution(object):
    def longestPalindrome(self, s):#看看各种组合中最长的回文是什么，那么只要找出所有的单数字母的补集，加1即可
        """
        :type s: str
        :rtype: int
        """
        hash = set()
        for c in s:
            if c not in hash:
                hash.add(c)
            else:
                hash.remove(c)
        # len(hash) is the number of the odd letters
        return len(s) - len(hash) + 1 if len(hash) > 0 else len(s)
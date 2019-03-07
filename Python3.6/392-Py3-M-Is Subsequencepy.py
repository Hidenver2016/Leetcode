# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 23:23:07 2019

@author: hjiang
"""

"""
Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t 
is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string 
by deleting some (can be none) of the characters without disturbing the relative positions 
of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"

Return true.

Example 2:
s = "axc", t = "ahbgdc"

Return false.

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want 
to check one by one to see if T has its subsequence. In this scenario, how would you change your code?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.
"""

# Time:  O(n)
# Space: O(1)

class Solution(object):#中规中矩的速度,自己改了反而比较好一点
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True

        i = 0
        for c in t:
            if c == s[i]:
                i += 1
            if i == len(s):
#                break
                return True
#        return i == len(s)
        return False
    
class Solution1(object):#这个最快，也没有解释，需要研究一下
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        index = -1
        for item in s:
            index = t.find(item, index+1)
            if index == -1:
                return False
        return True
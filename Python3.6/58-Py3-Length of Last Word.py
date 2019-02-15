# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 17:18:05 2019

@author: hjiang
"""

"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', 
return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
"""
# Time:  O(n)
# Space: O(1)

class Solution(object):
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        length = 0
        for i in reversed(s):
            if i == ' ':
                if length:
                    break
            else:
                length += 1
        return length

# Time:  O(n)
# Space: O(n)
class Solution2(object):
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        return len(s.strip().split(" ")[-1])
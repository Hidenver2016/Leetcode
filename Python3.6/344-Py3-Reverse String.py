# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 17:22:32 2019

@author: hjiang
"""
"""
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

 

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""
# Time:  O(n)
# Space: O(n)

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        string = list(s)
        i, j = 0, len(string) - 1
        while i < j:
            string[i], string[j] = string[j], string[i]
            i += 1
            j -= 1
        return "".join(string)


# Time:  O(n)
# Space: O(n)
class Solution2(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]#查一下这个空间复杂度
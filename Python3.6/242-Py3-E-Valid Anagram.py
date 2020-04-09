# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 15:45:35 2019

@author: hjiang
"""

"""
颠倒字母而成的字（anagram的复数形式）；（用复数）字谜
Given two strings s and t , write a function to determine if t is an anagram of s..

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""
#Time: O(n)
#Space: O(1) 字母的个数也是有限个的，只有26个，所以怎么都是常数
from collections import Counter
class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t): return False
        return not (Counter(s) - Counter(t))
    
if __name__ == "__main__":
    print(Solution().isAnagram("anagram","nagaram"))
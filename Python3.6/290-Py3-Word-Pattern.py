# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 17:42:56 2019

@author: hjiang
"""

"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern 
and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase 
letters separated by a single space.
原文：https://blog.csdn.net/fuxuemingzhu/article/details/72528424 
两次遍历，这样基本不会有漏网的
和205是一道题目
"""

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        strs = str.split()
        if len(pattern) != len(strs): return False
        d = dict()
        for i, p in enumerate(pattern): #d = {'a': 'dog', 'b': 'cat'}
            if p not in d: d[p] = strs[i]
            elif d[p] != strs[i]: return False
        d = dict()
        for i, p in enumerate(strs):# d = {'dog': 'a', 'cat': 'b'}
            if p not in d: d[p] = pattern[i]
            elif d[p] != pattern[i]: return False
        return True
    
    
if __name__ == "__main__":
    print(Solution().wordPattern("abba", "dog cat cat dog"))
    
    



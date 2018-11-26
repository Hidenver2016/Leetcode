# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 13:47:25 2018

@author: hjiang
"""
"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.
"""

class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        s2t, t2s = {}, {}
        for p, w in zip(s, t):
            if w not in s2t and p not in t2s:
                s2t[w] = p
                t2s[p] = w
            elif w not in s2t or s2t[w] != p:
                # Contradict mapping.
                return False
        return True
            
            
            
    def isIsomorphic1(self, s, t): #优秀
        return len(set(zip(s, t))) == len(set(s)) and len(set(zip(t, s))) == len(set(t))#算两遍
    
    def isIsomorphic2(self, s, t):
        d1, d2 = [[] for _ in range(256)], [[] for _ in range(256)]
        for i, val in enumerate(s):
            d1[ord(val)].append(i)
        for i, val in enumerate(t):
            d2[ord(val)].append(i)
        return sorted(d1) == sorted(d2)
    
    
    
    
if __name__ == "__main__":
    print(Solution().isIsomorphic2("foo","bar"))
    print(Solution().isIsomorphic2("paper","title"))
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 15:41:55 2019

@author: hjiang
"""

"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
https://leetcode.com/problems/longest-palindromic-substring/discuss/2954/Python-easy-to-understand-solution-with-comments-(from-middle-to-two-ends).
算法是从中间向两边扩展

"""
#O(n^2)
#O(n)
class Solution:
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):   #O(n)     
            odd  = self.palindromeAt(s, i, i)# odd case, like "aba"
            even = self.palindromeAt(s, i, i+1)# even case, like "abba"
            
            res = max(res, odd, even, key=len)
        return res
 
    # starting at l,r expand outwards to find the biggest palindrome
    def palindromeAt(self, s, l, r):    
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r] # O(n) 正好是之前算过的从l到r 相当于l-=1和r+=1后，两边各自缩进一位
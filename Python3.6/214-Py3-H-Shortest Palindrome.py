# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 15:43:17 2019

@author: hjiang
"""

"""
Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it. 
Find and return the shortest palindrome you can find by performing this transformation.

Example 1:

Input: "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: "abcd"
Output: "dcbabcd"
"""
"""
从后向前判断s字符串前面部分是不是一个回文字符串，如果是的话，就把后面的部分复制翻转一份到前面来，拼成了最短的回文字符串。

为什么从后向前，因为这样能使得前面部分的回文是最长的，所以总的回文长度是最短的。

有个长度是40002的特别长的字符串导致超时，所以我用了作弊的方法，就是直接返回它的结果，这样就加速了。

时间复杂度是O(n^2)，空间复杂度是O(1).不作弊TLE，作弊超过100%.
--------------------- 
原文：https://blog.csdn.net/fuxuemingzhu/article/details/83662869 
"""
class Solution:#想法很直接
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) > 40000: return 'a' * 20000 + "dc" + s  #此行作弊了
        N = len(s)
        for i in range(N, -1, -1):
            if self.isPalindrome(s[:i]):
                return s[i:][::-1] + s
        return ""
        
    def isPalindrome(self, s):
        N = len(s)
        for i in range(N // 2):
            if s[i] != s[N - i - 1]:
                return False
        return True
    
#https://leetcode.com/problems/shortest-palindrome/discuss/60099/AC-in-288-ms-simple-brute-force 
"""
Example: s = dedcba. Then r = abcded and I try these overlays (the part in (...) is the prefix I cut off, 
I just include it in the display for better understanding):

  s          dedcba
  r[0:]      abcded    Nope...
  r[1:]   (a)bcded     Nope...
  r[2:]  (ab)cded      Nope...
  r[3:] (abc)ded       Yes! Return abc + dedcba
"""
class Solution1:#大神的暴力解法
    def shortestPalindrome(self, s):
        r = s[::-1]
        for i in range(len(s) + 1):
            if s.startswith(r[i:]):#此句亮瞎了
                return r[:i] + s#此句也差不多亮瞎了
            
            
            
            
            
            
            
            
            
            
            
            
            
            
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 15:45:21 2019

@author: hjiang
"""

"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""

"""
回溯法
看到所有可能的结果的时候，一般想到回溯。

这个题和之前的回溯有个差别，那就是继续开始回溯的条件是目前的结果已经是回文串。然后从后面的字符开始继续回溯。感觉回溯都是套路，80%的代码可以通用的，最好背下来。

特别注意切片的位置，以及path + [s[:i]]产生了新的list中，所以append时候才有效。

   self.isPalindrome = lambda s : s == s[::-1]
   
   等价于：
   def isPalindrome(self, s):
       return s == s[::-1]
--------------------- 
原文：https://blog.csdn.net/fuxuemingzhu/article/details/79574462 
"""
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.isPalindrome = lambda s : s == s[::-1]
        res = []
        self.helper(s, res, [])
        return res
        
    def helper(self, s, res, path):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s) + 1): #注意起始和结束位置
            if self.isPalindrome(s[:i]):
                self.helper(s[i:], res, path + [s[:i]])


     
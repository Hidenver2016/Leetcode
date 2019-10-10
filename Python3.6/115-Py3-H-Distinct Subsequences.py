# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 23:23:44 2019

@author: hjiang
"""

"""
Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original 
string by deleting some (can be none) of the characters without disturbing 
the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Example 1:

Input: S = "rabbbit", T = "rabbit"
Output: 3
Explanation:

As shown below, there are 3 ways you can generate "rabbit" from S.
(The caret symbol ^ means the chosen letters)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^
Example 2:

Input: S = "babgbag", T = "bag"
Output: 5
Explanation:

As shown below, there are 5 ways you can generate "bag" from S.
(The caret symbol ^ means the chosen letters)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^
    
题目大意
求S中有多少个子序列等于T。

解题方法
动态规划


应该这样理解： 
1. dp[i][j]表示s[1:j] 和 t[1:i]中间有多少个t是s的子集，即符合题意的有多少。
    （花花的笔记http://zxi.mytechroad.com/blog/dynamic-programming/leetcode-115-distinct-subsequences/）
    
2. 如果t是空集，那么所有长度的s对他来说只有空集满足，所以dp[0][*] = 1 对于所有的j都是1.这也能看出上面就是从1开始的，0是空集

3. 先讨论s[j - 1] != t[i - 1]， 那么dp[i][j] = dp[i][j-1], 因为最后一个s[j-1]完全没用，不可能再增加数字了

4. 如果s[j - 1] == t[i - 1]， 那么dp[i][j]至少等于dp[i][j-1], 同时还要加上之前可以的dp[i-1][j-1]数量

这个严格说来应该是从花花或者guandyang的矩阵中推导出来比较有说服力，文字感觉还是差了一点
--------------------- 
作者：负雪明烛 
来源：CSDN 
原文：https://blog.csdn.net/fuxuemingzhu/article/details/84228383
http://www.cnblogs.com/grandyang/p/4294105.html   可以看一下grandyang推导的矩阵，这个估计考试的时候可以用
Ø r a b b b i t
Ø 1 1 1 1 1 1 1 1
r 0 1 1 1 1 1 1 1
a 0 0 1 1 1 1 1 1
b 0 0 0 1 2 3 3 3
b 0 0 0 0 1 3 3 3
i 0 0 0 0 0 0 3 3
t 0 0 0 0 0 0 0 3 

Time: O(n^2)
Space: O(n^2)
"""


class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        M, N = len(s), len(t)
        dp = [[0] * (M + 1) for _ in range(N + 1)]
        for j in range(M + 1):
            dp[0][j] = 1
        for i in range(1, N + 1):
            for j in range(1, M + 1):
                if s[j - 1] == t[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
        return dp[-1][-1]
    
    
    
    
    
    
    
    
    
    
    
    
    
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
这个题一看就是DP。向字符串序列问题确实有很多都是用DP求解的。

设dp数组dp[i][j]表示S的前j个字符是T的前i个字符的子序列的个数为dp[i][j]。

那么有dp[0][*] == 1，因为这个情况下，只能使用s的空字符串进行匹配t。

如果s[j - 1] == t[i - 1]，那么，dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]，原因是t的前j个字符可以由s的前[i - 1]个字符
和t的前[j - 1]个匹配的同时最后一个字符匹配，加上s的前[j - 1]个字符和t的前[i]个字符匹配同时丢弃s的第[j]个字符。

如果s[j - 1] != t[i - 1]，那么dp[i][j] = dp[i][j - 1]，因为只能是前面的匹配，最后一个字符不能匹配，所以丢弃了.
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
    
    
    
    
    
    
    
    
    
    
    
    
    
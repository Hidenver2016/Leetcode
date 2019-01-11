# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 10:28:41 2019

@author: hjiang
"""

"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
http://bangbingsyb.blogspot.com/2014/11/leetcode-wildcard-matching.html

此题和10题 regular expression matching非常类似建议一起复习
"""

# dp
# Time:  O(m * n)
# Space: O(m * n)
class Solution(object):
    # @return a boolean
    def isMatch(self, s, p):
        dp = [[False for j in range(len(p) + 1)] for i in range(len(s) + 1)]

        dp[0][0] = True
        for i in range(1, len(p) + 1):
            if p[i-1] == '*':
                dp[0][i] = dp[0][i-1] #匹配0个字符
        for i in range(1,len(s) + 1):
#            dp[i][0] = False
            for j in range(1, len(p) + 1):
                if p[j-1] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i-1][j] or dp[i-1][j-1]#匹配0个1个或者多个字符
                else:
                    dp[i][j] = dp[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '?')#匹配一个字符

        return dp[-1][-1]
    
if __name__ == "__main__":
    print(Solution().isMatch("aa","*"))
    
    
    
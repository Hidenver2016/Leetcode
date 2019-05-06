# -*- coding: utf-8 -*-
"""
Created on Wed May  1 14:53:34 2019

@author: hjiang
"""

"""
There is a strange printer with the following two special requirements:

The printer can only print a sequence of the same character each time.
At each turn, the printer can print new characters starting from and ending at any places, 
and will cover the original existing characters.
Given a string consists of lower English letters only, your job is to count the minimum number 
of turns the printer needed in order to print it.

Example 1:
Input: "aaabbb"
Output: 2
Explanation: Print "aaa" first and then print "bbb".
Example 2:
Input: "aba"
Output: 2
Explanation: Print "aaa" first and then print "b" from the second place of the string, 
which will cover the existing character 'a'.
Hint: Length of the given string will not exceed 100.
https://leetcode.com/problems/strange-printer/discuss/106795/Python-Straightforward-DP-with-Explanation
https://zxi.mytechroad.com/blog/dynamic-programming/leetcode-664-strange-printer/
https://www.cnblogs.com/grandyang/p/8319913.html
http://bookshadow.com/weblog/2017/08/21/leetcode-strange-printer/

自顶向下的递归dp,和741一样

用dp(i,j)表示对于s[i,j+1]需要多少次
如果先开始考虑s[i,k], 如果s[i] == s[k], 那么s[i, k-1]的次数也一样，因为s[i] == s[k],之前可以一次打出所有s[i]
所以，我们接下来只需要完成s[k+1, j]就可以了。那么，dp(i,j) = min(dp(i,j), dp(i, k-1) + dp(k+1, j))而且，
dp(i,j) = 1 + dp(i+1, j) 

741 546，664，488
"""

class Solution:
    def strangePrinter(self, S):#这种方法比自下向上的少了很多状态，应该会快很多
        memo = {}
        def dp(i, j):
            if i > j: return 0
            if (i, j) not in memo:
                ans = dp(i+1, j) + 1
                for k in range(i+1, j+1):
                    if S[k] == S[i]:
                        ans = min(ans, dp(i, k-1) + dp(k+1, j))
                memo[i, j] = ans
            return memo[i, j]
    
        return dp(0, len(S) - 1)


class Solution2:
    def strangePrinter(self, S):
        n = len(S)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n - 1, -1, -1):#因为是和后面的i+1相关，所以这里反着来
            for j in range(i, n):
                dp[i][j] = (1 if i == j else 1 + dp[i+1][j])
                for k in range(i + 1, j + 1):
                    if S[k] == S[i]:
                        dp[i][j] = min(dp[i][j], dp[i + 1][k - 1] + dp[k][j])
        return 0 if n == 0 else dp[0][n-1]

if __name__ == "__main__":
    S = "aaabbb"
    print(Solution().strangePrinter(S))
    print(Solution2().strangePrinter(S))
        
        
        
        
        
        
        
        
        
        
        
        
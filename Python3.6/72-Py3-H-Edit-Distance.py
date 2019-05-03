# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 17:25:36 2019

@author: hjiang
"""

"""
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
http://www.cnblogs.com/grandyang/p/4344107.html
其中dp[i][j]表示从word1的前i个字符转换到word2的前j个字符所需要的步骤。
"""
## Time:  O(n * m)
## Space: O(n * m)
#class Solution(object):
#    # @return an integer
#    def minDistance(self, word1, word2):
#        distance = [[i] for i in range(len(word1) + 1)]
#        distance[0] = [j for j in range(len(word2) + 1)]
#
#        for i in range(1, len(word1) + 1):
#            for j in range(1, len(word2) + 1):
#                insert = distance[i][j - 1] + 1
#                delete = distance[i - 1][j] + 1
#                replace = distance[i - 1][j - 1]
#                if word1[i - 1] != word2[j - 1]:
#                    replace += 1
#                distance[i].append(min(insert, delete, replace))
#
#        return distance[-1][-1]

"""
https://www.cnblogs.com/zuoyuan/p/3773134.html
https://blog.csdn.net/yangjingjing9/article/details/76724291

dp[i][j]表示word1[0...i-1]到word2[0...j-1]的编辑距离。而dp[i][0]显然等于i，因为只需要做i次删除操作就可以了。
同理dp[0][i]也是如此，等于i，因为只需做i次插入操作就可以了。dp[i-1][j]变到dp[i][j]需要加1，
因为word1[0...i-2]到word2[0...j-1]的距离是dp[i-1][j]，而word1[0...i-1]到word1[0...i-2]需要执行一次删除，
所以dp[i][j]=dp[i-1][j]+1；同理dp[i][j]=dp[i][j-1]+1，因为还需要加一次word2的插入操作。
如果word[i-1]==word[j-1]，则dp[i][j]=dp[i-1][j-1]，如果word[i-1]!=word[j-1]，
那么需要执行一次替换replace操作，所以dp[i][j]=dp[i-1][j-1]+1，以上就是状态转移方程的推导。

比如“abc”变成“aba”只需要用"a"将最后一个字符"c"替换掉就可以。此时distance = 1
如word1[i] == word2[j],只需把word1[0至i-1]变为word2[0至j-1]。此时res[i][j] = res[i-1][j-1]

leetcode 712
"""
    
# Time: O(n*m)
# Space: O(n*m)        
    
class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        m=len(word1)+1; n=len(word2)+1
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(n):
            dp[0][i]=i
        for i in range(m):
            dp[i][0]=i
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+(0 if word1[i-1]==word2[j-1] else 1))
        return dp[m-1][n-1]
    
    
    
    
    
    
    
    
    
    
    
    
    
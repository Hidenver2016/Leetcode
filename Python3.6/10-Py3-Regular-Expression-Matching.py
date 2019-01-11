# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 15:55:49 2018

@author: hjiang
"""

#Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
#
#'.' Matches any single character.
#'*' Matches zero or more of the preceding element.
#The matching should cover the entire input string (not partial).
#
#Note:
#
#s could be empty and contains only lowercase letters a-z.
#p could be empty and contains only lowercase letters a-z, and characters like . or *.
#Example 1:
#
#Input:
#s = "aa"
#p = "a"
#Output: false
#Explanation: "a" does not match the entire string "aa".
#Example 2:
#
#Input:
#s = "aa"
#p = "a*"
#Output: true
#Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
#Example 3:
#
#Input:
#s = "ab"
#p = ".*"
#Output: true
#Explanation: ".*" means "zero or more (*) of any character (.)".
#Example 4:
#
#Input:
#s = "aab"
#p = "c*a*b"
#Output: true
#Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".
#Example 5:
#
#Input:
#s = "mississippi"
#p = "mis*is*p*."
#Output: false

# dp
# Time:  O(m * n)
# Space: O(m * n)
"""
https://leetcode.com/problems/regular-expression-matching/discuss/5684/9-lines-16ms-c-dp-solutions-with-explanations
We define the state dp[i][j] to be true if s[0..i) matches p[0..j) and false otherwise. Then the state equations are:


dp[i][j] = dp[i][j - 2], if p[j - 1] == '*' and the pattern repeats for 0 times;
而关键的难点在于 p[j-1] = '*'。由于星号可以匹配0，1，乃至多个p[j-2]。
1. 匹配0个元素，即消去p[j-2]，此时p[0: j-1] = p[0: j-3]
dp[i][j] = dp[i][j-2]


dp[i][j] = dp[i - 1][j - 1], if p[j - 1] != '*' && (s[i - 1] == p[j - 1] || p[j - 1] == '.');



dp[i][j] = dp[i - 1][j] && (s[i - 1] == p[j - 2] || p[j - 2] == '.'), if p[j - 1] == '*' and the pattern repeats for at least 1 times.
"""

# dp
# Time:  O(m * n)
# Space: O(m * n)    
    
#http://www.voidcn.com/article/p-zioiffqq-mm.html
#http://bangbingsyb.blogspot.com/2014/11/leetcode-regular-expression-matching.html        
class Solution(object):
    def isMatch(self, s, p):
        """ :type s: str :type p: str :rtype: bool """
        dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        dp[0][0] = True
        for j in range(2,len(p) + 1):#第一行的边界条件， 匹配0个元素，即消去p[j-2]，此时p[0: j-1] = p[0: j-3]
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]  
        for i in range(1,len(s) + 1):
            for j in range(1,len(p) + 1):
                if p[j - 1] == '*': # 匹配一个，0个，和多个元素，三种情况都用or相连 (多个元素的话要考虑前一个是否相符，才可以往前推，推s)
                    dp[i][j] = dp[i][j-1] or dp[i][j-2] or (dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == '.'))
                elif p[j-1] == '.' or s[i-1] == p[j - 1]:
                    dp[i][j] = dp[i-1][j-1]

        return dp[-1][-1]
        

#递归，这个容易lte
"""
先来看递归的解法：

如果P[j+1]!='*'，S[i] == P[j]=>匹配下一位(i+1, j+1)，S[i]!=P[j]=>匹配失败；

如果P[j+1]=='*'，S[i]==P[j]=>匹配下一位(i+1, j+2)或者(i, j+2)，S[i]!=P[j]=>匹配下一位(i,j+2)。

匹配成功的条件为S[i]=='\0' && P[j]=='\0'。
"""
class Solution1:
    # @return a boolean
    def isMatch(self, s, p):
        if len(p)==0: return len(s)==0
        if len(p)==1 or p[1]!='*':
            if len(s)==0 or (s[0]!=p[0] and p[0]!='.'):
                return False
            return self.isMatch(s[1:],p[1:])
        else:# len(p)!=1, or p[1] =="*"
            i=-1; length=len(s)
            while i<length and (i<0 or p[0]=='.' or p[0]==s[i]):
                if self.isMatch(s[i+1:],p[2:]): return True
                i+=1
            return False

if __name__ == "__main__":
    print (Solution().isMatch("aaaa", "a*"))
#    print Solution().isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c")
#    print Solution().isMatch("aa","a")
#    print Solution().isMatch("aa","aa")
#    print Solution().isMatch("aaa","aa")
#    print Solution().isMatch("aa", "a*")
#    print Solution().isMatch("aa", ".*")
#    print Solution().isMatch("ab", ".*")
#    print Solution().isMatch("aab", "c*a*b")











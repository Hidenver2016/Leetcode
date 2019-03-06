# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 23:19:26 2019

@author: hjiang
"""

"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
"""
#https://leetcode.com/problems/longest-valid-parentheses/discuss/14312/My-ten-lines-python-solution
#https://leetcode.com/problems/longest-valid-parentheses/discuss/123926/Best-Python-Solution-(Beats-100)
"""
let dp[i] is the number of longest valid Parentheses ended with the i - 1 position of s, then we have the following relationship:
dp[i + 1] = dp[p] + i - p + 1 where p is the position of '(' which can matches current ')' in the stack.
"""
class Solution:#这个难理解，算了
    def longestValidParentheses(self, s):
        dp, stack = [0]*(len(s) + 1), []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    p = stack.pop()
                    dp[i + 1] = dp[p] + i - p + 1
        return max(dp)
    
#http://www.cnblogs.com/grandyang/p/4424731.html
class Solution1:#这个容易理解一点，时间空间都是n
    def longestValidParentheses(self, s):
        res = 0; start = 0
        stack = []
        for i in range(len(s)):
            if s[i] == "(": stack.append(i)
            elif s[i] == ")":
                if len(stack) == 0: start = i + 1#前面已无配对，需要右移
                else:
                    stack.pop()
                    if len(stack) == 0: 
                        res = max(res, i - start + 1)
                    else:
                        res = max(res, i - stack[-1])
        return res
    
if __name__ == "__main__":
    print(Solution1().longestValidParentheses(")()())"))
                    
                    
                
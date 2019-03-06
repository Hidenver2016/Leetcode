# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 23:18:14 2019

@author: hjiang
"""

"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""
#https://blog.csdn.net/fuxuemingzhu/article/details/79362373
# Time:  O(4^n / n^(3/2)) ~= Catalan numbers
# Space: O(n)

#核心 那什么时候添加右括号呢？当左括号个数大于右括号的个数时添加右括号。
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.dfs(res, n, n, '')
        return res
        
    def dfs(self, res, left, right, path):
        if left == 0 and right == 0:
            res.append(path)
            return
        if left > 0:
            self.dfs(res, left - 1, right, path + '(')
        if left < right:
            self.dfs(res, left, right - 1, path + ')')

# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 23:21:12 2019

@author: hjiang
"""

"""
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]
# Time:  O(C(n, c)), try out all possible substrings with the minimum c deletion.
# Space: O(c), the depth is at most c, and it costs n at each depth
"""

#https://leetcode.com/problems/remove-invalid-parentheses/discuss/75028/Short-Python-BFS
#http://www.cnblogs.com/grandyang/p/4944875.html
class Solution:
    def removeInvalidParentheses(self, s):
        def isvalid(s):
            ctr = 0
            for c in s:
                if c == '(':
                    ctr += 1
                elif c == ')':
                    ctr -= 1
                    if ctr < 0:
                        return False
            return ctr == 0
        level = {s}
        while True:
            valid = filter(isvalid, level)
            valid = list(valid)#python3 需要加上这一行
            if valid: #可以就返回，那么肯定是删掉最少的括号
                return valid# 两个循环在一行的，前面的是大循环，后面的是小循环
            level = {s[:i] + s[i+1:] for s in level for i in range(len(s))}#用这个方法level这个就没有关系。
#            for s in level:  #如果用这个操作的话，level本身会改变，循环就会报错，需要多加一个临时变量
#                for i in range(len(s)):
#                    level.add(s[:i] + s[i+1:])#一定要注意，对于上面那种一行的是add
if __name__ == "__main__":
    print(Solution().removeInvalidParentheses("()())()"))
            
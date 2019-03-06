# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 15:21:10 2018

@author: hjiang
"""

#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
#determine if the input string is valid.
#
#An input string is valid if:
#
#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
#Note that an empty string is also considered valid.
#
#Example 1:
#
#Input: "()"
#Output: true
#Example 2:
#
#Input: "()[]{}"
#Output: true
#Example 3:
#
#Input: "(]"
#Output: false
#Example 4:
#
#Input: "([)]"
#Output: false
#Example 5:
#
#Input: "{[]}"
#Output: true

# Time:  O(n)
# Space: O(n)


class Solution:
    # @return a boolean
    def isValid(self, s):
        stack, lookup = [], {"(": ")", "{": "}", "[": "]"}
        for p in s:
            if p in lookup:
                stack.append(p)#注意，遇到第二个条件，表示遇到了各种右括号，此时弹出stack最右element,其lookup值必须要等于p
            elif len(stack) == 0 or lookup[stack.pop()] != p:
                return False
        return len(stack) == 0#如果此时不是一个零，那么表示最后估计还剩一个左括号，可能是开头，也可能是结尾
    
if __name__ == "__main__":
#    print (Solution().isValid("()[]{}"))
    print (Solution().isValid("[()]"))
    
    
    
    
    
    
    
    
    
    
    
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 16:07:44 2019

@author: hjiang
"""

"""
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . 
The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.

用num保存上一个数字，用pre_op保存上一个操作符。当遇到新的操作符的时候，需要根据pre_op进行操作。乘除的优先级高于加减。所以有以下规则：

之前的运算符是+，那么需要把之前的数字num进栈，然后等待下一个操作数的到来。 
之前的运算符是-，那么需要把之前的数字求反-num进栈，然后等待下一个操作数的到来。 
之前的运算符是×，那么需要立刻出栈和之前的数字相乘，重新进栈，然后等待下一个操作数的到来。 
之前的运算符是/，那么需要立刻出栈和之前的数字相除，重新进栈，然后等待下一个操作数的到来。

注意比较的都是之前的操作符和操作数，现在遇到的操作符是没有什么用的。

原文：https://blog.csdn.net/fuxuemingzhu/article/details/80826333 

"""

class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        pre_op = '+'
        num = 0
        for i, each in enumerate(s):
            if each.isdigit():
                num = 10 * num + int(each)
            if i == len(s) - 1 or each in '+-*/':
                if pre_op == '+':
                    stack.append(num)
                elif pre_op == '-':
                    stack.append(-num)
                elif pre_op == '*':
                    stack.append(stack.pop() * num)
                elif pre_op == '/':
                    top = stack.pop()
#                    stack.append(int(stack.pop() / num))
                    if top < 0:#if l*r < 0 and l % r != 0 leetcode 150 关于这个除号. 如果是异号应该是top//num + 1，int(top/num)更好
                        stack.append(int(top / num))
                    else:
                        stack.append(top // num)
                pre_op = each
                num = 0
        return sum(stack)
    
if __name__ == "__main__":
    s = "14-3/2"
    print (Solution().calculate(s))


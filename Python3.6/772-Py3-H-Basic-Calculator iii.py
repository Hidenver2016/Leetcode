# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 15:44:30 2018

@author: hjiang
"""

# Time:  O(n)
# Space: O(n)

# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string may contain open ( and closing parentheses ),
# the plus + or minus sign -, non-negative integers and empty spaces .
#
# The expression string contains only non-negative integers, +, -, *, /
# operators ,
# open ( and closing parentheses ) and empty spaces .
# The integer division should truncate toward zero.
#
# You may assume that the given expression is always valid.
#
# Some examples:
#
# "1 + 1" = 2
# " 6-4 / 2 " = 4
# "2*(5+5*2)/3+(6/2+8)" = 21
# "(2+6* 3+5- (3*14/7+2)*5)+3"=-12
#



            
class Solution:#此题与227基本一样，注意遇到括号直接开始新的stack即可
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s + "$"
        def helper(stack, i):
            num = 0
            sign = '+'
            while i < len(s):
                c = s[i]
                if c == " ":
                    i += 1
                    continue
                if c.isdigit():
                    num = 10 * num + int(c)
                    i += 1
                elif c == '(':
                    num, i = helper([], i+1)#遇到括号直接开始新的stack即可
                else:#遇到运算符号了
                    if sign == '+':
                        stack.append(num)
                    if sign == '-':
                        stack.append(-num)
                    if sign == '*':
                        stack.append(stack.pop() * num)
                    if sign == '/':
                        stack.append(int(stack.pop() / num))
                    num = 0
                    i += 1
                    if c == ')':
                        return sum(stack), i
                    sign = c 
            return sum(stack)
        return helper([], 0)


if __name__ == "__main__":
    print (Solution().calculate("2*(5+5*2)/3+(6/2+8)"))
    print (Solution().calculate("(2+6* 3+5- (3*14/7+2)*5)+3"))

    s = "14-3/2"
    print (Solution().calculate(s))
    
    
#class Solution(object):
#    def calculate(self, s):
#        """
#        :type s: str
#        :rtype: int
#        """
#        operands, operators = [], []# treat as stacks
#        operand = ""
#        for i in reversed(range(len(s))):
#            if s[i].isdigit():
#                operand += s[i]
#                if i == 0 or not s[i-1].isdigit():
#                    operands.append(int(operand[::-1])) # 把int14从"41"再还原成 int14
#                    operand = ""
#            elif s[i] == ')' or s[i] == '*' or s[i] == '/': #优先级高的先存起来
#                operators.append(s[i])
#            elif s[i] == '+' or s[i] == '-': # 当前是加减，而之前有乘除，乘除要先行计算
#                while operators and (operators[-1] == '*' or operators[-1] == '/'):
#                    self.compute(operands, operators) #这里才是真正的计算
#                operators.append(s[i])
#            elif s[i] == '(':
#                while operators[-1] != ')':
#                    self.compute(operands, operators) # 真正的计算
#                operators.pop()
#
#        while operators:
#            self.compute(operands, operators)
#
#        return operands[-1]
#
#    def compute(self, operands, operators):
#        left, right = operands.pop(), operands.pop()
#        op = operators.pop()
#        if op == '+':
#            operands.append(left + right)
#        elif op == '-':
#            operands.append(left - right)
#        elif op == '*':
#            operands.append(left * right)
#        elif op == '/':
#            operands.append(left / right)























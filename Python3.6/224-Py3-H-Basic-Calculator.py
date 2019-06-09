# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 14:19:55 2018

@author: hjiang
"""

#Implement a basic calculator to evaluate a simple expression string.
#
#The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, 
#non-negative integers and empty spaces .
#
#Example 1:
#
#Input: "1 + 1"
#Output: 2
#Example 2:
#
#Input: " 2-1 + 2 "
#Output: 3
#Example 3:
#
#Input: "(1+(4+5+2)-3)+(6+8)"
#Output: 23



#class solution1(object):
#    def calculate(self, s):
#        operands, operators = [], [] # operands 是数字， operator是符号
#        operand = "" # 临时寄存
#        for i in reversed(range(len(s))):
#            if s[i].isdigit():
#                operand += s[i]
#                if i == 0 or not s[i-1].isdigit():
#                    operands.append(int(operand[::-1])) #[::-1] reverse
#                    operand = ""
#            elif s[i] == ")" or s[i] == "+" or s[i] == "-":
#                operators.append(s[i])
#            elif s[i] == "(":
#                while operators[-1] != ")":
#                    self.compute(operands, operators)
#                operators.pop()
#                    
#        while operators:
#            self.compute(operands,operators)
#            
#        return operands[-1]
#    
#    def compute(self, operands, operators):
#        left, right = operands.pop(), operands.pop()
#        op = operators.pop()
#        if op == "+":
#            operands.append(left + right)
#        elif op == "-":
#            operands.append(left - right)


"""
这个题没有乘除法，也就少了计算优先级的判断了。众所周知，实现计算器需要使用一个栈，来保存之前的结果，把后面的结果计算出来之后，和栈里的数字进行操作。

使用了res表示不包括栈里数字在内的结果，num表示当前操作的数字，sign表示运算符的正负，用栈保存遇到括号时前面计算好了的结果和运算符。

操作的步骤是：

如果当前是数字，那么更新计算当前数字；
如果当前是操作符+或者-，那么需要更新计算当前计算的结果res，并把当前数字num设为0，sign设为正负，重新开始；
如果当前是(，那么说明后面的小括号里的内容需要优先计算，所以要把res，sign进栈，更新res和sign为新的开始；
如果当前是)，那么说明当前括号里的内容已经计算完毕，所以要把之前的结果出栈，然后计算整个式子的结果；
最后，当所有数字结束的时候，需要把结果进行计算，确保结果是正确的。
https://blog.csdn.net/fuxuemingzhu/article/details/84133441
"""
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, num, sign = 0, 0, 1
        stack = []
        for c in s:
            if c.isdigit():
                num = 10 * num + int(c)
            elif c == "+" or c == "-":#这里需要理解是，每次计算的都是当前的前一步的值
                res = res + sign * num
                num = 0# num是当前值，每次计算之后都要归零，好取下一个
                sign = 1 if c == "+" else -1
            elif c == "(":#有括号，先存入stack，再重新开始
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ")":#此时出栈
                res = res + sign * num
                num = 0 # num是当前值，每次计算之后都要归零，好取下一个
                res *= stack.pop()#这里是乘上括号之前是加号或者减号，这个就是考虑到了取掉括号之后有可能要变号（括号前面是减号）
                res += stack.pop()#这里是括号内的结果加上之前计算的结果
        res = res + sign * num
        return res
    

            


        
if __name__ == "__main__":
    s = "2-1+(3-2)"
    s1 = "1+1"
    print (Solution().calculate(s))
#    print (Solution().calculate(s1))         
        
        
        
        
        
        
        
        
        
        
        
        
        
        
   














     
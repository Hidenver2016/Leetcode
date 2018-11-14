# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 18:39:00 2018

@author: hjiang
"""


"""
Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Example 1:

Input: num = "123", target = 6
Output: ["1+2+3", "1*2*3"] 
Example 2:

Input: num = "232", target = 8
Output: ["2*3+2", "2+3*2"]
Example 3:

Input: num = "105", target = 5
Output: ["1*0+5","10-5"]
Example 4:

Input: num = "00", target = 0
Output: ["0+0", "0-0", "0*0"]
Example 5:

Input: num = "3456237490", target = 9191
Output: []
"""

"""
此题用动态规划要考虑空间的问题，因为动态规划是需要存储一部分过程的
所以用dfs, 虽然计算时间长，但是保证不会爆

val = val * 10 + ord(num[i]) - ord('0') # val和val_str有两遍，第一遍是考虑从头开始的多个数字，第二遍是考虑从中间开始的多个数字
val_str += num[i]


"""


# Time:  O(4^n)
# Space: O(n)

class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        result, expr = [], []
        val, i = 0, 0
        val_str = ""
        while i < len(num):
            val = val * 10 + ord(num[i]) - ord('0') # val和val_str 操作从头开始的数字，包括从头开始多个数字合并的情况
            val_str += num[i]
            # Avoid "00...".
            if str(val) != val_str: # 因为00只会出现在从第一位开始的数字
                break
            expr.append(val_str)
            self.addOperatorsDFS(num, target, i + 1, 0, val, expr, result) 
            expr.pop()
            i += 1 # 对原始的数据循环
        return result

    def addOperatorsDFS(self, num, target, pos, operand1, operand2, expr, result):
        if pos == len(num) and operand1 + operand2 == target:
            result.append("".join(expr))
        else:
            val, i = 0, pos
            val_str = ""
            while i < len(num):
                val = val * 10 + ord(num[i]) - ord('0') # val和val_str操作从中间合并的数字
                val_str += num[i]
                # Avoid "00...".
                if str(val) != val_str:
                    break

                # Case '+':
                expr.append("+" + val_str)
                self.addOperatorsDFS(num, target, i + 1, operand1 + operand2, val, expr, result)
                expr.pop()

                # Case '-':
                expr.append("-" + val_str)
                self.addOperatorsDFS(num, target, i + 1, operand1 + operand2, -val, expr, result)
                expr.pop()

                # Case '*':
                expr.append("*" + val_str)
                self.addOperatorsDFS(num, target, i + 1, operand1, operand2 * val, expr, result)
                expr.pop()

                i += 1


if __name__ == "__main__":
    print (Solution().addOperators('105',5))
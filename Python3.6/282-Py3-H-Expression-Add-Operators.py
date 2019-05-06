# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 18:39:00 2018

@author: hjiang
"""


"""
Given a string that contains only digits 0-9 and a target value, 
return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

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

#class Solution(object):
#    def addOperators(self, num, target):
#        """
#        :type num: str
#        :type target: int
#        :rtype: List[str]
#        """
#        result, expr = [], []
#        val, i = 0, 0
#        val_str = ""
#        while i < len(num):
#            val = val * 10 + ord(num[i]) - ord('0') # val和val_str 操作从头开始的数字，包括从头开始多个数字合并的情况
#            val_str += num[i]
#            # Avoid "00...".
#            if str(val) != val_str: # 因为00只会出现在从第一位开始的数字
#                break
#            expr.append(val_str)
#            self.addOperatorsDFS(num, target, i + 1, 0, val, expr, result) 
#            expr.pop()
#            i += 1 # 对原始的数据循环
#        return result
#
#    def addOperatorsDFS(self, num, target, pos, operand1, operand2, expr, result):
#        if pos == len(num) and operand1 + operand2 == target:
#            result.append("".join(expr))
#        else:
#            val, i = 0, pos
#            val_str = ""
#            while i < len(num):
#                val = val * 10 + ord(num[i]) - ord('0') # val和val_str操作从中间合并的数字
#                val_str += num[i]
#                # Avoid "00...".
#                if str(val) != val_str:
#                    break
#
#                # Case '+':
#                expr.append("+" + val_str)
#                self.addOperatorsDFS(num, target, i + 1, operand1 + operand2, val, expr, result)
#                expr.pop()
#
#                # Case '-':
#                expr.append("-" + val_str)
#                self.addOperatorsDFS(num, target, i + 1, operand1 + operand2, -val, expr, result)
#                expr.pop()
#
#                # Case '*':
#                expr.append("*" + val_str)
#                self.addOperatorsDFS(num, target, i + 1, operand1, operand2 * val, expr, result)
#                expr.pop()
#
#                i += 1

#https://leetcode.com/problems/expression-add-operators/discuss/71968/Clean-Python-DFS-with-comments
"""
dfs() parameters:
num: remaining num string
temp: temporally string with operators added
cur: current result of "temp" string
last: last multiply-level number in "temp". if next operator is "multiply", "cur" and "last" will be updated
res: result to return
http://www.cnblogs.com/grandyang/p/4814506.html
而对于乘来说稍有些复杂，此时的diff应该是上一次的变化的diff乘以即将要乘上的数，有点不好理解，那我们来举个例子，
比如2+3*2，即将要运算到乘以2的时候，上次循环的curNum = 5, diff = 3, 而如果我们要算这个乘2的时候，
新的变化值diff应为3*2=6，而我们要把之前+3操作的结果去掉，再加上新的diff，即(5-3)+6=8，即为新表达式2+3*2的值
"""
"""
#https://leetcode.com/problems/expression-add-operators/discuss/128460/simple-Python-DFS-that-beats-100
下面别人的注释，这种方法不是最快的，中间有重复的部分，但是便于理解
"""
class Solution0: #看这个好了
    def addOperators(self, num, target):
        if not num:
            return []
        res = []

        def dfs(index, path, cur, last):
            if cur == target and index == len(num):
                res.append(path)
                return
            for i in range(index, len(num)):
                cur_num = num[index:i+1]
                if len(cur_num) > 1 and cur_num[0] == "0":# prevent "00*" as a number
                    break
                if index == 0:# corner case, no operation before first digit
                    dfs(i+1, cur_num, int(cur_num), int(cur_num))
                else:
                    dfs(i + 1, path + "+" + cur_num, cur + int(cur_num), int(cur_num))
                    dfs(i + 1, path + "-" + cur_num, cur - int(cur_num), -int(cur_num))
                    dfs(i + 1, path + "*" + cur_num, cur - last + last * int(cur_num), last * int(cur_num))

        dfs(0, "", 0, 0)
        return res
                
class Solution1:
    def addOperators(self, num, target):
        res, self.target = [], target
        for i in range(1,len(num)+1):
            if i == 1 or (i > 1 and num[0] != "0"): # prevent "00*" as a number
                self.dfs(num[i:], num[:i], int(num[:i]), int(num[:i]), res) # this step put first number in the string
        return res

    def dfs(self, num, temp, cur, last, res):
        if not num:
            if cur == self.target:
                res.append(temp)
            return
        for i in range(1, len(num)+1):
            val = num[:i]
            if i == 1 or (i > 1 and num[0] != "0"): # prevent "00*" as a number
                self.dfs(num[i:], temp + "+" + val, cur+int(val), int(val), res)
                self.dfs(num[i:], temp + "-" + val, cur-int(val), -int(val), res)
                self.dfs(num[i:], temp + "*" + val, cur-last+last*int(val), last*int(val), res)
                
                
                
class Solution2:
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        # use dfs with curr_total and prev_val, add four expressions in expr. Time O(n*3^n)
        result, expr = [], ''
        curr_total, prev_val = 0, 0
        pos = 0
        self.dfs(num, target, pos, curr_total, prev_val, expr, result)
        return result
    # dfs helper
    def dfs(self, num, target, pos, curr_total, prev_val, expr, result):
        # stop criteria
        if pos == len(num) and curr_total == target:
            result.append(expr)
        else:
            val = 0
            for i in range(pos, len(num)): # use for loop
                val = val * 10 + ord(num[i]) - ord('0')
                if pos == 0: # corner case, no operation before first digit
                    self.dfs(num, target, i+1, curr_total + val, val, expr + str(val), result)
                else:
                    # case '+'
                    self.dfs(num, target, i+1, curr_total + val, val, expr + '+' + str(val), result)
                    # case '-'
                    self.dfs(num, target, i+1, curr_total - val, -val, expr + '-' + str(val), result)
                    # case '*'
                    self.dfs(num, target, i+1, curr_total - prev_val + prev_val * val, prev_val * val, expr + '*' + str(val), result)
                    # can also extend to '/' case
                    if val !=0:
                        self.dfs(num, target, i+1, curr_total - prev_val + prev_val * 1.0 / val, prev_val * 1.0 / val, expr + '/' + str(val), result)
                if num[pos] == '0': # deal with '025' case, string starts with '0'
                    break


if __name__ == "__main__":
    print (Solution3().addOperators('105',5))
    
    
    
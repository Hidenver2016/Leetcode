# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 22:43:26 2019

@author: hjiang
"""

"""
Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, 
each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Example 1:

Input: "112358"
Output: true 
Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
             1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
Example 2:

Input: "199100199"
Output: true 
Explanation: The additive sequence is: 1, 99, 100, 199. 
             1 + 99 = 100, 99 + 100 = 199
Follow up:
How would you handle overflow for very large input integers?


是不是很眼熟呢？和我们刚刚做过的判断是否是有效的IP93. Restore IP Addresses如出一辙：使用回溯法+合理剪枝。

因为只要判断能否构成即可，所以不需要res数组保存结果。回溯法仍然是对剩余的数字进行切片，看该部分切片能否满足条件。
剪枝的方法是判断数组是否长度超过3，如果超过那么判断是否满足费布拉奇数列的规则。不超过3或者已经满足的条件下继续进行回溯切片。
最后当所有的字符串被切片完毕，要判断下数组长度是否大于等于3，这是题目要求。
--------------------- 参看leetcode 93题

原文：https://blog.csdn.net/fuxuemingzhu/article/details/80661715 

"""
class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        return self.dfs(num, [])

    def dfs(self, num_str, path):
        if len(path) >= 3 and  path[-1] != path[-2] + path[-3]:
            return False
        if not num_str and len(path) >= 3:
            return True
        for i in range(len(num_str)):
            curr = num_str[:i+1]
            if (curr[0] == '0' and len(curr) != 1):
                continue
            if self.dfs(num_str[i+1:], path + [int(curr)]):
                return True
        return False


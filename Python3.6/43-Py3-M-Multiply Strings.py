# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 21:00:20 2019

@author: hjiang
"""

"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""

# Time:  O(m * n)
# Space: O(m + n)

class Solution(object):#完全是乘法
    def multiply(self, num1, num2):
        num1, num2 = num1[::-1], num2[::-1]
        res = [0] * (len(num1) + len(num2))
        for i in range(len(num1)):
            for j in range(len(num2)):
                res[i + j] += int(num1[i]) * int(num2[j])
                res[i + j + 1] += res[i + j] // 10#反的，所以是前面一位
                res[i + j] %= 10#自己取余数

        # Skip leading 0s.
        i = len(res) - 1
        while i > 0 and res[i] == 0:
            i -= 1

        return ''.join(map(str, res[i::-1]))

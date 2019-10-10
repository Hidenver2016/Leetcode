# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 21:02:08 2019

@author: hjiang
"""

"""
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit 
signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function 
returns 231 − 1 when the division result overflows.
"""
# Time:  O(logn) = O(1)
# Space: O(1)

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        result, dvd, dvs = 0, abs(dividend), abs(divisor)
        while dvd >= dvs:#看清楚是两重循环
            inc = dvs#赋值
            i = 0# 注意这里
            while dvd >= inc:#logn的速度
                dvd -= inc
                result += 1 << i# 移位的优先级高于加减，先计算1*2**i,再相加
                inc <<= 1
                i += 1
        if dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0:
            return -result
        else:
            return result
        
if __name__ == "__main__":
    print(Solution().divide(10, 2))
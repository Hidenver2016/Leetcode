# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 21:22:29 2019

@author: hjiang
"""

"""
Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10^n.

Example:

Input: 2
Output: 91 
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, 
             excluding 11,22,33,44,55,66,77,88,99
             
https://blog.csdn.net/fuxuemingzhu/article/details/80552049
还是找规律吧：

如果n = 1，那么可以有10个数字不同（0～9）

如果n >= 2，那么第一位可以是1～9共9个数字，第二位可以是出去第一位的数字+0共9个数字，
之后的每位数字都必须不能使用前面已经用过的数字所以依次递减。即9,9,8,7,…,1

n位数字中由不同的数字构成的数字，是比它小的各位数字所能构成的该条件的数字求和。


如果看不明白代码，可以这么理解：题目要求的是0 ≤ x < 10^n的x个数，那么x可以为1位数，2位数……n位数。
当x为1位数的时候有10个结果；
当x为2位数的时候，有99个结果；
当x为3位数的时候，有998个结果……
也就是说当x为n位数的时候，有99*…*(11 - n个结果)，其中n必须小于等于10了（11位数字不可能每一位都不相同）。
最后求和就好。
--------------------- 

原文：https://blog.csdn.net/fuxuemingzhu/article/details/80552049 

"""
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        ans, product = 1, 1
        for i in range(min(n, 10)):
            product *= nums[i]
            ans += product
        return ans
    
if __name__ == "__main__":
    print(Solution().countNumbersWithUniqueDigits(2))


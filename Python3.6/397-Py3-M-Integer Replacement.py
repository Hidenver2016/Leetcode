# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 21:25:44 2019

@author: hjiang
"""

"""
Given a positive integer n and you can do operations as follow:

If n is even, replace n with n/2.
If n is odd, you can replace n with either n + 1 or n - 1.
What is the minimum number of replacements needed for n to become 1?

Example 1:

Input:
8

Output:
3

Explanation:
8 -> 4 -> 2 -> 1
Example 2:

Input:
7

Output:
4

Explanation:
7 -> 8 -> 4 -> 2 -> 1
or
7 -> 6 -> 3 -> 2 -> 1

https://blog.csdn.net/fuxuemingzhu/article/details/79495908
"""

class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 1:
            count += 1
            if n & 1:#奇数
                if n & 2 and n != 3:#尾号是11
                    n += 1
                else:#尾号是01
                    n -= 1
            else:#偶数
                n >>= 1
        return count

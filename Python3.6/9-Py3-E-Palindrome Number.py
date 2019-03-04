# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 15:43:01 2019

@author: hjiang
"""

"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?
https://blog.csdn.net/fuxuemingzhu/article/details/71334663
可以先转化成字符串，然后判断这个字符串是不是回文串。
"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False
        x = str(x)
        N = len(x)
        for i in range(N // 2):
            if x[i] != x[N - 1 - i]:
                return False
        return True
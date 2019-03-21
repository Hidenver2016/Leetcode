# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 22:41:55 2019

@author: hjiang
"""

"""
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:  

1 is typically treated as an ugly number.
n does not exceed 1690.
https://blog.csdn.net/fuxuemingzhu/article/details/49231615
所有的ugly number都是由1开始，乘以2/3/5生成的。

只要将这些生成的数排序即可获得，自动排序可以使用set

这样每次取出的第一个元素就是最小元素，由此再继续生成新的ugly number.

可以分成如下三组：
(1) 1×2, 2×2, 3×2, 4×2, 5×2, …

(2) 1×3, 2×3, 3×3, 4×3, 5×3, …

(3) 1×5, 2×5, 3×5, 4×5, 5×5, …
"""
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            return 0
        dp = [1] * n
        index2, index3, index5 = 0, 0, 0
        for i in range(1, n):#一边计算一边排序，溜溜溜溜！
            dp[i] = min(2 * dp[index2], 3 * dp[index3], 5 * dp[index5])
            if dp[i] == 2 * dp[index2]: index2 += 1
            if dp[i] == 3 * dp[index3]: index3 += 1
            if dp[i] == 5 * dp[index5]: index5 += 1
        return dp[n - 1]

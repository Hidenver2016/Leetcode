# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 22:08:29 2019

@author: hjiang
"""

"""
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
素数筛法就是把这个数的所有倍数都删除掉，因为这些数一定不是素数。最后统计一下数字剩余的没有被删除的个数就好。
https://blog.csdn.net/fuxuemingzhu/article/details/49279897
看一下这个里面的动态图
"""

# Time:  O(n)
# Space: O(n)

class Solution(object):
    # @param {integer} n
    # @return {integer}

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:#如果是质数，那么这个数的倍数肯定不是质数。本来应是从2开始乘，但是2之前已经算过，这个算法可以避免重复计算
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        return sum(primes)


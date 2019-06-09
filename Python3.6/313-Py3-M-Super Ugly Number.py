# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 16:17:24 2019

@author: hjiang
"""

"""
Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k.

Example:

Input: n = 12, primes = [2,7,13,19]
Output: 32 
Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 
             super ugly numbers given primes = [2,7,13,19] of size 4.
Note:

1 is a super ugly number for any given primes.
The given numbers in primes are in ascending order.
0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
The nth super ugly number is guaranteed to fit in a 32-bit signed integer.
"""

# Time:  O(n * k)
# Space: O(n + k)
# TLE due to the last test case, but it passess and performs the best in C++.
from heapq import heappop, heappush
class Solution4(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        uglies = [0] * n
        uglies[0] = 1
        ugly_by_prime = list(primes)
        idx = [0] * len(primes)

        for i in range(1, n):
            uglies[i] = min(ugly_by_prime)
            for k in range(len(primes)):
                if uglies[i] == ugly_by_prime[k]:
                    idx[k] += 1
                    ugly_by_prime[k] = primes[k] * uglies[idx[k]]
    
        return uglies[-1]
    
    
    def nthSuperUglyNumber1(self, n, P):
        res, heap = [1], [(P[i], P[i], 0) for i in range(len(P))]#[(2, 2, 0), (7, 7, 0), (13, 13, 0), (19, 19, 0)]
        while len(res) < n:
            val, prm, idx = heappop(heap)#idx表示这个组合被用了多少次
            if val <= res[-1]:
                while val <= res[-1]: idx += 1; val = prm * res[idx]
            else:
#                res += val,#[1,2] 注意这个逗号，就是res.append(val)
                res.append(val)
                val, idx = prm * res[idx + 1], idx + 1
            heappush(heap, (val, prm, idx))
        return res[-1]
if __name__ == "__main__":
    n = 12
    primes = [2,7,13,19]
    print(Solution4().nthSuperUglyNumber1(n, primes))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
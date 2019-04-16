# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 21:29:51 2019

@author: hjiang
"""

"""
Koko loves to eat bananas.  There are N piles of bananas, the i-th pile has piles[i] bananas.  The guards have gone and will come back in H hours.

Koko can decide her bananas-per-hour eating speed of K.  Each hour, she chooses some pile of bananas, and eats K bananas from that pile.  
If the pile has less than K bananas, she eats all of them instead, and won't eat any more bananas during this hour.

Koko likes to eat slowly, but still wants to finish eating all the bananas before the guards come back.

Return the minimum integer K such that she can eat all the bananas within H hours.

 

Example 1:

Input: piles = [3,6,7,11], H = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], H = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], H = 6
Output: 23
 

Note:

1 <= piles.length <= 10^4
piles.length <= H <= 10^9
1 <= piles[i] <= 10^9
"""
import math
class Solution1:
    def minEatingSpeed(self, piles, H):#把这个作为自己的解法好了
        l, r = 1, max(piles) + 1
        while l < r:
            m = l + (r - l)//2
            if sum(math.ceil(i / m) for i in piles) > H:
                l = m + 1
            else:
                r = m
        return l


import math
class Solution:
    def minEatingSpeed(self, piles, H):
#        piles.sort()
        l, r = min(piles), max(piles)
        while l < r:
            m = l + (r - l)//2
            if sum(math.ceil(i / m) for i in piles) <= H:#注意这里可以等于
                r = m
            else:
                l = m + 1
        return l
        
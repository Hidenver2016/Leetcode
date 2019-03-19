# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 14:28:09 2019

@author: hjiang
"""

"""
There are n bulbs that are initially off. You first turn on all the bulbs. 
Then, you turn off every second bulb. On the third round, you toggle every third bulb 
(turning on if it's off or turning off if it's on). For the i-th round, you toggle every i bulb. 
For the n-th round, you only toggle the last bulb. Find how many bulbs are on after n rounds.

Example:

Input: 3
Output: 1 
Explanation: 
At first, the three bulbs are [off, off, off].
After first round, the three bulbs are [on, on, on].
After second round, the three bulbs are [on, off, on].
After third round, the three bulbs are [on, off, off]. 

So you should return 1, because there is only one bulb is on.
https://blog.csdn.net/baidu_23318869/article/details/50386323
那么问题就简化为了求1到n之间完全平方数的个数，也就是平方根取整
http://www.cnblogs.com/grandyang/p/5100098.html

"""
import math
class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(math.sqrt(n))

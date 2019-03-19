# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 14:30:58 2019

@author: hjiang
"""

"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, 
replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 
(where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers 
for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
http://www.cnblogs.com/grandyang/p/4447233.html
https://leetcode.com/problems/happy-number/
我们可以用set来记录所有出现过的数字，然后每出现一个新数字，在set中查找看是否存在，若不存在则加入表中，
若存在则跳出循环，并且判断此数是否为1，若为1返回true，不为1返回false，代码如下：
"""
class Solution:
    def isHappy(self, n):
        mem = set()
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n in mem:
                return False
            else:
                mem.add(n)
        else:
            return True
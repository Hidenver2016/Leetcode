# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 14:33:31 2019

@author: hjiang
"""

"""
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:

Input:
3

Output:
3
Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12... is a 0, which is part of the number 10.
https://blog.csdn.net/fuxuemingzhu/article/details/84559975
http://www.cnblogs.com/grandyang/p/5891871.html
我们要得到第N位数字，如果直接暴力是超时的。正确的做法是找规律：个位数字有9个，2位数字有9×10=90个，
3位数字有9*100=900个……所以我们先求出n是几位数字，然后判断第n个数字应该落在哪个自然数上，最后再求这个自然数会落在自然数的那一位上。
"""

class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        _len = 1
        cnt = 9
        start = 1
        while n > _len * cnt:
            n -= _len * cnt #前九个数都是1位的，然后10到99总共90个数字都是两位的，100到999这900个数都是三位的
            _len += 1
            cnt *= 10
            start *= 10
        start += (n - 1) // _len
        return int(str(start)[(n - 1) % _len])
    
if __name__ == "__main__":
    print(Solution().findNthDigit(100))


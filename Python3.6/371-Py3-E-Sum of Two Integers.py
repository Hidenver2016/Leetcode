# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 12:16:57 2019

@author: hjiang
"""

"""
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = -2, b = 3
Output: 1

https://blog.csdn.net/fuxuemingzhu/article/details/79379939
其二进制形式为11: 1011, 5: 0101

1. 那么两个位置都为1的地方就需要进位, 所以进位值就为0001. 原位置两个数相加的结果为那个位置值的异或即1110, 
即两个位置值如果不一样就为1, 一样的话要么两个位置原来值都为0结果也为0, 要么进位, 那么结果依然是0. 

2. 接下来就要把进位位和下一位相加, 所以进位值左移一位,即0001变为0010, 重复上面操作可得新的**进位值**为0010, 原位置异或(即相加)结果为1100.

3. 继续重复上面操作直到进位为0, 可得到最终结果10000, 即16


这个题的做法就是用a保存“直接加”（不考虑进位）的结果，用b保存进位；然后使a再与b相加，直至保存进位的b为0.

“直接加”通过XOR实现，进位通过and实现。

注意，不能改
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
#        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
"""
class Solution(object):
    def getSum(self, a, b):# 
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
#        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
 
        while b != 0:
            # ^ get different bits and & gets double 1s, << moves carry
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask# 原来的值直接异或，进位的值左移一位即可
        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        return a if a <= MAX else ~(a ^ mask)

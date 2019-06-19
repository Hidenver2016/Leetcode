# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 12:18:09 2019

@author: hjiang
"""
"""
Given a non negative integer number num. For every numbers i in the range 
0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]
Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). 
But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function 
like __builtin_popcount in c++ or in any other language.


https://blog.csdn.net/fuxuemingzhu/article/details/70806676
把第i个数分成两种情况，
如果i是偶数，那么，它的二进制1的位数等于i//2中1的位数；
如果i是奇数，那么，它的二进制1的位数等于i-1的二进制位数+1，又i-1是偶数，所以奇数i的二进制1的位数等于i/2中二进制1的位数+1.

所以上面的这些可以很简单的表达成answer[i] = answer[i >> 1] + (i & 1)。

Python代码如下：

"""

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0] * (num + 1)
        for i in range(1, num + 1):
            res[i] = res[i // 2] + i % 2
        return res
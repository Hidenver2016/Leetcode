# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 21:17:57 2019

@author: hjiang
"""

"""
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true 
Explanation: 2^0 = 1
Example 2:

Input: 16
Output: true
Explanation: 2^4 = 16
Example 3:

Input: 218
Output: false
http://www.cnblogs.com/grandyang/p/4623394.html
这道题还有一个技巧，如果一个数是2的次方数的话，根据上面分析，那么它的二进数必然是最高位为1，其它都为0，
那么如果此时我们减1的话，则最高位会降一位，其余为0的位现在都为变为1，那么我们把两数相与，就会得到0，
用这个性质也能来解题，而且只需一行代码就可以搞定，如下所示：
"""
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and not (n & n-1)
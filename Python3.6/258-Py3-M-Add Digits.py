# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 11:19:18 2019

@author: hjiang
"""

"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.
Follow up:
Could you do it without any loop/recursion in O(1) runtime?

1    1
2    2
3    3
4    4
5    5
6    6
7    7
8    8    
9    9    
10    1
11    2
12    3    
13    4
14    5
15    6
16    7
17    8
18    9
19    1
20    2

 

根据上面的列举，我们可以得出规律，每9个一循环，所有大于9的数的树根都是对9取余，那么对于等于9的数对9取余就是0了，
为了得到其本身，而且同样也要对大于9的数适用，我们就用(n-1)%9+1这个表达式来包括所有的情况。
还有个特殊情况需要考虑一下，当num为0的时候，那么就会出现 -1 % 9 的情况，这个其实挺烦人的，
因为C++和Java会给出商0余-1的结果，而Python会给出商-1余8的结果，博主搜了一下，好像是说当有一个负数存在的时候，
C++/Java会尽可能让商大一些，而Python会让商小一些，所以结果不统一就神烦，那么只好做个额外判断了，特殊处理一下0的情况就OK了，所以解法如下：
"""

# Time:  O(1)
# Space: O(1)

class Solution(object):
    """
    :type num: int
    :rtype: int
    """
    def addDigits(self, num):
        return (num - 1) % 9 + 1 if num > 0 else 0
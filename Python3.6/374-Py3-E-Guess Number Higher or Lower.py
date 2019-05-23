# -*- coding: utf-8 -*-
"""
Created on Wed May 22 15:23:40 2019

@author: hjiang
"""

"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
Example :

Input: n = 10, pick = 6
Output: 6

做这个题的重点是明白guess()函数，题目说了是我取了一个数字，你去猜这个数字，guess()是我的数字大了还是小了。。明白这个意思了么。

所以这个题是标准的二分查找。
https://blog.csdn.net/fuxuemingzhu/article/details/71516105
"""
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n #[left, right]
        mid = left
        while left <= right:
            mid = (right + left) // 2
            res = guess(mid)
            if res == 0:
                return mid
            elif res == 1:
                left = mid + 1
            else:
                right = mid - 1
        return mid

# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 14:29:36 2019

@author: hjiang
"""

"""
You are playing the following Nim Game with your friend: There is a heap of stones on the table, 
each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. 
You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. Write a function to determine 
whether you can win the game given the number of stones in the heap.

Example:

Input: 4
Output: false 
Explanation: If there are 4 stones in the heap, then you will never win the game;
             No matter 1, 2, or 3 stones you remove, the last stone will always be 
             removed by your friend.
             
题目的意思是只要拿最后一个石子的人赢。

因为每次最多拿三个，所以只要我开始的时候，剩余四个的话，我就输了。

所以，所有子的个数不能被四整除我就赢了，否则我会输。输的原因是对手每次都拿4-n，n为当次我拿到子的个数。
https://blog.csdn.net/fuxuemingzhu/article/details/51284421
"""
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 != 0



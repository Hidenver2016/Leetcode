# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 21:14:55 2019

@author: hjiang
"""

"""
There is a list of sorted integers from 1 to n. Starting from left to right, 
remove the first number and every other number afterward until you reach the end of the list.

Repeat the previous step again, but this time from right to left, 
remove the right most number and every other number from the remaining numbers.

We keep repeating the steps again, alternating left to right and right to left, 
until a single number remains.

Find the last number that remains starting with a list of length n.

Example:

Input:
n = 9,
1 2 3 4 5 6 7 8 9
2 4 6 8
2 6
6

Output:
6
有的时候可以从结果来分析，这个只剩下一个数字，那么删掉的就是n-1,而且reverse的复杂度是n,
总体的复杂度应该是n^2/2的一个级数， n^2/2， (n/2)^2, (n/4)^2, ...

"""
class Solution:#这个解答的时间复杂度要研究一下list切片。slice的复杂度就是slice的长度
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr = range(1, n+1)#python3 中间这个只是一个generator,并不会产生一个超长的数列，memory是constant.pyhon2就会爆了
        while len(arr) > 1:
            arr = arr[1::2][::-1]#注意这个地方的[::-1]说明了是从先从左到右，然后再从右到左。 
        return arr[0]
    
if __name__ == "__main__":
    print(Solution().lastRemaining(9))
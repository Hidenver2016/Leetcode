# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 21:03:39 2019

@author: hjiang
"""

"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
https://blog.csdn.net/fuxuemingzhu/article/details/79254648
"""
#牛顿法的一个迭代序列：x(n+1)=x(n)－f(x(n))/f'(x(n))
# f(x) = x^2 - a
# 代入得 x-(x^2-a)/(2x)，也就是(x+a/x)/2

class Solution(object):#牛顿法，也要记住，尤其是上面的公式
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        num = x + 1
        while num * num > x:
            num = int((num + x / num) / 2)#这里加int是因为题目需要
        return num
    
    
#这个题是二分查找的经典题目了，直接套用二分查找的模板即可。这里贡献一个二分查找的模板，模板中查找的区间是[l, r)，即左闭右开。
def binary_searche(l, r):#这个需要背诵
    while l < r:
        m = l + (r - l) // 2
        if f(m):    # 判断找了没有，optional
            return m
        if g(m):
            r = m   # new range [l, m)
        else:
            l = m + 1 # new range [m+1, r)
    return l    # or not found

class Solution1(object):# 这个是二分查找
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left, right = 0, x + 1
        # [left, right)
        while left < right:
            mid = left + (right - left) // 2
            if mid ** 2 == x:
                return mid
            if mid ** 2 < x:
                left = mid + 1
            else:
                right = mid
        return left - 1
    
if __name__ == "__main__":
    print(Solution().mySqrt(5))

# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 15:50:06 2019

@author: hjiang
"""

"""
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.
http://www.cnblogs.com/grandyang/p/4225047.html
https://leetcode.com/problems/largest-number/discuss/53270/Python-simple-solution-in-4-lines
此题还需要自己再改写一遍
"""
# Time:  O(nlogn)
# Space: O(1)

class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        from functools import cmp_to_key
        comp = lambda a, b: 1 if a + b < b + a else -1 if a + b > b + a else 0
#        return str(int(''.join(sorted([str(x) for x in nums], key=cmp_to_key(comp)))))
        return str(int(''.join(sorted([str(x) for x in nums], key=cmp_to_key(comp)))))
"""
排序（Sort）

排序思路：对于两个备选数字a和b，如果str(a) + str(b) > str(b) + str(a)，则a在b之前，否则b在a之前

按照此原则对原数组从大到小排序即可

时间复杂度O（nlogn）

易错样例：
Input:     [0,0]
Output:    "00"
Expected:  "0"
compare是自定义比较函数，返回值是1或者-1，当a + b > b + a时返回-1，否则返回1。
"""
#http://bookshadow.com/weblog/2015/01/13/leetcode-largest-number/ 
from functools import cmp_to_key
class Solution1:#看这个
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        num = sorted([str(x) for x in num], key = cmp_to_key(self.compare))
        ans = ''.join(num).lstrip('0')#删除左边的"0"
        return ans or '0'

    def compare(self, a, b):
        return [1, -1][a + b > b + a]


if __name__ == "__main__":
    print(Solution1().largestNumber([3,30,34,5,9]))
    
    
    
    
    
    
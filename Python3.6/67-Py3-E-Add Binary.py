# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 20:59:35 2019

@author: hjiang
"""

"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""

class Solution:
    def addBinary(self, a, b):#没有说不可以用0b转化到二进制
        return bin(eval('0b' + a) + eval('0b' + b))[2:]
    
#https://leetcode.com/problems/add-binary/discuss/24500/An-accepted-concise-Python-recursive-solution-10-lines
    
    
#add two binary from back to front, I think it is very self explained, when 1+1 we need a carry.
# Time : O(n)
# Space: O(n)
class Solution1:
    def addBinary(self, a, b):
        if len(a)==0: return b
        if len(b)==0: return a
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[0:-1],b[0:-1]),'1')+'0'#这里就是进位a[0:-1]是从0开始到倒数第二位
        if a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[0:-1],b[0:-1])+'0'
        else:
            return self.addBinary(a[0:-1],b[0:-1])+'1'
        
if __name__ == "__main__":
    print(Solution1().addBinary('1', '1'))

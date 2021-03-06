# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 16:00:43 2019

@author: hjiang
"""

"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. 
Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. 
However, the numeral for four is not IIII. Instead, the number four is written as IV. 
Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. 
There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3
Example 2:

Input: "IV"
Output: 4
Example 3:

Input: "IX"
Output: 9
Example 4:

Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

# Time:  O(n)
# Space: O(1)

class Solution(object):
    # @return an integer
    def romanToInt(self, s):
        numeral_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C":100, "D": 500, "M": 1000}
        decimal = 0
        for i in range(len(s)):
            if i > 0 and numeral_map[s[i]] > numeral_map[s[i - 1]]:
                decimal += numeral_map[s[i]] - 2 * numeral_map[s[i - 1]]# XCIV 是94，看最后两位，按照这个算法就是100+1+5 -2×1，这个I被加了两回，所以需要减去
            else:
                decimal += numeral_map[s[i]]
        return decimal
    


def R2I(str):#自己写的方法比较快，因为基本都是在查表
    dict_R2I = {'I':1, 'V': 5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 
				'IV':4, 'IX':9, 'XL': 40, 'XC':90, 'CD': 400, 'CM':900,
				'II':2, 'III':3, 'XX':20, 'XXX': 30, 'CC':200, 'CCC':300, 'MM':2000, 'MMM':3000,
				'VI':6, 'VII':7, 'VIII':8, 'LX':60, 'LXX':70, 'LXXX':80,
				'DC':600, 'DCC':700, 'DCCC':800}
    res = 0
    i = 0
    while i < len(str):
        for j in range(4, 0, -1):
            if str[i: i+j] in dict_R2I:
                res += dict_R2I[str[i: i+j]]
                i = i+j
                break
				
    return res    

print(R2I('LVIII'))
    
    
    
    
    
    
    
    
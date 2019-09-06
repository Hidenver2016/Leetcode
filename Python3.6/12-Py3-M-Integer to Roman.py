# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 15:59:54 2019

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
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: 3
Output: "III"
Example 2:

Input: 4
Output: "IV"
Example 3:

Input: 9
Output: "IX"
Example 4:

Input: 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
Example 5:

Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
关键，这些4，9之类的也要加入dict
"""

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        numeral_map = {1: "I", 4: "IV", 5: "V", 9: "IX", \
                       10: "X", 40: "XL", 50: "L", 90: "XC", \
                       100: "C", 400: "CD", 500: "D", 900: "CM", \
                       1000: "M"}
        keyset, result = sorted(numeral_map.keys()), []# [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]

        while num > 0:
            for key in reversed(keyset):
                while num >= key:# num//key >0 也可以
                    num -= key
                    result += numeral_map[key]

        return "".join(result)
    
    def intToRoman1(self, str1):#自己写的，带上循环都比上面的快，充分证明这种题目就是大力出奇迹
        dict_R2I = {'I':1, 'V': 5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 
    				'IV':4, 'IX':9, 'XL': 40, 'XC':90, 'CD': 400, 'CM':900,
    				'II':2, 'III':3, 'XX':20, 'XXX': 30, 'CC':200, 'CCC':300, 'MM':2000, 'MMM':3000,
    				'VI':6, 'VII':7, 'VIII':8, 'LX':60, 'LXX':70, 'LXXX':80,
    				'DC':600, 'DCC':700, 'DCCC':800}
        dict_I2R = {}
        for key, item  in dict_R2I.items():
            dict_I2R[str(item)] = key
    	
        res = []
        temp1 = str(str1)
        n = len(temp1)
        for i in range(n-1, -1, -1):
            temp = int(temp1[i])*10**((n-1) - i)
            if temp == 0: continue
            res.append(dict_I2R[str(temp)])
        return "".join(res[::-1])
    
if __name__ == "__main__":
    print(Solution().intToRoman1(25))
    
    
    
    
    
    
    
    
    
    
    
    
    
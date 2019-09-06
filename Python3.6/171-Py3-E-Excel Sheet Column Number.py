# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 15:58:43 2019

@author: hjiang
"""

"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701
"""
# Time:  O(n)
# Space: O(1)

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for i in range(len(s)):
            result *= 26#这个写的顺序就是说要注意那种只有一个字母的情况
            result += ord(s[i]) - ord('A') + 1
        return result


def titleToNumber(str):#自己写的
    n = len(str)
    res = 0
	# if n == 1:
		# res = Ord(str) - Ord('A') + 1
    i = 0
    while i < n:
        res +=  (ord(str[i]) - ord('A') + 1)*26**(n - i - 1)
        i += 1
    return res

        
print(titleToNumber("AB"))



# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 00:51:16 2020

@author: hjiang
"""

"""
Given two strings str1 and str2 of the same length, 
determine whether you can transform str1 into str2 by doing zero or more conversions.

In one conversion you can convert all occurrences of one character in str1 to any other lowercase English character.

Return true if and only if you can transform str1 into str2.

 

Example 1:

Input: str1 = "aabcc", str2 = "ccdee"
Output: true
Explanation: Convert 'c' to 'e' then 'b' to 'd' then 'a' to 'c'. Note that the order of conversions matter.
Example 2:

Input: str1 = "leetcode", str2 = "codeleet"
Output: false
Explanation: There is no way to transform str1 to str2.
 

Note:

1 <= str1.length == str2.length <= 10^4
Both str1 and str2 contain only lowercase English letters.

这个题的意思就是要找一个从str1 的每一个字母到str2的唯一映射，如果与之前的映射冲突，那么证明不可以
"""

class Solution:
    def canConvert(self, str1, str2):
        if str1 == str2:
            return True
        m = {}
        for i in range(len(str1)):
            if str1[i] not in m:
                m[str1[i]] = str2[i]
            elif m[str1[i]] != str2[i]:
                return False
        return len(set(str2)) < 26
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 17:26:17 2019

@author: hjiang
"""

"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
"""
# Time:  O(n)
# Space: O(1)

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = "aeiou"
        string = list(s)#'str' object does not support item assignment,所以这个list就少不了
        i, j = 0, len(s) - 1
        while i < j:
            if string[i].lower() not in vowels:
                i += 1
            elif string[j].lower() not in vowels:
                j -= 1
            else:
                string[i], string[j] = string[j], string[i]
                i += 1
                j -= 1
        return "".join(string)
    
    
    def reverseVowels1(self, s):
        dict1 = "aeiou"
        st = list(s)
        lookup = []
        position = []
        for i in range(len(st)):
            if st[i].lower in dict1:
                lookup.append(st[i])
                position.append(i)
        lookup = lookup[::-1]
        for i in range(len(position)):
            st[position[i]] = lookup[i]
        s = "".join(st)
        return s

if __name__ == "__main__":
    print(Solution().reverseVowels1("leetcode"))

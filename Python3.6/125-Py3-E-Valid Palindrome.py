# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 15:39:52 2019

@author: hjiang
"""

"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""
# Time:  O(n)
# Space: O(1)

class Solution(object):
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():# isalnum 说明这个是不是字母或者数字, 意思就是遇到标点等符号直接往后走一步 “。aa”就是回文
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i, j = i + 1, j - 1
        return True
    
if __name__ == "__main__":
    print(Solution().isPalindrome('。aa'))
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 17:24:16 2019

@author: hjiang
"""

"""
Given an input string, reverse the string word by word.

Example:  

Input: "the sky is blue",
Output: "blue is sky the".
Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. 
However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.
Follow up: For C programmers, try to solve it in-place in O(1) space.
"""
# Time:  O(n)
# Space: O(n)

class Solution(object):
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        return ' '.join(reversed(s.split()))
    

#方法来自186题
#Time:O(n)
#Space:O(1)
#很好理解，先把句子整体反过来，然后在逐个翻转单词
#这个方法也可以操作151题
class Solution1:
    def reverseWords(self, s):
        self.reverse(s, 0, len(s) - 1)#['e', 'u', 'l', 'b', ' ', 's', 'i', ' ', 'y', 'k', 's', ' ', 'e', 'h', 't']
        
        beg = 0
        for i in range(len(s)):
            if s[i] == ' ':#单词翻转
                self.reverse(s, beg, i-1)
                beg = i + 1
            elif i == len(s) -1:#最后的单词翻转
                self.reverse(s, beg, i)

    def reverse(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

if __name__ == "__main__":
    print(Solution1().reverseWords(["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]))
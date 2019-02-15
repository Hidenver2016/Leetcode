# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 17:24:57 2019

@author: hjiang
"""

"""
Given an input string , reverse the string word by word. 

Example:

Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
Note: 

A word is defined as a sequence of non-space characters.
The input string does not contain leading or trailing spaces.
The words are always separated by a single space.
Follow up: Could you do it in-place without allocating extra space?
"""
# Time: O(n)
# Space:O(1)

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        def reverse(s, begin, end):
            for i in range((end - begin) // 2):
                s[begin + i], s[end - 1 - i] = s[end - 1 - i], s[begin + i]

        reverse(s, 0, len(s))
        i = 0
        for j in range(len(s) + 1):
            if j == len(s) or s[j] == ' ':
                reverse(s, i, j)
                i = j + 1


#Time:O(n)
#Space:O(1)
#很好理解，先把句子整体反过来，然后在逐个翻转单词
#这个方法也可以操作151题
class Solution1:
    def reverseWords(self, s):
        self.reverse(s, 0, len(s) - 1)#['e', 'u', 'l', 'b', ' ', 's', 'i', ' ', 'y', 'k', 's', ' ', 'e', 'h', 't']        
        j = 0
        for i in range(len(s)):
            if s[i] == ' ':#单词翻转
                self.reverse(s, j, i-1)
                j = i + 1
            elif i == len(s) -1:#最后的单词翻转
                self.reverse(s, j, i)
        return s

    def reverse(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
    
if __name__ == "__main__":
    print(Solution1().reverseWords(["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
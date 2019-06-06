# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 16:08:38 2019

@author: hjiang
"""

"""
Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the 
square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, 
square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits 
and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

这个题，遇到’[‘就把之前的字符串进行进栈操作。遇到’]'进行出栈操作。

curstring保存的是出栈操作完成后的字符串。

注意这一步：curstring = prestring + prenum * curstring，prestring是前面的字符串，
prenum * curstring是这一步骤结束之后的字符串，所以是前面的字符串+现在的字符串得到目前已有的字符串。

"""

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        curnum = 0
        curstring = ''
        stack = []
        for char in s:
            if char == '[':
                stack.append(curstring)#这里压入已经存储好的字符
                stack.append(curnum)#接着压入计算好的数字
                curstring = ''#这两行归零
                curnum = 0
            elif char == ']':#开始计算
                prenum = stack.pop()#弹出数字
                prestring = stack.pop()#弹出字符，这里是上一次的
                curstring = prestring + prenum * curstring#总体计算
            elif char.isdigit():
                curnum = curnum * 10 + int(char)#计算十位数相加的
            else:
                curstring += char#现在的字符
        return curstring
    
if __name__ == "__main__":
    Input = "3[a2[c]]"
    print(Solution().decodeString(Input))
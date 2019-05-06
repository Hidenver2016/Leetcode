# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 17:27:53 2018

@author: hjiang
"""
"""
#Given a string containing digits from 2-9 inclusive, 
return all possible letter combinations that the number could represent.
#
#A mapping of digit to letters (just like on the telephone buttons) is given below. 
Note that 1 does not map to any letters.
#
#
#
#Example:
#
#Input: "23"
#Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

在拨号键盘上按下了几个键，问能打出来的字符串的所有组合是多少。
https://blog.csdn.net/fuxuemingzhu/article/details/79363119

"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        kvmaps = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = []
        self.dfs(digits, 0, res, '', kvmaps)
        return res
    
    def dfs(self, string, index, res, path, kvmaps):
#        if index == len(string):  #这四行是原答案
#            if path != '':
#                res.append(path)
#            return
        if string == "": return [""]#这四行是自己写的，感觉比较简单，但是这个零输入的边界条件要考虑一下
        if len(path) == len(string):
            res.append(path)
            return
        for j in kvmaps[string[index]]:#这里的j表示数字对应的字母串中的字母，比如 2的时候第一个是a
            self.dfs(string, index + 1, res, path + j, kvmaps)

if __name__ == "__main__":
    print(Solution().letterCombinations("23"))

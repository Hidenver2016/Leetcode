# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 15:46:37 2019

@author: hjiang
"""

"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
https://blog.csdn.net/fuxuemingzhu/article/details/69831375
自动寻找key,然后分类，是242的一个升级。重点掌握如何自动寻找key和自动分类

在C++里面注意sort是在原地操作的，所以要把字符串复制一份，否则会修改原来的字符串。
代码和249题高度类似
"""
#Time:O(n)
#Space:O(n)
import collections
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = collections.defaultdict(list)#注意这个用法， 比setdefault更快
        for string in strs:
            sorted_str = ''.join(sorted(string))#寻找key
            res[sorted_str].append(string)#分类
        return list(res.values())

if __name__ ==  "__main__":
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
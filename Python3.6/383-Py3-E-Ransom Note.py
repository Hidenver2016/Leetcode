# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 17:21:10 2019

@author: hjiang
"""

"""
Given an arbitrary ransom note string and another string containing letters from all the magazines, 
write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
理解题意很关键，这个是说从magazine中取出几个元素排列组合能够摆成ransomNote。每个字母只能用一回
直接Counter，然后判断前者的每个字符出现次数都小于后者即可。

用小的（）检查大的
"""
# Time:  O(n)
# Space: O(1)
#https://blog.csdn.net/fuxuemingzhu/article/details/54178342
#直接Counter，然后判断前者的每个字符出现次数都小于后者即可。
class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        rcount = collections.Counter(ransomNote)
        mcount = collections.Counter(magazine)
        for r, c in rcount.items():
            if c > mcount[r]:#注意c是数量，r是key
                return False
        return True

# Time:  O(n)
# Space: O(1)
import collections

class Solution2(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        return not collections.Counter(ransomNote) - collections.Counter(magazine) #不能反过来写的原因是，后面减去前面返回的不是true or false
    
if __name__ == "__main__":
    print(Solution2().canConstruct("aa", "aab"))
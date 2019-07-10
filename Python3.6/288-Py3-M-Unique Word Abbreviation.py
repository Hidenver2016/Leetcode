# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 16:29:33 2019

@author: hjiang
"""

"""
An abbreviation of a word follows the form <first letter><number><last letter>. 
Below are some examples of word abbreviations:

a) it                      --> it    (no abbreviation)

     1
     ↓
b) d|o|g                   --> d1g

              1    1  1
     1---5----0----5--8
     ↓   ↓    ↓    ↓  ↓    
c) i|nternationalizatio|n  --> i18n

              1
     1---5----0
     ↓   ↓    ↓
d) l|ocalizatio|n          --> l10n
Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. 
A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.

Example:

Given dictionary = [ "deer", "door", "cake", "card" ]

isUnique("dear") -> false
isUnique("cart") -> true
isUnique("cane") -> false
isUnique("make") -> true

这题题目不难，但题目定义的让我一脸懵逼。
就是给了一组List，里面有若干个英语单词。然后除去头和尾，其他的字符都缩成了数字，比如：
"dear"的头是d，尾巴是r，中间的ea一共是2个字母，所以变成了2，最终缩完的output是：d2r
https://leetcode.com/problems/unique-word-abbreviation/discuss/73145/Python-short-solution-using-defaultdict-with-comments.
"""
import collections
class ValidWordAbbr1:
    def __init__(self, dictionary):
        self.dic = collections.defaultdict(set)
        for s in dictionary:
            val = s
            if len(s) > 2:
                s = s[0]+str(len(s)-2)+s[-1]
            self.dic[s].add(val)
    
    def isUnique(self, word):
        val = word 
        if len(word) > 2:
            word = word[0]+str(len(word)-2)+word[-1]
        # if word abbreviation not in the dictionary, or word itself in the dictionary (word itself may 
        # appear multiple times in the dictionary, so it's better using set instead of list)
        #这个地方还要加list, 比较奇怪
        return len(self.dic[word]) == 0 or (len(self.dic[word]) == 1 and val == list(self.dic[word])[0])
class ValidWordAbbr: #这个更容易理解   
    def __init__(self, dictionary):
        self.dt = collections.defaultdict(set)
        for d in dictionary:
            abbr = d[0] + str(len(d)) + d[-1]
            self.dt[abbr].add(d)
    
    def isUnique(self, word):
        abbr = word[0] + str(len(word)) + word[-1]
        return abbr not in self.dt or self.dt[abbr] == set([word])

if __name__ == "__main__":
    Input = ["ValidWordAbbr","isUnique"]
    Word = ["hello","helao"]
    A = ValidWordAbbr(Word)
    print(A.isUnique(Word))
    print(A.isUnique("hello"))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
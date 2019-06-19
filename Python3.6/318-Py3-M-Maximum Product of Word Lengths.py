# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 12:13:22 2019

@author: hjiang
"""

"""
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) 
where the two words do not share common letters. You may assume that each word will contain only lower case letters. 
If no such two words exist, return 0.

Example 1:

Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16 
Explanation: The two words can be "abcw", "xtfn".
Example 2:

Input: ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4 
Explanation: The two words can be "ab", "cd".
Example 3:

Input: ["a","aa","aaa","aaaa"]
Output: 0 
Explanation: No such pair of words.
只要是有重复字母，就不计算
https://blog.csdn.net/fuxuemingzhu/article/details/80932597
"""
import collections
class Solution:
    def maxProduct(self, words):#暴力法， set
        """
        :type words: List[str]
        :rtype: int
        """
        word_dict = dict()
        for word in words:
            word_dict[word] = set(word)
        max_len = 0
        for i1, w1 in enumerate(words):
            for i2 in range(i1+1, len(words)):
                w2 = words[i2]
                if not (word_dict[w1] & word_dict[w2]):#只要是有重复字母，就不能计算了
                    max_len = max(max_len, len(w1) * len(w2))
        return max_len
    
"""    
这个是个巧妙的方法。我们知道int有32位，而英文小写字符只有26个，所以，对于一个字符串，
把其出现过的字符对应到int上去，那么这个int就能当做这个字符串的摘要，表示这个这个字符串中都有哪些字符。
"""
    def maxProduct1(self, words):#位运算,不用看了，太难想
        """
        :type words: List[str]
        :rtype: int
        """
        res = 0
        d = collections.defaultdict(int)
        N = len(words)
        for i in range(N):
            w = words[i]
            for c in w:
                d[w] |= 1 << (ord(c) - ord('a'))
            for j in range(i):
                if not d[words[j]] & d[words[i]]:
                    res = max(res, len(words[j]) * len(words[i]))
        return res

    
    
if __name__ == "__main__":
    Input = ["abcw","baz","foo","bar","xtfn","abcdef"]
    Input1 = ["abcw", "bc"]
    print(Solution().maxProduct(Input1))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
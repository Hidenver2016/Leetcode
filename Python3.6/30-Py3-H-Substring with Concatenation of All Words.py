# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 15:34:16 2019

@author: hjiang
"""

"""
You are given a string, s, and a list of words, words, that are all of the same length. 
Find all starting indices of substring(s) in s that is a concatenation of each word 
in words exactly once and without any intervening characters.

Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
Output: []
 顺序无所谓，只要求出现一次
"""
#https://www.cnblogs.com/zuoyuan/p/3779978.html 
"""
解题思路：使用一个字典统计一下L中每个单词的数量。由于每个单词的长度一样，以题中给的例子而言，
可以3个字母3个字母的检查，如果不在字典中，则break出循环。有一个技巧是建立一个临时字典curr，
用来统计S中那些在L中的单词的数量，必须和L中单词的数量相等，否则同样break。
"""
# Time:  O(m * n * k), where m is string length, n is dictionary size, k is word length
# Space: O(n * k)
import collections
class Solution1:#这个比较清晰，看这个就行了
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L): #可以加一些边界条件
        if not S or not L: return []
        wordNum, wordLen = len(L), len(L[0])
        words = collections.Counter(L)#Counter({'bar': 1, 'foo': 1})
        res = []
        for i in range(len(S) + 1 - wordLen * wordNum):#这里+1是需要遍历到最后一个词
            curr = collections.defaultdict(int)
            j = 0
            while j < wordNum:
                word = S[i + j * wordLen : i + j * wordLen + wordLen]# 一个一个单词的比较
                if word not in words: break #如果不在，直接挂
                curr[word] += 1
                if curr[word] > words[word]: break# 多了也挂
                j += 1
            if j == wordNum: res.append(i)
        return res
    
    def findSubstring1(self, S, L):#这个是上面的详细版本
        words={}
        wordNum=len(L)
        for i in L:
            if i not in words:
                words[i]=1
            else:
                words[i]+=1
        wordLen=len(L[0])
        res=[]
        for i in range(len(S)+1-wordLen*wordNum):
            curr={}; j=0
            while j<wordNum:
                word=S[i+j*wordLen:i+j*wordLen+wordLen]
                if word not in words: 
                    break
                if word not in curr: 
                    curr[word]=1
                else:
                    curr[word]+=1
                if curr[word]>words[word]: break
                j+=1
            if j==wordNum: res.append(i)
        return res
    
# Time:  O(m * n * k), where m is string length, n is dictionary size, k is word length
# Space: O(n * k)
import collections
class Solution2(object):#这个是时间空间复杂度的分析
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        result, m, n, k = [], len(s), len(words), len(words[0])
        if m < n*k:
            return result

        lookup = collections.defaultdict(int)
        for i in words:
            lookup[i] += 1                            # Space: O(n * k)

        for i in range(m+1-k*n):                     # Time: O(m)
            cur, j = collections.defaultdict(int), 0
            while j < n:                              # Time: O(n)
                word = s[i+j*k:i+j*k+k]               # Time: O(k)
                if word not in lookup:
                    break
                cur[word] += 1
                if cur[word] > lookup[word]:
                    break
                j += 1
            if j == n:
                result.append(i)

        return result
    
if __name__ == "__main__":
    s = "barfoothefoobarman"
    words = ["foo","bar"]
    s1 = "wordgoodgoodgoodbestword",
    words1 = ["word","good","best","word"]
    
    print(Solution1().findSubstring(s1, words1))
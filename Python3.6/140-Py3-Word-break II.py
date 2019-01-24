# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 17:56:09 2019

@author: hjiang
"""

"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, 
add spaces in s to construct a sentence where each word is a valid dictionary word. 
Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
"""
#http://www.cnblogs.com/grandyang/p/4576240.html
#https://blog.csdn.net/fuxuemingzhu/article/details/85089275
#https://leetcode.com/problems/word-break-ii/discuss/44311/Python-easy-to-understand-solution #可以仔细看一下底下的解释

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        res = []
        memo = dict()
        return self.dfs(s, res, wordDict, memo)
    
    def dfs(self, s, res, wordDict, memo):
        if s in memo: return memo[s]
        if not s:
            return [""]
        res = []
        for word in wordDict:
            if s[:len(word)] != word: continue
            for r in self.dfs(s[len(word):], res, wordDict, memo):
                res.append(word + ("" if not r else " " + r))
        memo[s] = res
        return res
#https://leetcode.com/problems/word-break-ii/discuss/44311/Python-easy-to-understand-solution
#https://zxi.mytechroad.com/blog/leetcode/leetcode-140-word-break-ii/  
#看这个比较容易懂
#时间复杂度和空间复杂度都是O(2^n)        
class Solution1(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        return self.helper(s, wordDict, {})

    def helper(self, s, wordDict, memo):#这个memo在这里很重要，就是把过去做过分解的东西记下来
        if s in memo: return memo[s] #看看有没有记忆里面已经分解好了的，有的话直接调用
        if not s: return []

        res = []
        for word in wordDict:
#            if not s.startswith(word):
            if s[:len(word)] != word:
                continue
            if len(word) == len(s):
                res.append(word)
            else:#这个是先直接递归到最后（先分解最后一个词），然后在逐级向前，把剩下的分解
                resultOfTheRest = self.helper(s[len(word):], wordDict, memo)
                for item in resultOfTheRest:
                    item = word + ' ' + item
                    res.append(item)
        memo[s] = res
        return res
    
if __name__ == "__main__":
    print(Solution1().wordBreak("catsanddog", ["cats", "dog", "sand", "and", "cat"]))    
    
    
    
    
    
    
    
    
    

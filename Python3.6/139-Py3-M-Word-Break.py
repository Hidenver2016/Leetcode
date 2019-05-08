# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 00:32:07 2018

@author: hjiang
"""

#Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, 
#determine if s can be segmented into a space-separated sequence of one or more dictionary words.
#
#Note:
#
#The same word in the dictionary may be reused multiple times in the segmentation.
#You may assume the dictionary does not contain duplicate words.
#Example 1:
#
#Input: s = "leetcode", wordDict = ["leet", "code"]
#Output: true
#Explanation: Return true because "leetcode" can be segmented as "leet code".
#Example 2:
#
#Input: s = "applepenapple", wordDict = ["apple", "pen"]
#Output: true
#Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
#             Note that you are allowed to reuse a dictionary word.
#Example 3:
#
#Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
#Output: false
#http://www.cnblogs.com/grandyang/p/4257740.html
#注意这里dp数组的长度比s串的长度大1，是因为我们要handle空串的情况，我们初始化dp[0]为true，
#然后开始遍历。注意这里我们需要两个for循环来遍历，因为此时已经没有递归函数了，
#所以我们必须要遍历所有的子串，我们用j把[0, i)范围内的子串分为了两部分，
#[0, j) 和 [j, i)，其中范围 [0, j) 就是dp[j]，范围 [j, i) 就是s.substr(j, i-j)，
#其中dp[j]是之前的状态，我们已经算出来了，可以直接取，只需要在字典中查找s.substr(j, i-j)是否存在了，
#如果二者均为true，将dp[i]赋为true，并且break掉，
# Time: O((n+1)(n+2)/2) 这就是一个等差数列求和 1~n+1
# Space: O(n+1)
# DP的方法： bottom-up 从子问题到父问题，用循环，与tabluar联系
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True# 对应空串
        for i in range(n):# 全部都循环一遍，对于每一个i都给拆成[0,j]和[j,i]， 后面是dp[n+1]所以这里是range(n)
            for j in range(i, -1, -1):#每一个j都试一遍
                if dp[j] and s[j:i + 1] in wordDict:#各种分法都记录下来
                    dp[i + 1] = True
                    break
        return dp[n]
#
#
if __name__ == "__main__":
    assert Solution().wordBreak("leetcode", {"leet", "code"}) == True

# Return true because "leetcode" can be segmented as "leet code".
# 这个题目感觉递归和迭代没有太大区别
# Time:  O(n * l^2)
# Space: O(n)
#class Solution(object):
#    def wordBreak(self, s, wordDict):
#        """
#        :type s: str
#        :type wordDict: Set[str]
#        :rtype: bool
#        """
#        n = len(s)
#
#        max_len = 0
#        for string in wordDict:
#            max_len = max(max_len, len(string))
#
#        can_break = [False for _ in xrange(n + 1)]
#        can_break[0] = True
#        for i in xrange(1, n + 1):
#            for l in xrange(1, min(i, max_len) + 1):
#                if can_break[i-l] and s[i-l:i] in wordDict:
#                    can_break[i] = True
#                    break
#
#        return can_break[-1]
#
#    
#if __name__ == "__main__":
#    print Solution().wordBreak("leetcode", ["leet", "code"])
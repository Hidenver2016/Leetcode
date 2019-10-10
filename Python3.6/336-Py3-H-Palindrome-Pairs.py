# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 23:05:14 2018

@author: hjiang
"""
"""
Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, 
so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:

Input: ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]] 
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:

Input: ["bat","tab","cat"]
Output: [[0,1],[1,0]] 
Explanation: The palindromes are ["battab","tabbat"]

https://leetcode.com/problems/palindrome-pairs/discuss/79209/Accepted-Python-Solution-With-Explanation
Worst case time complexity takes O(n * m * m) where n is the length of words and m is the length of wordlist.

Average case time complexity takes O(n * m). As in the average case, the dictionary (aka hashmap) takes a search of O(1) on average case time complexity
"""



class Solution:# 此题是全都是unique单词，如果不是unqiue的，前面写两句判断即可。所以两次判断都有不等于自己的句子 pos[::-1] != w　和　pos[::-1] != w
    def palindromePairs(self, words):

            lookup = {w:i for i,w in enumerate(words)}
            res = []
            for i, w in enumerate(words):
                for j in range(len(w)+1):#这里主要是考虑了单词断开的情况，一小半是一个字符串，一大半是另一个字符串(取到w的最后一位)
                    pre, pos = w[:j], w[j:]
                    if pre==pre[::-1] and pos[::-1] != w and pos[::-1] in lookup:# w在后面，需要条件是，前一半自己对称（作为合成回文的中心）， 后一半的回文lookup里面有
                            res.append([lookup[pos[::-1]], i])
                    if j != len(w) and pos==pos[::-1] and pre[::-1] != w and pre[::-1] in lookup:#w在前面的情况，需要后面一半都是自对称的，而且前面一半的回文loopup里面有
                            res.append([i, lookup[pre[::-1]]])
            return res
        
# Time:  O(n * k^2), n is the number of the words, k is the max length of the words.
# Space: O(n * k)

#import collections


class Solution1(object):
    def palindromePairs(self, words):
 
        res = []
        lookup = {}
        for i, word in enumerate(words):
            lookup[word] = i

        for i in range(len(words)):
            for j in range(len(words[i]) + 1):
                prefix = words[i][j:]
                suffix = words[i][:j]
                if prefix == prefix[::-1] and \
                   suffix[::-1] in lookup and lookup[suffix[::-1]] != i:
                    res.append([i, lookup[suffix[::-1]]])
                if j > 0 and suffix == suffix[::-1] and \
                   prefix[::-1] in lookup and lookup[prefix[::-1]] != i:
                    res.append([lookup[prefix[::-1]], i])
        return res

class Solution2(object):# 这个方法超时了，但也过了80个test
    def palindromePairs(self, words):
        def Palincheck(s):
            l, r = 0, len(s)-1
            while l < r:
                if s[l] != s[r]: return False
                l += 1
                r -= 1
            return True
        result = []
        for i, w in enumerate(words):
            for j in range(i+1, len(words)):
                w1 = words[j]
                temp1 = w + w1
                temp2 = w1 + w
                if Palincheck(temp1): result.append([i,j])
                if Palincheck(temp2): result.append([j,i])
        return result

if __name__ == "__main__":
    s1 = ["slls","slls"]
    s2 = ["abcd","dcba","lls","s","sssll"]
    print(Solution2().palindromePairs(s2))















#def solution(list1):
#    ans = []
#    len1 = len(list1)
#    for i in range(len1):
#        temp1 = list1[i]
#        for j in range(len1):
#            temp2 = list1[j]
#            temp3 = temp1 + temp2
#            if temp1 == temp2:
#                continue
#            elif len(temp3)%2 == 0:
#                sign = 0
#                for i1 in range(len(temp3)//2):
#                    if temp3[i1] != temp3[len(temp3)-1-i1]:
#                        sign += 1
#                if sign == 0:
#                    ans.append([i,j])
#            elif len(temp3)%2 != 0:
#                sign1 = 0
#                for i2 in range(len(temp3)//2):
#                    if temp3[i2] != temp3[len(temp3)-1-i2]:
#                        sign1 +=1
#                if sign1 == 0:
#                    ans.append([i,j])
#                    
#    return ans
#
#def solution1(list1):
#    ans = []
#    len1 = len(list1)
#    for i in range(len1):
#        temp1 = list1[i]
#        for j in range(len1):
#            temp2 = list1[j]
#            temp3 = temp1 + temp2
#            if temp1 == temp2:
#                continue
#            else:
#                sign = 0
#                for i1 in range(len(temp3)//2):
#                    if temp3[i1] != temp3[len(temp3)-1-i1]:
#                        sign += 1
#                if sign == 0:
#                    ans.append([i,j])
##            elif len(temp3)%2 != 0:
##                sign1 = 0
##                for i2 in range(len(temp3)//2):
##                    if temp3[i2] != temp3[len(temp3)-1-i2]:
##                        sign1 +=1
##                if sign1 == 0:
##                    ans.append([i,j])
#                    
#    return ans
#    
#
#if __name__ == "__main__":
#    print (solution1(["abcd","dcba","lls","s","sssll"]))
#    print (solution1(["bat","tab","cat"]))
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
            
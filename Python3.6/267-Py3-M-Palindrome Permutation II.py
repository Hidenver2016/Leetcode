# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 15:45:39 2019

@author: hjiang
"""

"""
Given a string s, return all the palindromic permutations (without duplicates) of it. 
Return an empty list if no palindromic permutation could be form.

Example 1:

Input: "aabb"
Output: ["abba", "baab"]
Example 2:

Input: "abc"
Output: []

这个需要仔细看！！！

https://leetcode.com/problems/palindrome-permutation-ii/discuss/69717/Backtrack-Summary%3A-General-Solution-for-10-Questions!!!!!!!!-Python-(Combination-Sum-Subsets-Permutation-Palindrome)

思路: 统计给定字符串中每个字符的个数, 如果有多于一个单数的字符, 说明是无法构成回文的, 此时返回[]. 

如果只有一个单数字符或者没有单数字符, 就将出现偶数次的字符分成两半, 一半用来做全排列, 然后组合成一个回文数. 
其组成为: 全排列字符串+ 出现单数次的字符+全排列字符串翻转.
--------------------- 
作者：小榕流光 
来源：CSDN 
原文：https://blog.csdn.net/qq508618087/article/details/50886870 
版权声明：本文为博主原创文章，转载请附上博文链接！
"""
# Time:  O(n * n!)
# Space: O(n)
import collections
class Solution:
    def generatePalindromes(self, s):
        kv = collections.Counter(s)
        mid = [k for k, v in kv.items() if v%2]#为奇数的字母只能有一个
        if len(mid) > 1:
            return []
        mid = '' if mid == [] else mid[0] #把唯一的奇数字母提取出来
        half = ''.join([k * (v//2) for k, v in kv.items()])#['a', 'bb', 'c']
        half = [c for c in half]# 一半字符的list #['a', 'b', 'b', 'c']
        
        def backtrack(end, res, path):#一半字符的长度end, 临时的排列组合path   整个这个backtrack应该就是在做去掉重复字母的permutation
            if len(path) == end:#表示完成了一个排列组合，用一半的字母
                cur = ''.join(path)
                res.append(cur + mid + cur[::-1])
                return
#            else:
            for i in range(end):
                if visited[i] or (i>0 and half[i] == half[i-1] and not visited[i-1]):#后面这一半是用来处理重复字母的
                    continue
#                print("times")
                visited[i] = True
                path.append(half[i])#加入path, 每次加入一个字母，就会把这个字母为首的所有排列过一遍，然后再置为False,弹出
                backtrack(end, res, path)
                visited[i] = False#用过之后在置为False
                path.pop()
                    
        res = []
        visited = [False] * len(half)
        backtrack(len(half), res, [])
        return res
    
if __name__ == "__main__":
    print(Solution().generatePalindromes("aaaaaa"))
    
    
    
    
    
    
    
    
    
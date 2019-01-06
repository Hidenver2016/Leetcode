# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 13:49:13 2019

@author: hjiang
"""

"""
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false

http://www.cnblogs.com/grandyang/p/4298664.html
重点看二维数组是怎么推导出来的
  Ø d b b c a
Ø T F F F F F
a T F F F F F
a T T T T T F
b F T T F T F
c F F T T T T
c F F F T F T

我们发现，在任意非边缘位置dp[i][j]时，它的左边或上边有可能为True或是False，两边都可以更新过来，
只要有一条路通着，那么这个点就可以为True。那么我们得分别来看，如果左边的为True，
那么我们去除当前对应的s2中的字符串s2[j - 1] 和 s3中对应的位置的字符相比（计算对应位置时还要考虑已匹配的s1中的字符），为s3[j - 1 + i], 
如果相等，则赋True，反之赋False

"""
# Time:  O(m * n)
# Space: O(m * n)
# Dynamic Programming
class Solution(object):
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        match = [[False for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]
        match[0][0] = True #那么当s1和s2是空串的时候，s3必然是空串，则返回true。所以直接给dp[0][0]赋值true
        for i in range(1, len(s1) + 1):
            match[i][0] = match[i - 1][0] and s1[i - 1] == s3[i - 1]
        for j in range(1, len(s2) + 1):
            match[0][j] = match[0][j - 1] and s2[j - 1] == s3[j - 1]
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                match[i][j] = (match[i - 1][j] and s1[i - 1] == s3[i -1 + j]) \ # 此处的偏置是针对j
                                       or (match[i][j - 1] and s2[j - 1] == s3[j - 1 + i]) #此处的偏置是针对i
        return match[-1][-1]
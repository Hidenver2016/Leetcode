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
重点看二维数组是怎么推导出来的，能否从左上连通道右下，就表示是否连通
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

而上边为True的情况也类似，所以可以求出递推公式为：

这样理解，一种是从s1[i-1]来的，所以要比较s1[i-1]和s3[j+i-1] (这里指由dp[i-1][j]到dp[i][j])
另一种是从s2[j-1]来的，所以要比较s2[j-1]和s3[i+j-1]

所以递推式如下

dp[i][j] = (dp[i - 1][j] && s1[i - 1] == s3[i - 1 + j]) || (dp[i][j - 1] && s2[j - 1] == s3[j - 1 + i]);

其中dp[i][j] 表示的是 s2 的前 i 个字符和 s1 的前 j 个字符是否匹配 s3 的前 i+j 个字符，根据以上分析，可写出代码如下：

"""
# Time:  O(m * n)
# Space: O(m * n)
# Dynamic Programming
class Solution(object):
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]
        dp[0][0] = True #那么当s1和s2是空串的时候，s3必然是空串，则返回true。所以直接给dp[0][0]赋值true
        for i in range(1, len(s1) + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]#因为之前差了那个空集，所以这里是i-1，实际上就是i
        for j in range(1, len(s2) + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i -1 + j]) \ # 此处的偏置是针对j
                                       or (dp[i][j - 1] and s2[j - 1] == s3[j - 1 + i]) #此处的偏置是针对i
        return dp[-1][-1]
    

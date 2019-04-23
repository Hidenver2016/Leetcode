# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 21:29:24 2019

@author: hjiang
"""

"""
A string of '0's and '1's is monotone increasing if it consists of some number of '0's (possibly 0), 
followed by some number of '1's (also possibly 0.)

We are given a string S of '0's and '1's, and we may flip any '0' to a '1' or a '1' to a '0'.

Return the minimum number of flips to make S monotone increasing.

 

Example 1:

Input: "00110"
Output: 1
Explanation: We flip the last digit to get 00111.
Example 2:

Input: "010110"
Output: 2
Explanation: We flip to get 011111, or alternatively 000111.
Example 3:

Input: "00011000"
Output: 2
Explanation: We flip to get 00000000.
 

Note:

1 <= S.length <= 20000
S only consists of '0' and '1' characters.

题意：可以变成前面是0后面是1的，也可以变成全部是0或者全部是1的

需要计算每个位置前面有多少个1加上后面有多少个0。因为前面的1要翻转成0，后面的0要翻转成1. 找一个最小的就可以了
https://blog.csdn.net/fuxuemingzhu/article/details/83247054
关于为什么要偏置一位，因为这样才可以遍历全部，包含最前面第一个和最后一个这样子的边界条件
"""
class Solution(object):
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        n = len(S)
        l = [0] * (n + 1)#错开一位就是表示，这一位之前有多少个1，不包括当前位置，所以要计算到n+1,才知道总共有多少个1
        for i in range(1, n+1):
            l[i] = l[i-1] + int(S[i-1]) - 0#前面有多少个1，不包括当前位置
        ans = l[-1]
        for i in range(n + 1):
            ans = min(ans, l[i] + (n - l[-1]) - (i - l[i]))#包括自己，向后面有多少零(n - l[-1]) - (i - l[i])
        return ans
       
class Solution0(object):
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        N = len(S)
        P = [0] # how many ones P的长度是N+1
        for s in S:
            P.append(P[-1] + int(s))
        ans = P[-1]
        for i in range(len(P)):#那么后面0的个数是：总的0的个数(即，总个数减去总的1的个数） - 前面0的个数（即，现在的位置索引减去前面1的个数）。
            ans = min(ans, P[i] + (N - P[-1]) - (i - P[i]))#包括自己，向后面有多少零
        return ans
    
"""
定义两个数组：
dp[i][0]:表示i之前结尾的数字是0，不包括i
dp[i][1]:表示i之前结尾的数字是1，不包括i
"""    
    
class Solution1(object):#欣赏
    def minFlipsMonoIncr(self, S):#dp[i]只和dp[i-1]有关系，所以可以考虑降维
        """
        :type S: str
        :rtype: int
        """
        N = len(S)
        dp = [[0] * 2 for _ in range(N + 1)]
        for i in range(1, N + 1):
            if S[i - 1] == '0':#如果当前数字是0
                dp[i][0] = dp[i - 1][0]#对于结尾是0的数组，可以不操作
                dp[i][1] = min(dp[i - 1][1], dp[i - 1][0]) + 1#对于结尾是1的数组，考虑之前是1的，把当前0翻转；或者之前是0的，也把当前0翻转，看哪个小
            else:#如果当前位是1
                dp[i][0] = dp[i - 1][0] + 1#对于结尾是0的数组来说，就是翻转一位
                dp[i][1] = min(dp[i - 1][1], dp[i - 1][0])#对于结尾是1的数字来说，可以是之前的1数组不变，也可以是之前的0数字变成1数组，看哪个小
        return min(dp[N][0], dp[N][1])

class Solution2(object):#再简化
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        N = len(S)
        dp = [0] * 2
        for i in range(1, N + 1):
            if S[i - 1] == '0':
                dp[0] = dp[0]
                dp[1] = min(dp[1], dp[0]) + 1
            else:
                dp[1] = min(dp[1], dp[0])
                dp[0] = dp[0] + 1
        return min(dp[0], dp[1])

if __name__ == "__main__":
    print(Solution().minFlipsMonoIncr("11011"))
    
    
    
    
        
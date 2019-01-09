# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 16:56:02 2019

@author: hjiang
"""

"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
https://blog.csdn.net/fuxuemingzhu/article/details/82120874
此题与70题非常像，就是多了一些限制，dp[i+1]代表解析s[:i]字符串所有可能的方式数目。
意思就是在dp[i]这个位置，不是由[i-1]直接来的，就是由[i-2]直接来的（多了限制，需要注意）
http://www.cnblogs.com/grandyang/p/4313384.html
"""
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0] * (len(s) + 1)
        dp[0] = 1#这里只是一个初始化
        for i in range(1, len(dp)):# i是从第1个位置起(dp的第1个)，是s的第0个
            if s[i-1] != '0':
                dp[i] = dp[i-1] #相当于加dp[i-1]
            if i != 1 and '09' < s[i-2:i] < '27':#从第二位开始，需要注意s[i-2:i]如果是i-2 = -1,(s[-1:1],或者s[5:1]，输出都是[]),此外注意字符串比较方法
                dp[i] += dp[i-2]#相当于dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
    
if __name__ ==  "__main__":
    print(Solution().numDecodings("226"))

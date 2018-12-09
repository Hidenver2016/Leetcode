# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 17:09:43 2018

@author: hjiang
"""

"""
Given strings S and T, find the minimum (contiguous) substring W of S, 
so that T is a subsequence of W.

If there is no such window in S that covers all characters in T, return the empty string "". 
If there are multiple such minimum-length windows, return the one with the left-most starting index.

Example 1:

Input: 
S = "abcdebdde", T = "bde"
Output: "bcde"
Explanation: 
"bcde" is the answer because it occurs before "bdde" which has the same length.
"deb" is not a smaller window because the elements of T in the window must occur in order.
 

Note:

All the strings in the input will only contain lowercase letters.
The length of S will be in the range [1, 20000].
The length of T will be in the range [1, 100].
"""

"""
Very brief explannation : m = len(T), n = len(S), 
scan string S and maintain a up to date list of start index of matching T in list dp(size of m), 
dp[i] denotes the start index when i+1 chars of T are matched. When T[i] appears in S, 
we simply update dp[i] = dp[i-1], when T[0] appears in S with index, we update dp[0] = index. 
Whenever dp[m-1] is updated, we have a new window that T is sub-sequence of, 
and we keep a running minimum of this window width

We scan S once, and each update depends the number of same char in T. 
The worst case is O(mn) when all position of T are identical. 
When the char in T doesn't have much repetition, O(n) time complexity is achieved.

Space complexity O(m)
https://leetcode.com/problems/minimum-window-subsequence/discuss/109354/Python-O(m)-space-complexity-almost-O(n)-time-complexity
http://www.cnblogs.com/grandyang/p/8684817.html
http://www.cnblogs.com/lightwindy/p/8486724.html
"""
class Solution(object):
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        n, m = len(S), len(T)
        
        dic = dict()
        for i, s in enumerate(T):
            dic.setdefault(s, []).append(i)
            
        dp = [-1 for i in range(m)]# len(T) 用来记录start index
        
        count = n+1#先把count放在最后
        start = -1#置于最前
        
        for index, c in enumerate(S):
            if c in dic:
                for i in dic[c][::-1]:# [::-1]表示reversed i是在T里面遍历的坐标，当i = m-1时表示遍历完毕
                    if i == 0:#第一个对上了
                        dp[i] = index
                    else:
                        dp[i] = dp[i-1]# When T[i] appears in S, we simply update dp[i] = dp[i-1]，因为i在T里面也是逐个扫描的，最终dp里面全是start index
                    if i == m-1 and dp[i] >= 0 and index - dp[i]+1 < count:#更新count的条件
                        count = index - dp[i] + 1
                        start = dp[i]
        if dp[-1] < 0:#这个表示最终也没搞好
            return ""
        return S[start:start+count]
    

#class Solution1(object):
#    def minWindow(self, S, T):
#        m, n = len(S), len(T)
#        start = -1
#        minLen = float("inf")
#        dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]
#        for i in range(m+1): dp[i][0] = i
#        for i in range(1, m+1):
#            for j in range(1, min(i,n)+1):
#                if S[i-1] == T[j-1]:
#                    dp[i][j] = dp[i-1][j-1]
#                else:
#                    dp[i][j] = dp[i-1][j]
#            if dp[i][n] != -1:
#                len1 = i - dp[i][n]
#                if minLen > len1:
#                    minLen = len1
#                    start = dp[i][n]
#        if start != -1:
#            return S[start:start + minLen]
#        else:
#            return ""
                    

    
    
if __name__ == "__main__":
    print(Solution1().minWindow("abcdebdde", "bded"))
    
    
    
    
    
    
    
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 15:45:28 2019

@author: hjiang
"""

"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example:

Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""
    
    
"""
https://leetcode.com/problems/palindrome-partitioning-ii/discuss/42198/My-solution-does-not-need-a-table-for-palindrome-is-it-right-It-uses-only-O(n)-space.
The definition of 'cut' array is the minimum number of cuts of a sub string. More specifically, cut[n] stores the cut number of string s[0, n-1].

Here is the basic idea of the solution:

Initialize the 'cut' array: For a string with n characters s[0, n-1], it needs at most n-1 cut. Therefore, the 'cut' array is initialized as cut[i] = i-1

Use two variables in two loops to represent a palindrome:
The external loop variable 'i' represents the center of the palindrome. The internal loop variable 'j' represents the 'radius' of the palindrome. 
Apparently, j <= i is a must.
This palindrome can then be represented as s[i-j, i+j]. If this string is indeed a palindrome, then one possible value of cut[i+j] is cut[i-j] + 1, 
where cut[i-j] corresponds to s[0, i-j-1] and 1 correspond to the palindrome s[i-j, i+j];

When the loops finish, you'll get the answer at cut[s.length]

"""
#Time: O(n^2)
#Space: O(n)
class Solution1(object):#也属于从中间向两边扩散
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        cut = list(range(-1, size))#[-1,0,...,size-1] 对于一个长度为i的str, 最多需要i-1次切开
        for idx in range(1, size):# (idx, idx)表示奇数， (idx-1,idx)表示偶数
            for low, high in (idx, idx), (idx - 1, idx):# for i, j in (1, 2), (3, 4): print (i, j)    # row1: 1 2; row2: 3 4
                while low >= 0 and high < size and s[low] == s[high]:
                    cut[high + 1] = min(cut[high + 1], cut[low] + 1)
                    low -= 1#状态转移方程， 如果s[low:high] (包括high)之间是回文， 那么cut[high+1]位置的最多就是cut[low]+1 (加上一个已经判断好的回文)
                    high += 1
        return cut[-1]
    
if __name__ == "__main__":
    print(Solution1().minCut('aab'))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
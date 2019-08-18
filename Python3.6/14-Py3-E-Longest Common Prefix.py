# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 16:52:04 2019

@author: hjiang
"""

"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""
# Time:  O(n * k), k is the length of the common prefix
# Space: O(1)

class Solution(object):
    def longestCommonPrefix(self, strs):#这个比较简洁
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        for i in range(len(strs[0])):
            for string in strs[1:]:
                if i >= len(string) or string[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]
    
    def longestCommonPrefix1(self, strs):#自己写的，时间复杂度一样，空间复杂度O(n)
        if not strs:
            return ""
        
        res = []
        strs= sorted(strs, key = len)#这里空间复杂度高，因为新建立了一个sorted list
        stan = strs[0]
        for i in range(len(stan)):
            sign = 0
            for j in range(1, len(strs)):
                if strs[j][i] == stan[i]:
                    sign += 1
            if sign == len(strs) - 1:
                res += stan[i]
            else:
                return "".join(res)
        return "".join(res)
    
if __name__ == "__main__":
    print(Solution().longestCommonPrefix1(["flower","flow","flight"]))
    
    
    
    
    
    
    
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 14:43:04 2018

@author: hjiang
"""

"""
Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.
关键：此题比较容易，遍历一遍即可得到结果
"""

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        longest, start, distinct_count, visited = 0, 0, 0, [0 for _ in range(256)]
        for i, char in enumerate(s):
            if visited[ord(char)] == 0:
                distinct_count += 1
            visited[ord(char)] += 1 #最主要的功能是记录有重复的元素

            while distinct_count > k:
                visited[ord(s[start])] -= 1# 不停的减去重复的元素，或者扫描过的元素
                if visited[ord(s[start])] == 0:
                    distinct_count -= 1
                start += 1 #前面减去了重复的元素（扫描过的），此处自然要加一

            longest = max(longest, i - start + 1)
        return longest
    
if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstringKDistinct("eeeba",2))

        
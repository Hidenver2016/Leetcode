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
找出最多k个不一样characters的最长序列

此题和159题一样，把k改为2即可
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
        res, start, distinct_count, visited = 0, 0, 0, [0 for _ in range(256)]
        for i, char in enumerate(s):
            if visited[ord(char)] == 0:
                distinct_count += 1 #记录不一样的元素
            visited[ord(char)] += 1 #最主要的功能是记录有重复的元素

            while distinct_count > k: #不一样的元素已经超过k个
                visited[ord(s[start])] -= 1 #不停的减去最开始的元素，相当于sliding window
                if visited[ord(s[start])] == 0:
                    distinct_count -= 1
                start += 1 #前面减去了重复的元素（扫描过的），此处自然要加一

            res = max(res, i - start + 1)
        return res
    
if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstringKDistinct("eeeba",2))

        
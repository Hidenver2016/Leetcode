# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 17:11:02 2018

@author: hjiang
"""

"""
159. Longest Substring with At Most Two Distinct Characters
Hard
361
7


Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

Example 1:

Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.
Example 2:

Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.

"""
import collections
class Solution:#和下面的解法思路是一模一样的
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = collections.defaultdict(int)
        result, i = 0, 0 #i表示left , j 表示right
        for j, env in enumerate(s):
            count[env] += 1
            while len(count) > 2:
                count[s[i]] -= 1#全都是不符合条件的时候操作开始的位置i
                if count[s[i]] == 0:
                    del count[s[i]]
                i += 1
            result = max(result, j-i+1)
        return result
    
    
#此题亦可直接复用340题的答案，把k=2即可
# Time:  O(n)
# Space: O(1)

class Solution1(object):#这个是340的答案，找k个不一样的最长序列
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        longest, start, distinct_count, visited = 0, 0, 0, [0 for _ in range(256)]
        for i, char in enumerate(s):
            if visited[ord(char)] == 0:
                distinct_count += 1 #记录不一样的元素
            visited[ord(char)] += 1 #最主要的功能是记录有重复的元素

            while distinct_count > k: #不一样的元素已经超过k个
                visited[ord(s[start])] -= 1 #不停的减去重复的元素，或者扫描过的元素
                if visited[ord(s[start])] == 0:
                    distinct_count -= 1
                start += 1 #前面减去了重复的元素（扫描过的），此处自然要加一

            longest = max(longest, i - start + 1)
        return longest
    
    
if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstringTwoDistinct("ccaabbb"))
            
                    
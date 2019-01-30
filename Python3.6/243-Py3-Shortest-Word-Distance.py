# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 17:44:03 2019

@author: hjiang
"""

"""
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
"""
# Time:  O(n)
# Space: O(1)

class Solution(object):
    # @param {string[]} words
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def shortestDistance(self, words, word1, word2):
        dist = float("inf")
        i, index1, index2 = 0, None, None
        while i < len(words):
            if words[i] == word1:
                index1 = i
            elif words[i] == word2:
                index2 = i

            if index1 is not None and index2 is not None:
                dist = min(dist, abs(index1 - index2))#对应于多个有重复的情况，比如有两个makes
            i += 1

        return dist
    
if __name__ == "__main__":
    print(Solution().shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "coding", "practice"))
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 17:27:26 2019

@author: hjiang
"""

"""
You are playing the following Flip Game with your friend: Given a string that 
contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". 
The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to compute all possible states of the string after one valid move.

Example:

Input: s = "++++"
Output: 
[
  "--++",
  "+--+",
  "++--"
]
Note: If there is no valid move, return an empty list [].
"""
# Time:  O(c * n + n) = O(n * (c+1))
# Space: O(n)

class Solution(object):
    def generatePossibleNextMoves(self, s):#写的太复杂了，没必要
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        i, n = 0, len(s) - 1
        while i < n:                                    # O(n) time
            if s[i] == '+':
                while i < n and s[i+1] == '+':          # O(c) time
                    res.append(s[:i] + '--' + s[i+2:])  # O(n) time and space
                    i += 1
            i += 1
        return res


# Time:  O(c * m * n + n) = O(c * n + n), where m = 2 in this question
# Space: O(n)
# This solution compares O(m) = O(2) times for two consecutive "+", where m is length of the pattern
class Solution2(object):
    def generatePossibleNextMoves(self, s):
      """
      :type s: str
      :rtype: List[str]
      """
      return [s[:i] + "--" + s[i+2:] for i in range(len(s) - 1) if s[i:i+2] == "++"]
    def generatePossibleNextMoves1(self, s):#看这个比较容易记
        res = []
        for i in range(len(s)-1):
            if s[i:i+2] == "++":
                res.append(s[:i] + "--" + s[i+2:])
        return res
              
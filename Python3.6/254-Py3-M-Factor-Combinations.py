# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 17:00:54 2019

@author: hjiang
"""

"""
Numbers can be regarded as product of its factors. For example,

8 = 2 x 2 x 2;
  = 2 x 4.
Write a function that takes an integer n and return all possible combinations of its factors.

Note:

You may assume that n is always positive.
Factors should be greater than 1 and less than n.
Example 1:

Input: 1
Output: []
Example 2:

Input: 37
Output:[]
Example 3:

Input: 12
Output:
[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]
Example 4:

Input: 32
Output:
[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2],
  [2, 4, 4],
  [4, 8]
]
"""
#http://www.cnblogs.com/grandyang/p/5332722.html
# Time:  O(nlogn)
# Space: O(logn)

class Solution(object):
    # @param {integer} n
    # @return {integer[][]}
    def getFactors(self, n):
        res = []
        path = []
        self.helper(n, res, path)
        return res

    def helper(self, n, res, path):
        i = 2 if not path else path[-1]
        while i*i <= n:
            if n % i == 0:
                path.append(i);
                path.append(n / i);
                res.append(list(path));
                path.pop();
                self.helper(n / i, res, path);
                path.pop()
            i += 1
            
            
            
            
            
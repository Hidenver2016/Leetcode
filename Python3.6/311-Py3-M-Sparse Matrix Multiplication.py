# -*- coding: utf-8 -*-
"""
Created on Tue May 28 23:18:41 2019

@author: hjiang
"""

"""
Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

Input:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

Output:

     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
"""

# Time:  O(m * n * l), A is m x n matrix, B is n x l matrix
# Space: O(m * l)

class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
#        m, n, l = len(A), len(A[0]), len(B[0])
#        res = [[0 for _ in range(l)] for _ in range(m)]
#        for i in range(m):
#            for k in range(n):
#                if A[i][k]: #这里是亮点，如果是0就不用计算了
#                    for j in range(l):
#                        res[i][j] += A[i][k] * B[k][j]
#        return res
    
        l, m, n = len(A), len(A[0]), len(B[0])
        res = [[0 for _ in range(n)] for _ in range(l)]
        for i in range(l):
            for j in range(m):
                if A[i][j]: #这里是亮点，如果是0就不用计算了
                    for k in range(n):
                        res[i][k] += A[i][j] * B[j][k]
        return res
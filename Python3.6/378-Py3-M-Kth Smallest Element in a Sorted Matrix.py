# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 21:29:00 2019

@author: hjiang
"""

"""
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note: 
You may assume k is always valid, 1 ≤ k ≤ n2.
"""
import bisect
class Solution:
    def kthSmallest(self, matrix, k):#自己写的，直接法
        temp = []
        for row in matrix:
            temp += row
        temp.sort()
        return temp[k-1]
    
    
class Solution1(object):
    def kthSmallest(self, matrix, k):#这个方法好，记住这个
        l, r = matrix[0][0], matrix[-1][-1]
        while l < r:
            m = (l + r) // 2
            if sum(bisect.bisect_right(row, m) for row in matrix) >= k:#在矩阵中比m小的数字的个数大于等于k
                r = m
            else:
                l = m + 1
        return l
    
if __name__ == "__main__":
    matrix = [
            [ 1,  5,  9],
            [10, 11, 13],
            [12, 13, 15]]
    k = 8
    print(Solution1().kthSmallest(matrix,k))
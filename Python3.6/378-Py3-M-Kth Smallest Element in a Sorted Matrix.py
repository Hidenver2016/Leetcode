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
O(n^2 * log n). Space complexity is O(n^2).
"""
import bisect
class Solution:
    def kthSmallest(self, matrix, k):#自己写的，直接法
        temp = []
        for row in matrix:
            temp += row
        temp.sort()
        return temp[k-1]
    
#O(n * log(n)) 
#The space complexity is constant.
#377. Combination Sum IV is pretty much doing the same thing,
#https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/85193/Binary-Search-Heap-and-Sorting-comparison-with-concise-code-and-1-liners-Python-72-ms
class Solution1(object):
    def kthSmallest(self, matrix, k):#这个方法好，记住这个
        l, r = matrix[0][0], matrix[-1][-1]
        while l < r:
            m = (l + r) // 2#注意大于等于是表示左边第一个（符合题意），而bisect_right表示小于等于的都要包括
            if sum(bisect.bisect_right(row, m) for row in matrix) >= k:#在矩阵中比m小的数字的个数大于等于k （计算每一行比m小的数字）
                r = m
            else:
                l = m + 1
        return l
    
if __name__ == "__main__":
    matrix = [
            [ 1,  5,  9],
            [10, 11, 13],
            [12, 18, 35]]
    k = 8
    print(Solution1().kthSmallest(matrix,k))
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 14:25:41 2019

@author: hjiang
"""

"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
https://blog.csdn.net/fuxuemingzhu/article/details/77444695
第一,python支持整体赋值，nums1[:n] = nums2[:n],
第二，这个题需要从两个序列的后面考虑，如果大，就往后面放，如果nums1先放完了，那么前面的数要由nums2[:n]来代替. 
    如果是nums2先放完了，那么无所谓

注意，如果nums1已经遍历结束了，就要把nums2剩下的元素放到nums1的前面。最后可以确保有序。
"""
# Time:  O(n)
# Space: O(1)
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n -1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        nums1[:n] = nums2[:n]
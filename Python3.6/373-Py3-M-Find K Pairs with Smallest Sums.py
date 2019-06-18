# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 16:18:51 2019

@author: hjiang
"""

"""
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u,v) which consists of one element from the first array and one element from the second array.

Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]] 
Explanation: The first 3 pairs are returned from the sequence: 
             [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [1,1],[1,1]
Explanation: The first 2 pairs are returned from the sequence: 
             [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
Example 3:

Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [1,3],[2,3]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]
"""
#https://blog.csdn.net/fuxuemingzhu/article/details/79564362
#看到全排列，于是我用了笛卡尔积，结果遇到特别长的两个数组时，内存超了。。代码还是很简单的。
import itertools
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        pairs = list(itertools.product(nums1, nums2))
        return sorted(pairs, key = lambda x: sum(x))[:k]

"""
首先将（nums1[i] + nums2[0], i, 0）加入堆，i取值范围[0, size1)

弹出堆顶元素sum, i, j，将(nums1[i], nums2[j])加入结果集ans

若j + 1 < size2，则将(nums1[i] + nums2[j + 1], i, j + 1)加入堆

循环直到结束
注意，不用保证每次进堆的元素是和最小！相对较小即可！
"""
import heapq
class Solution1(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        len1, len2 = len(nums1), len(nums2)
        if not len1 or not len2: return res
        heap = []
        for x in range(len1):
            heapq.heappush(heap, (nums1[x] + nums2[0], x, 0))
        while len(res) < min(k, len1 * len2):
            sum, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            if j + 1 < len2:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        return res












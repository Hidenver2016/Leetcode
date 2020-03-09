# -*- coding: utf-8 -*-
"""
Created on Thu May 23 16:04:51 2019

@author: hjiang
"""

"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such 
that you cannot load all elements into the memory at once?

https://blog.csdn.net/fuxuemingzhu/article/details/54341965#Python_112
"""
# time O(n+nlogn)
# space: O(5+length(res))
"""
Python排序+双指针
看到题目说了如果已经排序了会怎么样，这是一个很明显的需要排序的提示，告诉我们先排序。
下面的操作就像merge两个有序链表差不多，分别从两个的起始位置判断是否相等即可。

需要注意的是题目要求的是结果中的出现次数等于两个数组交集部分的次数，
所以当两个数组元素相等的时候需要把两个指针同时右移。

时间复杂度O(NlogN)，空间复杂度O(1).

"""
class Solution:
    def intersect(self, nums1, nums2):#移位
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        l1, l2 = 0, 0
        N1, N2 = len(nums1), len(nums2)
        res = []
        while l1 != N1 and l2 != N2:
            if nums1[l1] == nums2[l2]:
                res.append(nums1[l1])
                l1 += 1
                l2 += 1
            elif nums1[l1] < nums2[l2]:
                l1 += 1
            else:
                l2 += 1
        return res
    
"""
Python解法使用字典
使用字典对两个数组出现的数字进行统计，然后直接判断数字是否在另一个字典里出现过，把结果直接拼接上两个的最小次数个当前数字。

时间复杂度O(N)，空间复杂度O(N).打败了98%的提交
"""
import collections    
class Solution1:
    def intersect(self, nums1, nums2):#相乘
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        count1 = collections.Counter(nums1)
        count2 = collections.Counter(nums2)
        res = []
        for k, v in count1.items():
            if k in count2:
                res += [k] * min(v, count2[k])
        return res

if __name__ == "__main__":
    print(Solution1().intersect([4,9,5], [9,4,9,8,4]))


# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 14:13:51 2019

@author: hjiang
"""

"""
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:

Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
Example 2:

Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
"""
# Time:  O(n)
# Space: O(n)
"""
完全是自己想出来的算法哈哈哈。两个while嵌套，第一个嵌套遍历Nums，第二个嵌套要往后走，
看看后面的数字是不是比前面的数字大1，是的话就一直后移。根据i和j是否重叠来判断是加上一个数字还是加上一个区间。
依然来自负雪明烛
"""


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums: return []
        res = []
        i = 0
        while i < len(nums):
            j = i
            while j < len(nums) - 1 and nums[j] == nums[j + 1] - 1:
                j += 1
            if j == i:
                res.append(str(nums[i]))
            else:
                res.append('%s->%s' % (str(nums[i]), str(nums[j])))
            i = j + 1
        return res
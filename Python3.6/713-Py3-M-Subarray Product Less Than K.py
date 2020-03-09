# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 22:16:00 2020

@author: hjiang
"""

"""
Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Note:

0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.

O(n)
O(1)
"""
class Solution():
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0
        j = 0
        res = 1
        count = 0
        for i in range(len(nums)):
            res *= nums[i]
            if res >= k:
                while j <= i and res >= k:
                    res /= nums[j]
                    j += 1
            count += i - j + 1
        return count
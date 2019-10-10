# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 22:13:03 2019

@author: hjiang
"""

"""
Given an array of n integers nums and a target, 
find the number of index triplets i, j, k with 0 <= i < j < k < n 
that satisfy the condition nums[i] + nums[j] + nums[k] < target.

Example:

Input: nums = [-2,0,1,3], and target = 2
Output: 2 
Explanation: Because there are two triplets which sums are less than 2:
             [-2,0,1]
             [-2,0,3]
Follow up: Could you solve it in O(n2) runtime?
https://leetcode.com/problems/3sum-smaller/discuss/68881/Python-solution-with-comments.
"""
# O(n*n) time
def threeSumSmaller(self, nums, target):
    count = 0
    nums.sort()
    for i in range(len(nums)):
        j, k = i+1, len(nums)-1
        while j < k:
            s = nums[i] + nums[j] + nums[k]
            if s < target:
                # if (i,j,k) works, then (i,j,k), (i,j,k-1),..., 
                # (i,j,j+1) all work, totally (k-j) triplets
                count += k-j# 注意这里， 比如是012345， k=5, j=2,那么就是[2,3],[2,4],[2,5]。而不是k-j+1，这个是长度，不是配对数
                j += 1# 也要注意
            else:
                k -= 1
    return count
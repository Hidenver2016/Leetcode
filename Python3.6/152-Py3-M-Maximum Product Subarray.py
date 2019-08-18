# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 14:12:02 2019

@author: hjiang
"""

"""
Given an integer array nums, find the contiguous subarray within an array 
(containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
https://blog.csdn.net/fuxuemingzhu/article/details/83211451
当前的最大值等于已知的最大值、最小值和当前值的乘积，当前值，这三个数的最大值。
当前的最小值等于已知的最大值、最小值和当前值的乘积，当前值，这三个数的最小值。
结果是最大值数组中的最大值。
"""
# Time:  O(n)
# Space: O(1)

class Solution0(object):#和方法2一样,就看这个把
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        global_max, local_max, local_min = float("-inf"), 1, 1
        for x in A:
            local_max, local_min = max(x, local_max * x, local_min * x), min(x, local_max * x, local_min * x)
            global_max = max(global_max, local_max)
        return global_max
    
# Time:  O(n)
# Space: O(n)

class Solution1(object):#动态规划
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        N = len(nums)
        f = [0] * N
        g = [0] * N
        f[0] = g[0] = res = nums[0]
        for i in range(1, N):
            f[i] = max(f[i - 1] * nums[i], nums[i], g[i - 1] * nums[i])
            g[i] = min(f[i - 1] * nums[i], nums[i], g[i - 1] * nums[i])
            res = max(res, f[i])
        return res
    
# Time:  O(n)
# Space: O(1)
    
class Solution2(object):#1的改进，空间变成O(1)和方法0一样
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        N = len(nums)
        f = g = res = nums[0]
        for i in range(1, N):
            pre_f, pre_g = f, g
            f = max(pre_f * nums[i], nums[i], pre_g * nums[i])
            g = min(pre_f * nums[i], nums[i], pre_g * nums[i])
            res = max(res, f)
        return res


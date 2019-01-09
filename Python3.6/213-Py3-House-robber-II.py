# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 13:39:55 2019

@author: hjiang
"""

"""
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed. 
All houses at this place are arranged in a circle. 
That means the first house is the neighbor of the last one. 
Meanwhile, adjacent houses have security system connected and it will automatically 
contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, 
determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
             
那我们这里变通一下，如果我们把第一家和最后一家分别去掉，各算一遍能抢的最大值，然后比较两个值取其中较大的一个即为所求
"""

# Time:  O(n)
# Space: O(1)

#class Solution:
#    def rob(self, nums):
#        def rob(nums):
#            now = prev = 0
#            for n in nums:
#                now, prev = max(now, prev + n), now
#            return now
#        return max(rob(nums[len(nums) != 1:]), rob(nums[:-1]))
    
class Solution1:#这种比较好理解
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums) <= 2: return max(nums[0], nums[1])
        N = len(nums)
        return max(self.rob_range(nums[0 : N - 1]), self.rob_range(nums[1 : N]))
    
    def rob_range(self, nums):
#        if not nums: return 0
#        if len(nums) == 1: return nums[0]
#        if len(nums) == 2: return max(nums[0], nums[1])
        N = len(nums)
        dp = [0] * N
        dp[0], dp[1] = nums[0], max(nums[0], nums[1]) 
        for i in range(2, N):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]

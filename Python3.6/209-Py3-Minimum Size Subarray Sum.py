# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 17:30:45 2019

@author: hjiang
"""

"""
Given an array of n positive integers and a positive integer s, 
find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 
因为这个题需要求最小值，所以结果初始化为inf，每次移动一下右指针，当和满足条件的时候，更新结果，并移动左指针，同时记得把和删去左边的数字。
这里求和的区间是左右都是闭区间。

时间复杂度是O(N)，空间复杂度是O(1)。
"""
# Time:  O(n)
# Space: O(1)

class Solution(object):
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        start = 0
        sum = 0
        min_size = float("inf")#取最小值就要先赋值最大
        for i in range(len(nums)):
            sum += nums[i]
            while sum >= s:
                min_size = min(min_size, i - start + 1)#要记住这个算长度的套路
                sum -= nums[start]
                start += 1

        return min_size if min_size != float("inf") else 0

# Time:  O(nlogn)
# Space: O(n)
# Binary search solution.
#https://leetcode.com/problems/minimum-size-subarray-sum/discuss/59093/Python-O(n)-and-O(n-log-n)-solution
#http://www.cnblogs.com/grandyang/p/4501934.html        
class Solution1:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, target, nums):
        result = len(nums) + 1
        for idx, n in enumerate(nums[1:], 1):# 注意第二个参数是起始参数，表示从1开始数
            nums[idx] = nums[idx - 1] + n
        left = 0
        for right, n in enumerate(nums):
            if n >= target:
                left = self.find_left(left, right, nums, target, n)
                result = min(result, right - left + 1)
        return result if result <= len(nums) else 0
    
    def find_left(self, left, right, nums, target, n):
        while left < right:
            mid = (left + right) // 2
            if n - nums[mid] >= target:#这个地方相当于是求满足要求的子序列
                left = mid + 1
            else:
                right = mid
        return left
    
if __name__ == "__main__":
    print(Solution1().minSubArrayLen(7, [2,3,1,2,4,3]))
    
    
    
    
    
    
    
    
    
    
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 17:24:27 2019

@author: hjiang
"""

"""
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. 
You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Note: 
You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?
http://www.cnblogs.com/grandyang/p/4656517.html
http://zxi.mytechroad.com/blog/heap/leetcode-239-sliding-window-maximum/
"""

# Time:  O(n)
# Space: O(k)

from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dq = deque()
        max_numbers = []

        for i in range(len(nums)):
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            if i >= k and dq and dq[0] == i - k:
                dq.popleft()
            if i >= k - 1:
                max_numbers.append(nums[dq[0]])

        return max_numbers
    
    
#花花的答案    
import collections    
class MaxQueue:
  def __init__(self):
    self.q_ = collections.deque()
  
  def push(self, e):# 会把q里面比自己小的元素全部删掉  O(1)时间
    while self.q_ and e > self.q_[-1]: self.q_.pop()
    self.q_.append(e)
  
  def pop(self): #O(1)时间 vector pop是O(n)时间
    self.q_.popleft()
  
  def max(self):
    return self.q_[0]
    
class Solution1:
  def maxSlidingWindow(self, nums, k):
    q = MaxQueue()
    ans = []
    for i in range(len(nums)):
      q.push(nums[i])
      if i >= k - 1: #窗口已经放满了
        ans.append(q.max())
        if nums[i - k + 1] == q.max(): q.pop()# 这个地方的意思是，只有是最大的是最左边的才需要删掉（第一如果不是最大元素，那么已经被删了，第二，窗口向后移动，也会把第一个删掉）
    return ans    
    
    
    
    
    
    
    
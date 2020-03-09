# -*- coding: utf-8 -*-
"""
Created on Wed May 22 15:23:08 2019

@author: hjiang
"""

"""
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.
Note:

Your solution should be in logarithmic complexity.
https://blog.csdn.net/fuxuemingzhu/article/details/79633332
https://www.cnblogs.com/grandyang/p/4217175.html
那么我们在确定二分查找折半后中间那个元素后，和紧跟的那个元素比较下大小，
如果大于，则说明峰值在前面，如果小于则在后面。这样就可以找到一个峰值了，
代码如下：
"""
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid1 = (left + right) // 2
            mid2 = mid1 + 1
            if nums[mid1] >= nums[mid2]:
                right = mid1#峰值在右侧
            else:
                left = mid1 + 1 #峰值在左侧
        return left


if __name__ == "__main__":
    print(Solution().findPeakElement([1,2,1,3,5,6,4]))

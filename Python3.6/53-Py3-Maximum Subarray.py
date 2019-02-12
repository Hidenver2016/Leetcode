# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 17:28:12 2019

@author: hjiang
"""

"""
Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the 
divide and conquer approach, which is more subtle.
http://www.cnblogs.com/grandyang/p/4377150.html
GeekstoGeeks
"""
# Time:  O(n)
# Space: O(1)

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if max(nums) < 0:
            return max(nums)#如果都是负数的话，越加越小，答案就是只取一个数
        global_max, local_max = 0, 0
        for x in nums:
            local_max = max(x, local_max + x)
            global_max = max(global_max, local_max)
        return global_max


class Solution2: #这个是divide and conquer   
    def maxCrossingSum(self, arr, l, m, h) : 
        # Include elements on left of mid. 
        sm = 0; left_sum = float("-inf")
          
        for i in range(m, l-1, -1) : 
            sm = sm + arr[i]
            left_sum = max(left_sum, sm)# 相对于下面判断句，这个简单，但是时间长一点
              
#            if (sm > left_sum) : 
#                left_sum = sm 
                    
        # Include elements on right of mid 
        sm = 0; right_sum = float("-inf")
        for i in range(m + 1, h + 1) : 
            sm = sm + arr[i]
            right_sum = max(sm, right_sum)
              
#            if (sm > right_sum) : 
#                right_sum = sm 
                
        # Return sum of elements on left and right of mid 
        return left_sum + right_sum; 
            
    # Returns sum of maxium sum subarray in aa[l..h] 
    def maxSubArraySum(self, arr, l, h) :           
        # Base Case: Only one element 
        if (l == h) : 
            return arr[l] 
      
        # Find middle point 
        m = (l + h) // 2
      
        # Return maximum of following three possible cases 
        # a) Maximum subarray sum in left half 
        # b) Maximum subarray sum in right half 
        # c) Maximum subarray sum such that the  
        #     subarray crosses the midpoint  
        return max(self.maxSubArraySum(arr, l, m), 
                   self.maxSubArraySum(arr, m+1, h), 
                   self.maxCrossingSum(arr, l, m, h))
    
    def maxSubArray(self, nums):
        return self.maxSubArraySum(nums, 0, len(nums)-1)

if __name__ == "__main__":
    print(Solution2().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
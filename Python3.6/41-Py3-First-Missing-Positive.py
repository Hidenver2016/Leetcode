# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 22:42:24 2019

@author: hjiang
"""

"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.
"""
'''
http://www.cnblogs.com/grandyang/p/4395963.html
既然不能建立新的数组，那么我们只能覆盖原有数组，我们的思路是把1放在数组第一个位置nums[0]，2放在第二个位置nums[1]，
即需要把nums[i]放在nums[nums[i] - 1]上，那么我们遍历整个数组，如果nums[i] != i + 1, 
而nums[i]为整数且不大于n，另外nums[i]不等于nums[nums[i] - 1]的话，我们将两者位置调换，
如果不满足上述条件直接跳过，最后我们再遍历一遍数组，如果对应位置上的数不正确则返回正确的数，
'''

# Time:  O(n)
# Space: O(1)

class Solution(object):
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        i = 0
        while i < len(A):
            if A[i] > 0 and A[i] - 1 < len(A) and A[i] != A[A[i]-1]:
                A[A[i]-1], A[i] = A[i], A[A[i]-1]#需要把nums[i]放在nums[nums[i] - 1]上,数字放在对应的位置上
            else:
                i += 1

        for i, integer in enumerate(A):
            if integer != i + 1:
                return i + 1
        return len(A) + 1
    
if __name__ == "__main__":
    print(Solution().firstMissingPositive([3,4,-1,1])) # [1,-1,3,4] 每个数安扎位置放好
    print(Solution().firstMissingPositive([7,8,9,11,12]))# [7,8,9,11,12], 但是i在开始第二个循环就是i=5
    
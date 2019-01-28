# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 16:33:04 2019

@author: hjiang
"""

"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
最开始时两个指针都指向第一个数字，如果两个指针指的数字相同，则快指针向前走一步，
如果不同，则两个指针都向前走一步，这样当快指针走完整个数组后，慢指针当前的坐标加1就是数组中不同数字的个数，
"""
# Time:  O(n)
# Space: O(1)

class Solution(object):
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        length = 0
        for i in range(len(A)):
            if A[length] != A[i]:
                length += 1
                A[length] = A[i]#因为是duplicate，所以是修改后一个
        return length + 1 #因为是去重复，所以还是要留一个，此处就是+1 （与27题对比）
    
if __name__ == "__main__":
    print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
#    答案： 5, [0, 1, 2, 3, 4, 2, 2, 3, 3, 4]
    
    
    
    
    
    
    
    
    
    
    
    
    
    
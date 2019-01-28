# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 17:04:42 2019

@author: hjiang
"""

"""
Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,1,2,3,3],

Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.

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
"""
# Time:  O(n)
# Space: O(1)

#class Solution(object):
#    # @param a list of integers
#    # @return an integer
#    def removeDuplicates(self, A):
#        if not A:
#            return 0
#
#        last, same = 0, False
##        while i < len(A):
#        for i in range(1, len(A)):
#            if A[last] != A[i] or not same:
#                same = A[last] == A[i]
#                last += 1
#                A[last] = A[i]
##            i += 1
#
#        return last + 1, A
    
#https://blog.csdn.net/fuxuemingzhu/article/details/82829709
#一个快指针对所有的数字进行遍历，另外一个慢指针指向了不满足题目要求的第一个位置。
#这样当遍历到一个新的数字而且这个新的数字和慢指针指向的前两个数字相同时，把它交换到这个不满足的位置，然后两个指针同时右移即可。
class Solution1(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0#慢指针
        for n in nums:#快指针
            if i < 2 or n != nums[i - 2]:
                nums[i] = n
                i += 1
        return i
    
if __name__ == "__main__":
    print(Solution1().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
    print(Solution1().removeDuplicates([0,0,1,1,1,1,2,3,3]))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
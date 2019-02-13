# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 14:31:44 2019

@author: hjiang
"""

"""
A sequence of numbers is called a wiggle sequence if the differences between successive 
numbers strictly alternate between positive and negative. The first difference (if one exists) 
may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.

For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3) 
are alternately positive and negative. In contrast, [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences, 
the first because its first two differences are positive and the second because its last difference is zero.

Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence. 
A subsequence is obtained by deleting some number of elements (eventually, also zero) from the original sequence, 
leaving the remaining elements in their original order.

Example 1:

Input: [1,7,4,9,2,5]
Output: 6
Explanation: The entire sequence is a wiggle sequence.
Example 2:

Input: [1,17,5,10,13,15,10,5,16,8]
Output: 7
Explanation: There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].
Example 3:

Input: [1,2,3,4,5,6,7,8,9]
Output: 2
Follow up:
Can you do it in O(n) time?
"""
# Time:  O(n)
# Space: O(1)
#https://blog.csdn.net/fuxuemingzhu/article/details/82902655
#原数组里面的都算，

class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return n
        inc, dec = 1, 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                inc = dec + 1
            elif nums[i] < nums[i - 1]:
                dec = inc + 1
        return max(inc, dec)
    
    def wiggleMaxLength1(self,nums):# 自己乱编的题目，找连续的wiggle
        n = len(nums)
        if n <=1: return n
        inc, dec = 1, 1
        inc1, dec1 = [0]*len(nums), [0]*len(nums)
        for i in range(2,n):#因为是看前面两个，所以把判断句写在最前
            if nums[i-2] < nums[i-1] < nums[i] or nums[i-2] > nums[i-1] > nums[i]:
                
                inc, dec = 1, 1
            if nums[i] > nums[i-1]:
                inc = dec + 1
            elif nums[i] < nums[i-1]:
                dec = inc + 1
            inc1[i], dec1[i] = inc, dec

        inc3, dec3 = 1, 1
        inc4, dec4 = [0]*len(nums), [0]*len(nums)
        for i in range(n-2):#因为是看后面两个，所以把判断句写在最后

            if nums[i] > nums[i+1]:
                inc3 = dec3 + 1
            elif nums[i] < nums[i+1]:
                dec3 = inc3 + 1
            inc4[i], dec4[i] = inc3, dec3 
            if nums[i+2] < nums[i+1] < nums[i] or nums[i+2] > nums[i+1] > nums[i]:
                
                inc3, dec3 = 1, 1
        a1 = max(max(inc1), max(dec1))
        a2 = max(max(inc4), max(dec4))
        return max(a1, a2)
                
    
if __name__ == "__main__":
    print(Solution().wiggleMaxLength1([1,2,3,4,2,5,6,7,6,8,9,10,9,11,9]))
    print(Solution().wiggleMaxLength1([1,0,5,4,9,5,6,7,6,8,9,10,9,11,9]))
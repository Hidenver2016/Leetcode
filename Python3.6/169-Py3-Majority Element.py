# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 14:03:13 2019

@author: hjiang
"""

"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""

import collections
class Solution(object):
    def majorityElement(self, nums):#此解法中的dict操作需要掌握！！！
        """
        :type nums: List[int]
        :rtype: int
        """
        keys = set(nums)
        dict1 = dict()
        for i in keys:
            dict1[i] = 0#要先赋值为0！！！
        
        for j in nums:
            dict1[j] += 1
        
        dict2 = {v: k for k, v in dict1.items()} #由values求key
        
        return dict2[max(dict1.values())] #get values取最大，然后求key
#        return nums[idx]

    def majorityElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(collections.Counter(nums).items(), key=lambda a: a[1], reverse=True)[0][0]
    
if __name__ == "__main__":
    print(Solution().majorityElement([2,2,1,1,1,2,2,3,4,5,3,3,4]))
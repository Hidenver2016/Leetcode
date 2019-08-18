# -*- coding: utf-8 -*-
"""
Created on Wed May 22 15:12:09 2019

@author: hjiang
"""

"""

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

具体来说，假设数组是A，每次左边缘为l，右边缘为r，还有中间位置是m。在每次迭代中，分三种情况：

（1）如果target==A[m]，那么m就是我们要的结果，直接返回；
（2）如果A[m]<A[r]，那么说明从m到r一定是有序的（没有受到rotate的影响），那么我们只需要判断target是不是在m到r之间，如果是则把左边缘移到m+1，
否则就target在另一半，即把右边缘移到m-1。
（3）如果A[m]>=A[r]，那么说明从l到m一定是有序的，同样只需要判断target是否在这个范围内，相应的移动边缘即可。

注意，由于这个题目要进行和边缘元素的判断，所以没有采取[l,r)的左闭右开区间，而是使用了[l, r]双闭区间。
--------------------- 

原文：https://blog.csdn.net/fuxuemingzhu/article/details/79534213 

33, 81一起做

"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums: return -1
        l, r = 0, len(nums) - 1
        while l <= r:#注意，边缘元素的判断
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[r]:#mid和r之间是有序的
                if nums[mid] < target <= nums[r]:#注意mid的那一侧都是小于或者大于，另一侧才包含等于，这样才好修改
                    l = mid + 1#在右侧
                else:
                    r = mid - 1#在左侧
            else:#左侧是一定有序的
                if nums[mid] > target >= nums[l]:
                    r = mid - 1#在左侧
                else:
                    l = mid + 1#在右侧
        return -1

if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    target = 0
    print(Solution().search(nums, target))          
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
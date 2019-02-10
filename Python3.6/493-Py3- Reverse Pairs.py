# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 22:13:57 2019

@author: hjiang
"""

"""
Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.

Example1:

Input: [1,3,2,3,1]
Output: 2
Example2:

Input: [2,4,3,5,1]
Output: 3
Note:
The length of the given array will not exceed 50,000.
All the numbers in the input array are in the range of 32-bit integer.
http://www.cnblogs.com/grandyang/p/6657956.html
https://stackoverflow.com/questions/2272819/sort-a-part-of-a-list-in-place  关于python的部分数组排序
"""

# Time:  O(nlogn)
# Space: O(n)

class Solution0(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def merge(nums, start, mid, end):
            r = mid + 1
            tmp = []
            for i in range(start, mid + 1):
                while r <= end and nums[i] > nums[r]:
                    tmp.append(nums[r])
                    r += 1
                tmp.append(nums[i])
            nums[start:start+len(tmp)] = tmp

        def countAndMergeSort(nums, start, end):
            if end - start <= 0:
                return 0

            mid = start + (end - start) // 2
            count = countAndMergeSort(nums, start, mid) + countAndMergeSort(nums, mid + 1, end)
            r = mid + 1
            for i in range(start, mid + 1):
                while r <= end and nums[i] > nums[r] * 2:
                    r += 1
                count += r - (mid + 1)
#            merge(nums, start, mid, end)  #https://stackoverflow.com/questions/2272819/sort-a-part-of-a-list-in-place
#            nums[start:(end+2)].sort()
            nums[start:(end+1)] = sorted(nums[start:(end+1)])#实现python中的部分数组排序，可以直接不要上面那个merge函数
            return count
        return countAndMergeSort(nums, 0, len(nums) - 1)


import numpy as np      
class Solution1(object):#这个和上面的是一样的，就是要注意第88行，等于上面那个merge函数
    def reversePairs(self, nums):
        nums = np.array(nums)
        """
        :type nums: List[int]
        :rtype: int
        """

        def countAndMergeSort(nums, start, end):
            
            if end - start <= 0:
                return 0

            mid = start + (end - start) // 2
            count = countAndMergeSort(nums, start, mid) + countAndMergeSort(nums, mid + 1, end)
            r = mid + 1
            for i in range(start, mid + 1):
                while r <= end and nums[i] > nums[r] * 2:
                    r += 1
                count += r - (mid + 1)
#            merge(nums, start, mid, end)  #https://stackoverflow.com/questions/2272819/sort-a-part-of-a-list-in-place
#            nums[start:(end+2)].sort()
            nums[start:(end+1)].sort()
            return count

        return countAndMergeSort(nums, 0, len(nums) - 1)

if __name__ == "__main__":
    print(Solution1().reversePairs([1,3,2,3,1]))
    print(Solution1().reversePairs([2,4,3,5,1]))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
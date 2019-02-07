# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 17:17:15 2019

@author: hjiang
"""

"""
Given two arrays of length m and n with digits 0-9 representing two numbers. 
Create the maximum number of length k <= m + n from digits of the two. 
The relative order of the digits from the same array must be preserved. 
Return an array of the k digits.

Note: You should try to optimize your time and space complexity.

Example 1:

Input:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
Output:
[9, 8, 6, 5, 3]
Example 2:

Input:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
Output:
[6, 7, 6, 0, 4]
Example 3:

Input:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
Output:
[9, 8, 9]
"""
#https://leetcode.com/problems/create-maximum-number/discuss/77286/Short-Python-Ruby-C%2B%2B
#https://leetcode.com/problems/create-maximum-number/discuss/77291/Share-my-Python-solution-with-explanation


"""
http://bookshadow.com/weblog/2015/12/24/leetcode-create-maximum-number/
https://leetcode.com/problems/create-maximum-number/discuss/77286/Short-Python-Ruby-C%2B%2B
1. 从数组nums中挑选出t个数，在保持元素相对顺序不变的情况下，使得选出的子数组最大化。

2. 在保持元素相对顺序不变的前提下，将数组nums1与数组nums2合并，使合并后的数组最大化。

枚举nums1子数组与nums2子数组的长度len1, len2，在满足长度之和len1+len2等于k的前提下，分别求解最大子数组，并进行合并。

然后从合并得到的子数组中取最大数组即为所求。
"""

class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        def getMax(nums, k):# 1. 从数组nums中挑选出t个数，在保持元素相对顺序不变的情况下，使得选出的子数组最大化。
            drop = len(nums) - k
            out = []
            for num in nums:
                while drop and out and out[-1] < num:#因为是要按顺序来，所以每次都只比较最后的就可以了
                    out.pop()
                    drop -= 1# 取k个数就是要弹出len(nums)-k个数
                out.append(num)
            return out[:k]


        def merge(nums1, nums2):# 2. 在保持元素相对顺序不变的前提下，将数组nums1与数组nums2合并，使合并后的数组最大化。
            return [max(nums1, nums2).pop(0) for _ in nums1 + nums2]
        
        len1, len2 = len(nums1), len(nums2)
        res = []
#        for x in range(max(0, k - len2), min(k, len1) + 1):#这个地方太不好理解了
        for x in range(k+1):
            if x <= len1 and k - x <= len2:
                tmp = merge(getMax(nums1, x), getMax(nums2, k - x))#在满足长度之和len1+len2等于k的前提下，分别求解最大子数组
                res = max(tmp, res)
        return res
    
    
if __name__ == "__main__":
    print(Solution().maxNumber([6,7],[6,0,4],5))
    
    
    
    
    
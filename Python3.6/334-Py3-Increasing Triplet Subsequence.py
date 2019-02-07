# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 10:53:17 2019

@author: hjiang
"""

"""
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

Return true if there exists i, j, k 
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

Example 1:

Input: [1,2,3,4,5]
Output: true
Example 2:

Input: [5,4,3,2,1]
Output: false
"""

# Time:  O(n)
# Space: O(1)

#import bisect


class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        min_num, a, b = float("inf"), float("inf"), float("inf")
        for c in nums:
            if min_num >= c:
                min_num = c
            elif b >= c:
                a, b = min_num, c
            else:  # a < b < c
                return True
        return False
#https://blog.csdn.net/fuxuemingzhu/article/details/79826703
#整体的思想其实是很灵活的，保存的是遍历时见到的最小和次小
#这个题目也可以参考grandyang的解，dp,不过超时了      http://www.cnblogs.com/grandyang/p/5194599.html  
    
class Solution1(object):# 这个比较好理解
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first, second = float('inf'), float('inf')
        for num in nums:
            if num <= first:
                first = num #最小的数在这里就会返回
            elif num <= second:
                second = num #次小的数在这里也会返回
            else:# a < b < c
                return True#这里就是第三大的数
        return False


if __name__ == "__main__":
    print(Solution1().increasingTriplet([4,5,1,2,6]))
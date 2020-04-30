# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 14:18:12 2019

@author: hjiang
"""

"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), 
prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""

#https://blog.csdn.net/fuxuemingzhu/article/details/79530847
#http://www.cnblogs.com/grandyang/p/4843654.html

"""
这个题中，一定有重复的数字，因此最少也得两个数字，故不用进行只有一个数字和是否有环的判断。
142题类似 linked list cycle II
道理是因为有重复数字，那么指针在移动的过程中一定会因为这个重复的数字反复的经过某一条路径。
这个路径就是我们所谓的链表的环。如果抽象到这个层面就可以使用求环的算法解析了
"""
class Solution(object):#这个反而比较快
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:#这个算出位置, 第slow个数字重复了,三个重复数就不行了，找大概位置
            fast = nums[nums[fast]]
            slow = nums[slow]
        fast = 0
#        return nums[slow]
        while slow != fast:#这个才是数字，重复的数字是什么，只有这个的话，不收敛，会乱跑
            fast = nums[fast]
            slow = nums[slow]
        return fast
#二分查找
#https://leetcode.com/problems/find-the-duplicate-number/discuss/73022/Python-Solution-with-O(1)-space-and-O(nlogn)-time
"""
The difficulty in this problem lies in O(1) space, and many solution using O(n) space can also be accepted by OJ.
The solution is applying bi-search in the range[1, n] by counting the element which falls in sub range(n/2, n].
If the number is bigger than capacity of that sub range, it means the duplicated integer falls in the sub-range.
Otherwise the duplicated integer falls in the other half sub range.
我们统计小于等于mid的数字个数count，当nums在[1,mid]双闭区间中的数字不存在重复时，count应该恰好等于mid；
当nums在[1,mid]双闭区间中的数字存在重复时，count应该>mid；当nums在[1,mid]双闭区间中的数字存在遗漏时，
count应该<mid。所以，当我们发现count <= mid时，说明重复数字在[mid + 1, N]中，否则在[1,mid)中。

原文：https://blog.csdn.net/fuxuemingzhu/article/details/79530847 

"""
class Solution1(object):
    def findDuplicate(self, nums):
        low = 0
        high = len(nums) - 1
        mid = (high + low) // 2
        while low + 1 < high:
            count = 0
            for k in nums:
                if mid < k <= high:
                    count += 1#相当于一个重复数的计数器
            if count > high - mid:
                low = mid
            else:
                high = mid
            mid = (high + low) // 2
        return high
    
if __name__ == "__main__":
    print(Solution().findDuplicate([1,3,4,2,2,5,6]))
    # print(Solution().findDuplicate([2,5,9,6,9,3,8,9,7,1]))
    
    
    
    
    
    
    
    
    
    
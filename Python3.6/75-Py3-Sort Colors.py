# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 14:27:56 2019

@author: hjiang
"""

"""
Given an array with n objects colored red, white or blue, sort them in-place so that objects 
of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array 
with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
https://blog.csdn.net/fuxuemingzhu/article/details/79392195
因为只有三个数，所以简单的方法是计数排序。第一次遍历，统计出这三个数字出现的次数，第二次遍历，根据三个数字的次数对原列表进行修改。
"""
from collections import Counter
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = Counter(nums)# count[0]是最小的数有多少个，这里最小的数是0，所以接下来就是三个判断句直接全部重新插入数组即可
        for i in range(len(nums)):
            if i < count[0]:
                nums[i] = 0
            elif i < count[0] + count[1]:
                nums[i] = 1
            else:
                nums[i] = 2
                
"""
如果只能扫一遍，很容易想到的就是左边存放0和1，右边存放2.两边往中间靠。

设置两个指针，zero和two；zero指向第一个1的位置（0串的末尾），two指向第一个非2的位置。然后用i对nums进行遍历：

然后使用i从头到尾扫一遍，直到与two相遇。

i遇到0就换到左边去，遇到2就换到右边去，遇到1就跳过。

需要注意的是：由于zero记录第一个1的位置，因此A[zero]与A[i]交换后，A[zero]为0,A[i]为1，因此i++，zero++；

而two记录第一个非2的位置，可能为0或1，因此A[two]与A[i]交换后，A[two]为2,A[i]为0或1，i不能前进，要后续判断。

"""
                
class Solution1(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero = 0
        two = len(nums) - 1
        i = 0
        while i <= two:
            if nums[i] == 0:
                nums[zero], nums[i] = nums[i], nums[zero]
                i += 1
                zero += 1#zero指向第一个1的位置（0串的末尾）
            elif nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                nums[two], nums[i] = nums[i], nums[two]
                two -= 1#被换的变，two变了，i不变  two指向第一个非2的位置（从右向左，或者说是1的最后一个位置）。
        return nums
                
if __name__ == "__main__":
    print(Solution1().sortColors([2,0,2,1,1]))


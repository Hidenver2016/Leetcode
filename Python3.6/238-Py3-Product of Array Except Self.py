# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 14:10:20 2019

@author: hjiang
"""

"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] 
is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]  
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not 
count as extra space for the purpose of space complexity analysis.)
方法：
第一遍，从左向右：
[1,2,3,4]
[1,1,2,6] left_product
计算的是每个数字左边的乘积，斜着计算
第二遍，从右向左：
[24,12,8,6] 计算的是右边的乘积，斜着计算
"""

# Time:  O(n)
# Space: O(1)

class Solution(object):
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        if not nums:
            return []

        left_product = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            left_product[i] = left_product[i - 1] * nums[i - 1]

        right_product = 1
        for i in range(len(nums) - 2, -1, -1):
            right_product *= nums[i + 1]
            left_product[i] = left_product[i] * right_product

        return left_product
#这个题巧妙的地方在于，结果数组不算作空间复杂度里，所以可以用在结果数组中遍历的方式去做。
#第一次遍历在结果数组里保存每个数字左边的数字乘积，第二个遍历保存的是左边乘积和这个数字右边的乘积的乘积。
# https://blog.csdn.net/fuxuemingzhu/article/details/79325534       
class Solution1(object):#和上面的一样，比较简洁
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = []
        _len = len(nums)
        prod = 1
        for i in range(_len):# 左边的乘积
            answer.append(prod)# 1，1，2，6
            prod *= nums[i]
        prod = 1
        for i in range(_len - 1, -1, -1):#右边的乘积
            answer[i] *= prod#24，12，8，6
            prod *= nums[i]
        return answer
    
if __name__ == "__main__":
    print(Solution().productExceptSelf([1,2,3,4]))
    
    
    
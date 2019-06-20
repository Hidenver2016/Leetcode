# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 11:34:13 2019

@author: hjiang
"""

"""
Given an array of numbers nums, in which exactly two elements appear only once 
and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
Note:

The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. 
Could you implement it using only constant space complexity?


想到这个系列的第一个题，就是找出单个的只出现一次的字符。做法是异或操作。这个题也是用异或。

把所有的数字进行一次异或，得到的是只出现了一次的两个数字的异或。

这两个数字不等，因此他们的二进制必定至少1位不同，即异或结果中为1的那位（一个数字的该位为1，另个数字的该位为0）。
找出从右向左的第一个不同的位置（异或值为1的位置），给mask在该位置设置成1，mask的其余位置是0. 
mask存在的意义在于我们能通过该位置来分辨出两个只出现了一次的数字。

然后技巧性的来了：再进行一次异或操作。

每个数字都跟mask相与。通过与的结果为0和为1，即可区分出两个数字。

我刚开始有点不明白的是，为什么把所有的元素都重新异或了？其实，因为除了这两个元素以外，其他的元素都出现了两次，
这两次相同的数字的和mask的与操作的结果是相同的，所以会被异或两次抵消掉。

一言以蔽之，先通过异或找出两个元素的异或结果。再根据异或结果的出现为1的位置作为mask，mask的二进制只有1位是1，
也就是只看两个元素的该位置。最后，通过与操作判断该位置是0还是1区分两个元素。
--------------------- 

原文：https://blog.csdn.net/fuxuemingzhu/article/details/79434100 

"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        num1, num2 = 0, 0
        for num in nums:
            xor ^= num
        mask = 1
        while xor & mask == 0:
            mask = mask << 1
        for num in nums:
            if num & mask == 0:
                num1 ^= num
            else:
                num2 ^= num
        return [num1, num2]


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = collections.Counter(nums)
        res = []
        for num, c in count.items():
            if c == 1:
                res.append(num)
        return res

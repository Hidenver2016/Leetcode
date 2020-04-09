# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 13:57:17 2019

@author: hjiang
"""

"""
Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of
 [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();

另外一个抽样算法叫做水塘抽样，其本来的目的是在大数据流中的随机抽样问题，即：当内存无法加载全部数据时，如何从包含未知大小的数据流中随机选取k个数据，
并且要保证每个数据被抽取到的概率相等。

当K = 1时，数据流中第i个数被保留的概率为 1/i。只要采取这种策略，只需要遍历一遍数据流就可以得到采样值，并且保证所有数被选取的概率均为 1/N 。
当K > 1时，对于前k个数，我们全部保留，对于第i（i>k）个数，我们以K/i的概率保留第i个数，并以 1/K的概率与前面已选择的k个数中的任意一个替换。

这个和水塘采样貌似没关系！！！


依次遍历列表中的每一位，并将这一位与其后面的随机一位交换顺序。
https://blog.csdn.net/fuxuemingzhu/article/details/79391342
"""
import random
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        res = self.nums[:]
        for i in range(len(self.nums)):
            t = random.randrange(i, len(self.nums))
            res[i], res[t] = res[t], res[i]
            
        return res








class Solution1(object):#库函数

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        nums_s = self.nums[:]
        random.shuffle(nums_s)
        return nums_s
    
    
    
    
    
    
    
    
    
    
    

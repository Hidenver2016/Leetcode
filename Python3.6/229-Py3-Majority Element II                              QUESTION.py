# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 14:03:54 2019

@author: hjiang
"""

"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
"""
#https://blog.csdn.net/fuxuemingzhu/article/details/83501323
import collections
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        count = collections.Counter(nums)
        res = []
        for n, t in count.items():
            if t > N / 3:
                res.append(n)
        return res
    def majorityElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [i[0] for i in collections.Counter(nums).items() if i[1] > len(nums) / 3] #这个里面i[1]是次数，i[0]是key

    
"""
https://blog.csdn.net/fuxuemingzhu/article/details/51288749
/*
    思路：摩尔投票(Moore Vote)升级版，超过n/3的数最多只能有两个；
    先选出两个候选人A,B,遍历数组，如果投A（等于A），则A的票数++;如果投B，B的票数++；
    如果A,B都不投（即与A，B都不相等）,那么检查此时是否AB中候选人的票数是否为0，如果为0,则成为新的候选人；
    如果A,B两个人的票数都不为0，那么A,B两个候选人的票数均--；
    遍历结束后选出两个候选人，但是这两个候选人是否满足>n/3，还需要再遍历一遍数组，找出两个候选人的具体票数
     */
     
     
1.对于v[i](1<=i<=n)，如果c此时为未知状态，则c=v[i]，t=1，递增i。
2.如果c==v[i]，++t，递增i。
3.如果c!=v[i]，--t，如果t==0，将c置为未知状态，递增i。 
4.所有投票处理完毕后，如果c为未知状态，则说明不存在任何候选人的得票数过半，否则重新遍历数组v，
  统计候选人c的实际得票总数，如果c的得票数确实过半，则c就是最终结果。

"""
class Solution1(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        m = n = cm = cn = 0
        for num in nums:
            if num == m:
                cm += 1
            elif num == n:
                cn += 1
            elif cm == 0:
                m = num
                cm = 1
            elif cn == 0:
                n = num
                cn = 1
            else:
                cm -= 1
                cn -= 1
        cm = cn = 0
        for num in nums:
            if num == m:
                cm += 1
            elif num == n:
                cn += 1
        res = []
        if cm > N / 3:
            res.append(m)
        if cn > N / 3:
            res.append(n)
        return res
    
class Solution2(object):# 莫尔投票法，单个变量的,但是一定需要过n/2, [1,1,1,3,3,2,2,2,1,1],少于一半，结果是2
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = cm = 0
        for num in nums:
            if m == num:
                cm += 1
            elif cm == 0:
                m = num
                cm = 1
            else:
                cm -= 1
        return m
    def majorityElement1(self, nums):
        count, cand = 0, 0
        for num in nums:
            if num == cand:
                count += 1
            elif count == 0:
                cand, count = num, 1
            else:
                count -= 1
        return cand
    
if __name__ == "__main__":
    print(Solution2().majorityElement1([1,1,1,3,3,2,2,2,1,1]))
    print(Solution().majorityElement2([1,2,3,3,5,2,7,8,2,2,1,1,1,1,1]))


    
    
    
    
    
    

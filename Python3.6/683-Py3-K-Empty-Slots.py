# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 17:13:28 2018

@author: hjiang
"""
"""
There is a garden with N slots. In each slot, there is a flower. The N flowers will bloom one by one in N days. 
In each day, there will be exactly one flower blooming and it will be in the status of blooming since then.

Given an array flowers consists of number from 1 to N. 
Each number in the array represents the place where the flower will open in that day.

For example, flowers[i] = x means that the unique flower that blooms at day i will be at position x, 
where i and x will be in the range from 1 to N.

Also given an integer k, you need to output in which day there exists two flowers in the status of blooming, 
and also the number of flowers between them is k and these flowers are not blooming.

If there isn't such day, output -1.

Example 1:
Input: 
flowers: [1,3,2]
k: 1
Output: 2
Explanation: In the second day, the first and the third flower have become blooming.
Example 2:
Input: 
flowers: [1,2,3]
k: 1
Output: -1
Note:
The given array will be in the range [1, 20000].

 Time:  O(n)
 Space: O(n)

https://blog.csdn.net/magicbean2/article/details/79235465
"""

class Solution(object):
    def kEmptySlots(self, flowers, k): # 原题意是flowers[i] = x, 第i天开第x位置的花
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        days = [0] * len(flowers)
        for i in range(len(flowers)):
            days[flowers[i]-1] = i # 改换顺序，从零开始， day[x] = i 表示 第x位置的花第i天开
        result = float("inf")
        i, left, right = 0, 0, k+1
        while right < len(days):
            #重点， 对于位置间隔是k来说，就是要找一个k子区间[left, left + 1, ...left + k - 1, right)
            #对于任意的i = left + 1,...left + k - 1，满足days[left] < days[i] && days[right] < days[i]。中间的数字要大于day[left]和day[right]的数字
            if days[i] < days[left] or days[i] <= days[right]:# 这个地方实际上是找不符合要求的，除了等于（等于是符合要求的）
                if i == right: #关键就是这个等于，等于表示找到了
                    result = min(result, max(days[left], days[right])) #如果是等于，那么两个值days[left],days[right]取较大的即可
                left, right = i, k+1+i # 左右两个指针是一定指向间隔为k个位置的两朵花，这里表示找不到符合题意的就移动窗口
            i += 1 # i 在左右两个指针之间搜索
        return -1 if result == float("inf") else result+1 #把之前的-1改回来
    
    
if __name__ == "__main__":
    print(Solution().kEmptySlots([1,3,2],1))
    print(Solution().kEmptySlots([1,2,3],1))    
    
    
    
    
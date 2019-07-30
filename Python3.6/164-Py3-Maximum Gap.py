# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 13:43:18 2019

@author: hjiang
"""

"""
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Return 0 if the array contains less than 2 elements.

Example 1:

Input: [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either
             (3,6) or (6,9) has the maximum difference 3.
Example 2:

Input: [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
Note:

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
Try to solve it in linear time/space.
"""

#http://www.cnblogs.com/grandyang/p/4234970.html
"""
遇到这类问题肯定先想到的是要给数组排序，但是题目要求是要线性的时间和空间，那么只能用桶排序或者基排序。
这里我用桶排序Bucket Sort来做，首先找出数组的最大值和最小值，然后要确定每个桶的容量，
即为(最大值 - 最小值) / 个数 + 1，在确定桶的个数，即为(最大值 - 最小值) / 桶的容量 + 1，
然后需要在每个桶中找出局部最大值和最小值，而最大间距的两个数不会在同一个桶中，而是一个桶的最小值和另一个桶的最大值之间的间距。
代码如下：
"""
import math
class Solution:
    def maximumGap(self, num):
        if len(num) < 2 or min(num) == max(num):
            return 0
        a, b = min(num), max(num)
        size = math.ceil((b-a)/(len(num)-1))
        bucket = [[None, None] for _ in range((b-a)//size+1)]
        for n in num:
            b = bucket[(n-a)//size]#确定在哪个桶里面
            b[0] = n if b[0] is None else min(b[0], n)# 最小值
            b[1] = n if b[1] is None else max(b[1], n)#最大值
        bucket = [b for b in bucket if b[0] is not None]#除掉那些none的点
        return max(bucket[i][0]-bucket[i-1][1] for i in range(1, len(bucket))) #需要排序后的连续数之间的最大差距，所以是两个桶之间的差距（注意最大最小）
    
if __name__ == "__main__":
    print(Solution().maximumGap([3,6,9,1]))
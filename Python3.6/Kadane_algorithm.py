# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 23:01:43 2019

@author: hjiang
"""

"""
https://zh.wikipedia.org/wiki/%E6%9C%80%E5%A4%A7%E5%AD%90%E6%95%B0%E5%88%97%E9%97%AE%E9%A2%98
Kadane algorithm
查找一个序列中最接近(小于等于)k的子序列的和
使用了二分搜索。对于当前的和为sum，我们只需要找到一个最小的数x，使得 sum – k <=x，这样可以保证sum – x <=k。
"""
from bisect import bisect_left, insort_right
result = float("-inf")
k = 7
sums = [-2,1,-3,4,-1,2,1,-5,4]
accu_sum_set, accu_sum = [0], 0
for sum in sums:
    accu_sum += sum
    it = bisect_left(accu_sum_set, accu_sum - k)  # Time: O(logn)， accu_sum - k 就是 sum-k
    if it != len(accu_sum_set):
        print (sum)
        print ("accu_sum, accu_sum_set[it], accu_sum - accu_sum_set[it]:",accu_sum, accu_sum_set[it],accu_sum - accu_sum_set[it])
        result = max(result, accu_sum - accu_sum_set[it])# accu_sum_set[it]就是序列中最接近sum-k的数，这里有个减号，就是想让x最小
    insort_right(accu_sum_set, accu_sum)  # Time: O(n)
    
print(result)


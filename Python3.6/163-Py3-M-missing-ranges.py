# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 17:53:28 2018

@author: hjiang
"""

"""
Given a sorted integer array nums, where the range of elements are in the 
inclusive range [lower, upper], return its missing ranges.

Example::

Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: ["2", "4->49", "51->74", "76->99"]

这种区间的题目，要根据上下区间来操作，此题就是：
pre = lower-1
A.append(upper+1)
"""
# Time:  O(n)
# Space: O(1)

class Solution(object):
    def findMissingRanges1(self, A, lower, upper):
        result = []
        A.append(upper+1)
        pre = lower - 1
        for i in A:
           if (i == pre + 2):
               result.append(str(i-1))
           elif (i > pre + 2):
               result.append(str(pre + 1) + "->" + str(i -1))
           pre = i
        return result
    
    def findMissingRanges(self, A, lower, upper):#这个自己写的大了会内存溢出
        res = []
        all_s = set(list(range(upper + 1)))
        rest_s = list(all_s - set(A))
        i = 0
        while i < len(rest_s):
            j = i
            while (j < len(rest_s) - 1 and rest_s[j] == rest_s[j + 1] - 1):
                j += 1
            if j == i:
                res.append(str(rest_s[i]))
            else:
                res.append('%s->%s' % (str(rest_s[i]), str(rest_s[j])))
            i = j + 1
        return res
                
                
    
if __name__ == "__main__":
    print(Solution().findMissingRanges([0, 1, 3, 50, 75], 0, 99))

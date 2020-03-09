# -*- coding: utf-8 -*-
"""
Created on Tue May 28 23:35:54 2019

@author: hjiang
"""

"""
Assume you have an array of length n initialized with all 0's and are given k update operations.

Each operation is represented as a triplet: [startIndex, endIndex, inc] 
which increments each element of subarray A[startIndex ... endIndex] (startIndex and endIndex inclusive) with inc.

Return the modified array after all k operations were executed.

Example:

Input: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
Output: [-2,0,3,5,3]
Explanation:

Initial state:
[0,0,0,0,0]

After applying operation [1,3,2]:
[0,2,2,2,0]

After applying operation [2,4,3]:
[0,2,5,5,3]

After applying operation [0,2,-2]:
[-2,0,3,5,3]
https://leetcode.com/problems/range-addition/discuss/84220/O(n%2Bk)-Python-Solution
https://www.cnblogs.com/grandyang/p/5628786.html
这道题的提示说了我们肯定不能把范围内的所有数字都更新，而是只更新开头结尾两个数字就行了，
那么我们的做法就是在开头坐标startIndex位置加上inc，而在结束位置加1的地方加上-inc，
那么根据题目中的例子，我们可以得到一个数组，nums = {-2, 2, 3, 2, -2, -3}，
然后我们发现对其做累加和就是我们要求的结果result = {-2, 0, 3, 5, 3}
"""
class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        res = [0] * length
        for update in updates:
            start, end, inc = update
            res[start] += inc
            
            if end + 1 <= length - 1:
                res[end+1] -= inc

        sum = 0
        for i in range(length):
            sum += res[i]
            res[i] = sum
        return res

if __name__ == "__main__":
    updates = [[1,3,2],[2,4,3],[0,2,-2]]
    print(Solution().getModifiedArray(5, updates))
    
    
    
    
    
    
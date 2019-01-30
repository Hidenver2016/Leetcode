# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 13:36:07 2019

@author: hjiang
"""

"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
"""
# Time:  O(n^2)
# Space: O(k)

class Solution(object):
    # @return a list of integers
    def getRow(self, rowIndex):
        result = [0] * (rowIndex + 1)
        for i in range(rowIndex + 1):
            old = result[0] = 1
            for j in range(1, i + 1):
                old, result[j] = result[j], old + result[j]
        return result

    def getRow2(self, rowIndex):#这个好，一次可以解两问（118 & 119）
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        res = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip(row + [0], [0] + row)]# 这个顺序没关系， [0] + row， row + [0]也可以，因为前面操作是“+”
            res.append([row])
        return row, res
    
if __name__ == "__main__":
    print(Solution().getRow2(4))
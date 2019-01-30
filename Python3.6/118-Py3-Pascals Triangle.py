# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 23:52:59 2019

@author: hjiang
"""
'''
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],             110
   [1,2,1],            011
  [1,3,3,1],
 [1,4,6,4,1]
]
'''
# Time:  O(n^2)
# Space: O(1)

class Solution(object):
    # @return a list of lists of integers
    def generate(self, numRows):
        result = []
        for i in range(numRows):
            result.append([])
            for j in range(i + 1):
                if j in (0, i):#对于第i行， 第0个和第i个都是要置1的
                    result[i].append(1)
                else:
                    result[i].append(result[i - 1][j - 1] + result[i - 1][j])#中间i,j位置的等于上一行的i-1,j-1和i-1,j之和
        return result

#explanation: Any row can be constructed using the offset sum of the previous row. Example:
#    1 3 3 1 0 
# +  0 1 3 3 1
# =  1 4 6 4 1

    def generate2(self, numRows):
        if not numRows: return []
        res = [[1]]
        for i in range(1, numRows):
            res += [list(map(lambda x, y: x + y, res[-1] + [0], [0] + res[-1]))]
        return res
    
if __name__ == "__main__":
    print(Solution().generate2(5))
    
    
    
    
    
    
    
    
    
    
    
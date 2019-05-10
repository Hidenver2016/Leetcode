# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 15:16:44 2018

@author: hjiang
"""

"""
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","1","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6

The solution is based on largest rectangle in histogram solution. 
Every row in the matrix is viewed as the ground with some buildings on it. 
The building height is the count of consecutive 1s from that row to above rows. 
The rest is then the same as this solution for largest rectangle in histogram
关键：此题比较难，技巧比较多。注意高度是随每行的遍历而累加，
此题需要和84题联合看，区别就是每一行row的height是活的


https://leetcode.com/problems/maximal-rectangle/discuss/29065/AC-Python-DP-solutioin-120ms-based-on-largest-rectangle-in-histogram

第一， 把每一行作为“地板”，不为零的数字作为高度（实际是宽度，但这里写成height），注意是累加高度，中间一旦有零就要断开
第二，用i遍历列，当height发生下降的时候计算之前的最大矩形面积
84，85，42都一起看看
"""

class Solution1:   
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix[0])
        height = [0] * (n + 1)# 此处有一个技巧，最后专门多一位0，让接下来的height[stack[-1]]在最后总是0（height的最后一位是零）
        ans = 0
        for row in matrix:# 把每一行作为地，上面的列就是height
            for i in range(n):#对于每一列来说
                height[i] = height[i] + 1 if row[i] == '1' else 0 #此处是累加高度，一旦中间有零，height直接归零
            stack = [-1]
            for i in range(n + 1):#
                while height[i] < height[stack[-1]]:#当出现平地时，（平地位置为i），计算building的面积，逐个计算
                    h = height[stack.pop()]#弹出当前的
                    w = i - 1 - stack[-1]#计算宽度则用下一个
                    ans = max(ans, h * w)#
                stack.append(i)
        return ans
    


if __name__ == "__main__":
    A = [["1","1","1","0","0"],
         ["1","0","1","1","1"],
         ["1","1","1","1","1"],
         ["1","0","0","1","0"]]
    print(Solution1().maximalRectangle(A))

# Time:  O(n^2)
# Space: O(n)
# DP solution.

#class Solution2(object):
#    def maximalRectangle(self, matrix):
#        """
#        :type matrix: List[List[str]]
#        :rtype: int
#        """
#        if not matrix:
#            return 0
#
#        result = 0
#        m = len(matrix)
#        n = len(matrix[0])
#        L = [0 for _ in range(n)]
#        H = [0 for _ in range(n)]
#        R = [n for _ in range(n)]
#
#        for i in range(m):
#            left = 0
#            for j in range(n):
#                if matrix[i][j] == '1':
#                    L[j] = max(L[j], left)#最靠右的
#                    H[j] += 1 #高度增加
#                else:
#                    L[j] = 0
#                    H[j] = 0
#                    R[j] = n
#                    left = j + 1
#
#            right = n
#            for j in reversed(range(n)):
#                if matrix[i][j] == '1':
#                    R[j] = min(R[j], right)#最靠左的
#                    result = max(result, H[j] * (R[j] - L[j]))
#                else:
#                    right = j
#
#        return result

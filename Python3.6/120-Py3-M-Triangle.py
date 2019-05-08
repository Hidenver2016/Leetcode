# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 17:00:17 2018

@author: hjiang
"""

"""
Given a triangle, find the minimum path sum from top to bottom. 
Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, 
where n is the total number of rows in the triangle.

"""

# Modify the original triangle, bottom-up 这个题目要反着来，从下面往上
# 递推公式minpath[k][i] = min( minpath[k+1][i], minpath[k+1][i+1]) + triangle[k][i]; 此处需要注意三角形的序号特点：
#[
#     [0],
#    [0,1],
#   [0,1,2],
#  [0,1,2,3]
#]
# 由于要求是in-place所以此题直接改了triangle中的数据
#
def minimumTotal(self, triangle):#inplace,good!
    if not triangle:
        return 
    for i in range(len(triangle)-2, -1, -1):# 行,倒数第二行开始到顶
        for j in range(len(triangle[i])):# 列（第几个）
            triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
    return triangle[0][0]#因为是从后往前算，所以答案就是第一个


# bottom-up, O(n) space，额外开了n个space
def minimumTotal1(self, triangle):
    if not triangle:
        return 
    res = triangle[-1]
    for i in range(len(triangle)-2, -1, -1):
        for j in range(len(triangle[i])):
            res[j] = min(res[j], res[j+1]) + triangle[i][j]# 此处是行号其实没什么用，就直接去掉了
    return res[0]
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 14:27:47 2019

@author: hjiang
"""

"""
There are a row of n houses, each house can be painted with one of the k colors. 
The cost of painting each house with a certain color is different. 
You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x k cost matrix. 
For example, costs[0][0] is the cost of painting house 0 with color 0; 
costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Example:

Input: [[1,5,3],[2,9,4]]
Output: 5
Explanation: Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5; 
             Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5. 
Follow up:
Could you solve it in O(nk) runtime?
"""
# Time:  O(n * k)
# Space: O(k)
#import functools.reduce as reduce
#class Solution(object):
#    def minCostII(self, costs):
#        """
#        :type costs: List[List[int]]
#        :rtype: int
#        """
#        return min(reduce(self.combine, costs)) if costs else 0
#
#    def combine(self, tmp, house):
#        smallest, k, i = min(tmp), len(tmp), tmp.index(min(tmp))
#        tmp, tmp[i] = [smallest] * k, min(tmp[:i] + tmp[i+1:])
#        return map(sum, zip(tmp, house))
"""
https://leetcode.com/problems/paint-house-ii/discuss/69521/Python-O(nk)-beat-95-solution-with-explaination    
This is a Markov Chain (dp) with k states (color 1, color 2...color k) and n stages, 
we simply update the costs matrix to keep track of the optimal value for each state at current stage.
min1 means we paint all other states with the minimum cost, 
while min2 means we cannot paint consecutive houses with same color so we choose the second lowest cost to add up with.
http://www.cnblogs.com/grandyang/p/5322870.html 
这题的解法的思路还是用DP，但是在找不同颜色的最小值不是遍历所有不同颜色，
而是用min1和min2来记录之前房子的最小和第二小的花费的颜色，
如果当前房子颜色和min1相同，那么我们用min2对应的值计算，反之我们用min1对应的值，
这种解法实际上也包含了求次小值的方法

这个题目不同之处就是颜色数不确定，需要调整
这个题目和256非常相似，因为颜色数不确定，所以有两个选择：
第一，前一个房子颜色最便宜min1，
第二，除掉最便宜的，次便宜的min2
第三，下一个房子全部更新，注意如果当前房子颜色和min1相同，那么我们用min2对应的值计算，反之我们用min1对应的值
"""
# Time:  O(n * k)   
class Solution1(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs: return 0
        n, k = len(costs), len(costs[0])
        for i in range(1, n):
            min1 = min(costs[i-1])
            idx = costs[i-1].index(min1)
            min2 = min(costs[i-1][:idx] + costs[i-1][idx+1:])# 除掉idx最小的, 括号里的表达式就是除掉idx
            for j in range(k):
                if j == idx:
                    costs[i][j] += min2
                else:
                    costs[i][j] += min1
        return min(costs[-1])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
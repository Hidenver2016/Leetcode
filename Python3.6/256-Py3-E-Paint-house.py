# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 13:50:04 2019

@author: hjiang
"""

"""
There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. 
The cost of painting each house with a certain color is different. 
You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. 
For example, costs[0][0] is the cost of painting house 0 with color red; 
costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Example:

Input: [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue. 
             Minimum cost: 2 + 5 + 3 = 10.
             
             
其中dp[i][j]表示刷到第 i+1 房子用颜色 j 的最小花费
dp[i][j] = dp[i][j] + min(dp[i - 1][(j + 1) % 3], dp[i - 1][(j + 2) % 3])；
https://www.cnblogs.com/grandyang/p/5319384.html             
"""

# Time:  O(n)
# Space: O(n)？觉得是1
class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0

        n = len(costs)#有多少个房子要刷
        for i in range(1, n):
            costs[i][0] += min(costs[i - 1][1], costs[i - 1][2])
            costs[i][1] += min(costs[i - 1][0], costs[i - 1][2])
            costs[i][2] += min(costs[i - 1][0], costs[i - 1][1])

        return min(costs[n - 1])#此时已经将所有组合（分组最小）算出，直接求最小即可 min([21, 10, 37]) = 10
    
    def minCost1(self, costs):#另一种形式，可以应对多个颜色的情况,我写的这个
        if not costs: return 0
        n = len(costs)#房子数
        m = len(costs[0])#颜色数
        for i in range(1, n):
            for j in range(m):
                costs[i][j] = costs[i][j] + min(costs[i-1][(j+1)%3], costs[i-1][(j+2)%3])
        return min(costs[n-1])

if __name__ == "__main__":
    Input = [[17,2,17],[16,16,5],[14,3,19]]
    print(Solution().minCost1(Input))
    
    
    
    
    
    
    
    
    
    
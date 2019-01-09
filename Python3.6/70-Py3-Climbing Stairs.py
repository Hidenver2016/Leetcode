# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 14:14:34 2018

@author: hjiang
"""

"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
分析：假设梯子有n层，那么如何爬到第n层呢，因为每次只能怕1或2步，那么爬到第n层的方法要么是从第n-1层一步上来的，
要不就是从n-2层2步上来的，所以递推公式非常容易的就得出了：dp[n] = dp[n-1] + dp[n-2]。(这里非常关键，因为在n时，只有两种选择)
可以用递归直接求解，但是递归方法超时，这里用dp方法：
"""
class Solution(object):
    """
    :type n: int
    :rtype: int
    """
    # Time:  O(n)
    # Space: O(1)
#    def climbStairs(self, n):
#        prev, current = 0, 1
#        for i in range(n):
#            prev, current = current, prev + current,
#        return current
    #Top down
    # Time:  O(2^n) 传统递归方法的时间复杂度，具体计算参看https://www.cnblogs.com/mozi-song/p/9615167.html（中间部分）
    # Space: O(n)
    def climbStairs1(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs1(n - 1) + self.climbStairs1(n - 2)
     
    # Bottom up, O(n) space
    # Time: O(n)
    # Space: O(n)
    def climbStairs2(self, n):
        if n == 1:
            return 1
        res = [0 for i in range(n)]
        res[0], res[1] = 1, 2
        for i in range(2, n):
            res[i] = res[i-1] + res[i-2]
        return res[-1]
    
if __name__ == "__main__":
    print(Solution().climbStairs1(5))
    
    
    
    
    
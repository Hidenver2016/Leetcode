# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 18:02:54 2019

@author: hjiang
"""

"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""
# Time:  O(n)
# Space: O(1)

"""
一定要先卖了才可以买，要不是[3,3,5,0,0,3,1,4]可以先买两个0,然后3，4再卖，结果是7
"""
#class Solution(object):
#    # @param prices, a list of integer
#    # @return an integer
#    def maxProfit(self, prices):
#        hold1, hold2 = float("-inf"), float("-inf")
#        release1, release2 = 0, 0
#        for i in prices: #Assume we only have 0 money at first
#            release2 = max(release2, hold2 + i)#The maximum if we've just sold 2nd stock so far.
#            hold2 = max(hold2, release1 - i)#The maximum if we've just buy  2nd stock so far.
#            release1 = max(release1, hold1 + i)#The maximum if we've just sold 1nd stock so far.
#            hold1 = max(hold1, -i)#The maximum if we've just buy  1st stock so far. 
#        return release2 #Since release1 is initiated as 0, so release2 will always higher than release1.
    
#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/39611/Is-it-Best-Solution-with-O(n)-O(1).
#normal order of "buy first -> sell first -> buy second -> sell second" may be easier to understand.
class Solution0:#这个最容易理解，其实也是动态规划
    def maxProfit(self, prices):
        b1, b2 = float('-inf'), float('-inf')
        s1, s2 = 0, 0
        for p in prices:
            b1 = max(b1, - p)# 买
            s1 = max(s1, b1 + p)#卖
            b2 = max(b2, s1 - p)
            s2 = max(s2, b2 + p)
            
        return s2
    
    
#http://www.cnblogs.com/grandyang/p/4281975.html
#https://blog.csdn.net/fuxuemingzhu/article/details/84640318
        
class Solution1(object):#用这个，还可以当成第四问188的解
    def maxProfit(self, k, prices):#这个是可以当成123第三问的解的
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k <= 0 or not prices: return 0
        N = len(prices)
        if k >= N:
            _sum = 0
            for i in range(1, N):
                if prices[i] > prices[i - 1]:
                    _sum += prices[i] - prices[i - 1]
            return _sum
        g = [0] * (k + 1)#global
        l = [0] * (k + 1)#local
        for i in range(N - 1):
            diff = prices[i + 1] - prices[i]
            for j in range(k, 0, -1):
                l[j] = max(g[j - 1] + max(diff, 0), l[j] + diff)#最后一次交易在最后一天卖出的最大利润，此为局部最优
                g[j] = max(l[j], g[j])#累积的最优
        return g[-1]    
    
class Solution2(object):#动态规划，太难了，但是可以解任意次交易
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        N = len(prices)
        k = 3#交易两次就取3，因为开始是0.
        g = [[0] * k for _ in range(N)]
        l = [[0] * k for _ in range(N)]
        for i in range(1, N):
            diff = prices[i] - prices[i - 1]
            for j in range(1, k):
                l[i][j] = max(g[i - 1][j - 1] + max(diff, 0), l[i - 1][j] + diff)
                g[i][j] = max(l[i][j], g[i - 1][j])
        return g[-1][-1]


if __name__ == "__main__":
    print(Solution0().maxProfit([3,3,5,0,0,3,1,4]))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
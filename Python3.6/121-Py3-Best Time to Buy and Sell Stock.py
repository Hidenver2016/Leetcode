# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 18:00:32 2019

@author: hjiang
"""

"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction 
(i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

"""
遍历一次就可以了，但是需要注意顺序
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        N = len(prices)
        res = 0
        minP, maxP = float("inf"), 0
        for i in range(N):
            if minP > prices[i]:
                minP = prices[i]
                maxP = 0
            if maxP < prices[i]:
                maxP = prices[i]
            res = max(res, maxP - minP)
        return res
    
'''
只需要遍历一次数组，用一个变量记录遍历过数中的最小值，然后每次计算当前值和这个最小值之间的差值最为利润，
然后每次选较大的利润来更新。当遍历完成后当前利润即为所求，
还是有顺序的，要先算最小值
'''
# Time:  O(n)
# Space: O(1)

class Solution1(object):#这个比较好理解
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        max_profit, min_price = 0, float("inf")
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit
    
if __name__ == "__main__":
    print(Solution().maxProfit([7,1,5,3,6,4]))



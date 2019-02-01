# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 14:33:52 2019

@author: hjiang
"""

"""
Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i; 
and a non-negative integer fee representing a transaction fee.

You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction. 
You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)

Return the maximum profit you can make.

Example 1:
Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
Buying at prices[0] = 1
Selling at prices[3] = 8
Buying at prices[4] = 4
Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
Note:

0 < prices.length <= 50000.
0 < prices[i] < 50000.
0 <= fee < 50000.
"""
#https://blog.csdn.net/fuxuemingzhu/article/details/79888528

"""
可以使用dp的方法去做。该dp使用了两个数字，cash和hold。解释如下：

cash 该天结束手里没有股票的情况下，已经获得的最大收益
hold 该天结束手里有股票的情况下，已经获得的最大收益
所以转移状态分析如下：

cash 更新的策略是：既然今天结束之后手里没有股票，那么可能是今天没买（保持昨天的状态），也可能是今天把股票卖出了

hold 更新的策略是：今天今天结束之后手里有股票，那么可能是今天没卖（保持昨天的状态），也可能是今天买了股票
"""
class Solution:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        cash = 0
        hold = -prices[0]
        for i in range(1, len(prices)):
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, cash - prices[i])
        return cash

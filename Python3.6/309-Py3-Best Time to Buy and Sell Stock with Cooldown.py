# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 18:05:15 2019

@author: hjiang
"""

"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. 
You may complete as many transactions as you like 
(ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]
"""
#https://blog.csdn.net/fuxuemingzhu/article/details/82656899

"""
cash 该天结束手里没有股票的情况下，已经获得的最大收益
hold 该天结束手里有股票的情况下，已经获得的最大收益
状态转移方程式这样的：

cash[i]代表的是手里没有股票的收益，这种可能性是今天卖了或者啥也没干。
max(昨天手里有股票的收益+今天卖股票的收益，昨天手里没有股票的收益)， 即max(cash[i - 1], hold[i - 1] + prices[i])；

hold[i]代表的是手里有股票的收益，这种可能性是今天买了股票或者啥也没干，今天买股票必须昨天休息。
所以为max(今天买股票是前天卖掉股票的收益-今天股票的价格，昨天手里有股票的收益）。即max(hold[i - 1], cash[i - 2] - prices[i])。

另外需要注意的是，题目说的是昨天卖了股票的话今天不能买，对于开始的第一天，不可能有卖股票的行为，所以需要做个判断。

该算法的时间复杂度是O(n)，空间复杂度是O(n)。
"""
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        cash = [0] * len(prices)
        hold = [0] * len(prices)
        hold[0] = -prices[0]
        for i in range(1, len(prices)):
            cash[i] = max(cash[i - 1], hold[i - 1] + prices[i])
            hold[i] = max(hold[i - 1], (cash[i - 2] if i >= 2 else 0) - prices[i])
        return cash[-1]
    
if __name__ == "__main__":
    print(Solution().maxProfit([1,2,3,0,2]))
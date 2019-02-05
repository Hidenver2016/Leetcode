# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 18:04:10 2019

@author: hjiang
"""

"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:

Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
"""
#https://blog.csdn.net/fuxuemingzhu/article/details/84671154

class Solution(object):
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
        g = [0] * (k + 1)
        l = [0] * (k + 1)
        for i in range(N - 1):
            diff = prices[i + 1] - prices[i]
            for j in range(k, 0, -1):
                l[j] = max(g[j - 1] + max(diff, 0), l[j] + diff)#最后一次交易在最后一天卖出的最大利润，此为局部最优
                g[j] = max(l[j], g[j])#累积的最优
        return g[-1]
    
    def maxProfit1(self,k, prices):#这个方法是可以解，但是下面这个二维数组会在k变大的时候崩溃，所以只能参考上面那个解
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        N = len(prices)
        k1 = k+1#交易两次就取3，因为开始是0.
        g = [[0] * k1 for _ in range(N)]
        l = [[0] * k1 for _ in range(N)]
        for i in range(1, N):
            diff = prices[i] - prices[i - 1]
            for j in range(1, k1):
                l[i][j] = max(g[i - 1][j - 1] + max(diff, 0), l[i - 1][j] + diff)
                g[i][j] = max(l[i][j], g[i - 1][j])
        return g[-1][-1]
    
if __name__ == "__main__":
    print(Solution().maxProfit1(2, [3,2,6,5,0,3]))
    
    
    
    
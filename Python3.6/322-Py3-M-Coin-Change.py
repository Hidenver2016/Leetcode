# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 11:37:31 2019

@author: hjiang
"""

"""
You are given coins of different denominations and a total amount of money amount. 
Write a function to compute the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
"""
# Time:  O(n * k), n is the number of coins, k is the amount of money
# Space: O(k)

class Solution(object):#这个超时了，但是思路很清楚，用这个回答也可以
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        INF = 0x7fffffff  # Using float("inf") would be slower.
        amounts = [INF] * (amount + 1)
        amounts[0] = 0
        for i in range(amount + 1):
            if amounts[i] != INF:
                for coin in coins:
                    if i + coin <= amount:
                        amounts[i + coin] = min(amounts[i + coin], amounts[i] + 1)
        return amounts[amount] if amounts[amount] != INF else -1
    
    
#Assume dp[i] is the fewest number of coins making up amount i, then for every coin in coins, dp[i] = min(dp[i - coin] + 1).
#
#The time complexity is O(amount * coins.length) and the space complexity is O(amount)
#https://leetcode.com/problems/coin-change/discuss/77372/Clean-dp-python-code
class Solution1(object):
    def coinChange(self, coins, amount):
        MAX = float('inf')
        dp = [0] + [MAX] * amount

        for i in range(1, amount + 1):
            dp[i] = min([dp[i - c] if i - c >= 0 else MAX for c in coins]) + 1

#        return [dp[amount], -1][dp[amount] == MAX]
        if dp[amount] == MAX: return -1
        else: return dp[amount] 
    
if __name__ == "__main__":
    print(Solution1().coinChange([1,2,5], 11))
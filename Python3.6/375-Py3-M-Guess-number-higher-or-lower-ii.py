# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 22:21:10 2018

@author: hjiang
"""

"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.

However, when you guess a particular number x, and you guess wrong, you pay $x. 
You win the game when you guess the number I picked.

Example:

n = 10, I pick 8.

First round:  You guess 5, I tell you that it's higher. You pay $5.
Second round: You guess 7, I tell you that it's higher. You pay $7.
Third round:  You guess 9, I tell you that it's lower. You pay $9.

Game over. 8 is the number I picked.

You end up paying $5 + $7 + $9 = $21.
Given a particular n ≥ 1, find out how much money you need to have to guarantee a win.


https://www.cnblogs.com/zichi/p/5701194.html
http://www.cnblogs.com/grandyang/p/5677550.html
这是一道很典型的动态规划题，你根本不可能去盲目地猜，然后使劲地暴力递归去解！
这样的复杂度是指数级的。是否能够递推求解？比如已经知道 n 为 1-5 的情况，
当 n 为 6 时，第一次猜，我们可以有 6 种猜法，分别选择 1,2,3,4,5 和 6，

我们以猜 3 为例，比如说第一把猜了 3，那么如果猜的大了，
那么我们接下去要求的是从 [1, 2] 中猜到正确数字所需要花费的最少 money，记为 x，
如果猜的小了，那么我们接下去要求的是从 [4, 6] 中猜到正确数字所需要花费的最少 money，记为 y，
如果刚好猜中，则结束。

很显然，如果第一把猜 3，那么猜中数字至少需要花费的 money 为 
3 + max(x, y, 0)，"至少需要的花费"，就要我们 "做最坏的打算，尽最大的努力"，即取最大值。
这是第一把取 3 的情况，我们还需要考虑其他 5 种情况，然后六种情况再取个最小值，
就是 n=6 至少需要的 money！（想想，是不是这样？）

https://leetcode.com/problems/guess-number-higher-or-lower-ii/discuss/84769/Two-Python-solutions
To find out how much money I need to win the range lo..hi (the game starts with the range 1..n), 
I try each possible x in the range (except hi, which is pointless because hi-1 costs less 
and provides more information), calculate how much I need when using that x, 
and take the minimum of those amounts.

计算局部最大值local_max = k + max(dp[j][k - 1], dp[k + 1][i])，这个正好是将该区间在每一个位置都分为两段，
然后取当前位置的花费加上左右两段中较大的花费之和为局部最大值，为啥要取两者之间的较大值呢，
因为我们要cover所有的情况，就得取最坏的情况， 然后更新全局最小值。

那么我们的策略是用k来遍历所有的数字，然后再根据k分成的左右两个区间，取其中的较大cost加上k。

Bottom-up dynamic programming:
    
# Time:  O(n^2)
# Space: O(n^2)    
        
"""

class Solution:
    def getMoneyAmount(self, n):
        dp = [[0] * (n+1) for _ in range(n+1)]# dp[i][j]表示从数字i到j之间猜中任意一个数字最少需要花费
        for lo in range(n, 0, -1):
            for hi in range(lo+1, n+1):
                dp[lo][hi] = min(x + max(dp[lo][x-1], dp[x+1][hi]) for x in range(lo, hi))# min是针对所有x的
#                print(lo, hi, dp[lo][hi])#从后往前算，从少向多算
        return dp[1][n]
    
if __name__ ==  "__main__":
    print(Solution().getMoneyAmount(10))
    
    





















    
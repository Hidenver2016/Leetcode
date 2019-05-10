# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 15:45:04 2019

@author: hjiang
"""

"""
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. 
The dungeon consists of M x N rooms laid out in a 2D grid. 
Our valiant knight (K) was initially positioned in the top-left room and 
must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. 
If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; 
other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

 

Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 
if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

-2 (K)	-3	3
-5	-10	   1
10	30	-5 (P)
 

Note:

The knight's health has no upper bound.
Any room can contain threats or power-ups, even the first room the knight enters 
and the bottom-right room where the princess is imprisoned.
http://www.cnblogs.com/grandyang/p/4233035.html
反向计算，从后到前
所以用当前房间的右边和下边房间中骑士的较小血量减去当前房间的数字，如果是负数或着0，
说明当前房间是正数，这样骑士进入当前房间后的生命值是1就行了，因为不会减血。
而如果差是正数的话，当前房间的血量可能是正数也可能是负数，但是骑士进入当前房间后的生命值就一定要是这个差值。

因为是要救公主，所以必须要在到达最后一个格子的时候生命值至少为1.所以可以考虑在最后的格子后面加上两个格子，置初始值为1

"""

#def calculateMinimumHP(self, dungeon):
#       """
#       :type dungeon: List[List[int]]
#       :rtype: int
#       """
#       
#       R, C = len(dungeon), len(dungeon[0])
#       dp = [[0] * C for _ in range(R)]
#       dp[-1][-1] = max(1 - dungeon[-1][-1], 1)
#       for i in range(R - 2, -1, -1):
#           dp[i][C - 1] = max(dp[i + 1][C - 1] - dungeon[i][C - 1], 1)
#       for i in range(C - 2, -1, -1):
#           dp[R - 1][i] = max(dp[R - 1][i + 1] - dungeon[R - 1][i], 1)
#       
#       for i in range(R - 2, -1, -1):
#           for j in range(C - 2, -1, -1):
#               # if adding health is much larger than health required, set it to 1
#               dp[i][j] = max(min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j], 1)
#       
#       return dp[0][0]
# Time: O(m*n)
# Space: O(m*n)
   
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if not dungeon: return 0
        m, n = len(dungeon), len(dungeon[0])
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)] # 这个地方多加一行一列使得在反向考虑中不用考虑边界条件
        dp[m - 1][n] = dp[m][n - 1] = 1 #那么此时公主房间的右边和下边房间里的数字我们就都设置为1， 这个地方已经搞出去了
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] = max(1, min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j])#至少要有1,要不是就挂了
        return dp[0][0]
    
if __name__ == "__main__":
    Grid = [[-2, -3, 3], [-5,-10, 1], [10, 30, -5]]
    print(Solution().calculateMinimumHP(Grid))
    
    

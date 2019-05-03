# -*- coding: utf-8 -*-
"""
Created on Thu May  2 22:30:04 2019

@author: hjiang
"""

"""
Think about Zuma Game. You have a row of balls on the table, colored red(R), yellow(Y), 
blue(B), green(G), and white(W). You also have several balls in your hand.

Each time, you may choose a ball in your hand, and insert it into the row 
(including the leftmost place and rightmost place). Then, if there is a group 
of 3 or more balls in the same color touching, remove these balls. Keep doing 
this until no more balls can be removed.

Find the minimal balls you have to insert to remove all the balls on the table. 
If you cannot remove all the balls, output -1.

Examples:

Input: "WRRBBW", "RB"
Output: -1
Explanation: WRRBBW -> WRR[R]BBW -> WBBW -> WBB[B]W -> WW

Input: "WWRRBBWW", "WRBRW"
Output: 2
Explanation: WWRRBBWW -> WWRR[R]BBWW -> WWBBWW -> WWBB[B]WW -> WWWW -> empty

Input:"G", "GGGGG"
Output: 2
Explanation: G -> G[G] -> GG[G] -> empty 

Input: "RBYYBBRRB", "YRBGB"
Output: 3
Explanation: RBYYBBRRB -> RBYY[Y]BBRRB -> RBBBRRB -> RRRB -> B -> B[B] -> BB[B] -> empty 

Note:
You may assume that the initial row of balls on the table won’t have any 3 or 
more consecutive balls with the same color.
The number of balls on the table won't exceed 20, and the string represents these 
balls is called "board" in the input.
The number of balls in your hand won't exceed 5, and the string represents these 
balls is called "hand" in the input.
Both input strings will be non-empty and only contain characters 'R','Y','B','G','W'.

https://leetcode.com/problems/zuma-game/discuss/221386/Python-DFS-16-lines-very-easy-to-understand

Time: O(n+m)^m*n^2  n=20, m=5
Space: O(m*n) m是递归深度，每次创建一个棋盘
剪枝，每次都要插能引爆的，意思就是至少插在要两个相连的球的后面
"""

class Solution:
    def findMinStep(self, board, hand):   
        def dfs(s, c):
            if not s: return 0
            res, i = float("inf"), 0
            while i < len(s):
                j = i + 1
                while j < len(s) and s[i] == s[j]: j += 1
                incr = 3 - (j - i)
                if c[s[i]] >= incr:
                    incr = 0 if incr < 0 else incr
                    c[s[i]] -= incr
                    tep = dfs(s[:i] + s[j:], c)
                    if tep >= 0: res = min(res, tep + incr)
                    c[s[i]] += incr
                i = j
            return res if res != float("inf") else -1
        return dfs(board, collections.Counter(hand))
    
    
    
    
    
    
    
    
    
    
    
    
    
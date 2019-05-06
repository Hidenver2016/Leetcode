# -*- coding: utf-8 -*-
"""
Created on Thu May  2 11:49:51 2019

@author: hjiang
"""

"""
Given several boxes with different colors represented by different positive numbers. 
You may experience several rounds to remove boxes until there is no box left. 
Each time you can choose some continuous boxes with the same color (composed of k boxes, k >= 1), 
remove them and get k*k points.
Find the maximum points you can get.

Example 1:
Input:

[1, 3, 2, 2, 2, 3, 4, 3, 1]
Output:
23
Explanation:
[1, 3, 2, 2, 2, 3, 4, 3, 1] 
----> [1, 3, 3, 4, 3, 1] (3*3=9 points) 
----> [1, 3, 3, 3, 1] (1*1=1 points) 
----> [1, 1] (3*3=9 points) 
----> [] (2*2=4 points)
Note: The number of boxes n would not exceed 100.
https://leetcode.com/problems/remove-boxes/discuss/101311/Python-Fast-DP-with-Explanation
https://www.cnblogs.com/grandyang/p/6850657.html

此题最关键就是要找出来有的子序列是需要被抽出来的： 花花的讲解，k个箱子在j右边
定义dp[i][j][k]: 最大分数b[i]~b[j],其中b[j]后面跟了k个和b[j]颜色一样的箱子
状态转移方程：
dp[i][j][k] = dp[i][j-1][0] + (k + 1)^2  # 把box[j]和后面的k个箱子组成一组，然后remove，得到(k + 1)^2
            = dp[i][p][k+1] + dp[p+1][j-1][0]  # p是一个分割点，需要遍历，i <= p < j。 子序列为 dp[p+1][j-1][0], 
                其中把b[j]就是现在的[k+1]的第一个,因为取出子序列，b[j]向前移动了。
                
                
答案的讲解：k个箱子在i左边
定义dp[i][j][k]: 最大分数b[i]~b[j],其中b[i]左边有k个和b[i]颜色一样的箱子
状态转移方程：
dp[i][j][k] = dp[i+1][j][0] + (k + 1)^2 # 把b[i]并到左边的k个箱子里面去，长度为k+1, 得到 (k + 1)^2
            = dp[i+1][m-1][0] + dp[m][j][k+1]  #这个是假设中间有一个b[m]和b[i]颜色一样，所以先抽取子序列dp[i+1][m-1][0]，
            而剩下的序列dp[m][j][k+1]和初始条件一样,k+1是d[i]和之前的k个一样的合并了。这样完成了状态方程推导
            
741 546，664，488
"""
class Solution:
    def removeBoxes(self, A):
        N = len(A)
        memo = [[[0]*N for _ in range(N) ] for _ in range(N) ]

        def dp(i, j, k):
            if i > j: return 0
            if not memo[i][j][k]:
                m = i
                while m+1 <= j and A[m+1] == A[i]:
                    m += 1
                i, k = m, k + m - i # k+m-i是计算总共多少个b[i], m-i是多了的，本来是k+m-i+1,但是下一行是(k+1)^2,所以这里不用重复+1
                ans = dp(i+1, j, 0) + (k+1) ** 2
                for m in range(i+1, j+1):
                    if A[i] == A[m]:
                        ans = max(ans, dp(i+1, m-1, 0) + dp(m, j, k+1))
                memo[i][j][k] = ans
            return memo[i][j][k]

        return dp(0, N-1, 0)
    
    
    
    
    
    
    
    
    
    
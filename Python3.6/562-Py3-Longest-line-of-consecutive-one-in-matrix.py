# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 22:00:24 2018

@author: hjiang
"""
"""
Given a 01 matrix M, find the longest line of consecutive one in the matrix. 
The line could be horizontal, vertical, diagonal or anti-diagonal.
Example:
Input:
[[0,1,1,0],
 [0,1,1,0],
 [0,0,0,1]]
Output: 3
Hint: The number of elements in the given matrix will not exceed 10,000.
http://www.cnblogs.com/grandyang/p/6900866.html
如果i是从0到m+n-1之间遍历，j是在i到0之间遍历，那么对角线的数字的坐标就为(i-j, j)，
逆对角线的坐标就为(m-1-i+j, j)，m = len(M)行数

重点： 掌握dp的方法，不用去一个个的暴力搜索，在dp中上一步的搜索结果被记住，下一次的时候直接调用

"""
# Time:  O(m * n)
# Space: O(n)

class Solution(object):#优
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M: return 0
        result = 0
        dp = [[[0] * 4 for _ in range(len(M[0]))] for _ in range(2)] # 2*len(M[0])*4，这里是至少需要两行，要不是上次的值直接被抹去了
        for i in range(len(M)):#行
            for j in range(len(M[0])):#列
                dp[i % 2][j][:] = [0] * 4# 这里是记录每次算的值，所以要每次都置零
                if M[i][j] == 1:
                    dp[i % 2][j][0] = dp[i % 2][j - 1][0]+1 if j > 0 else 1 #行，j横向运行，j增大
                    dp[i % 2][j][1] = dp[(i-1) % 2][j][1]+1 if i > 0 else 1 #列，i纵向运行，i增大
                    dp[i % 2][j][2] = dp[(i-1) % 2][j-1][2]+1 if (i > 0 and j > 0) else 1 #正对角线， i-1和j-1都是对角线  (i-1)%2是range(2)关于上一步的记忆
                    dp[i % 2][j][3] = dp[(i-1) % 2][j+1][3]+1 if (i > 0 and j < len(M[0])-1) else 1 #反对角线
#                    print(dp)
                    result = max(result, max(dp[i % 2][j]))
        return result
    
if __name__ == "__main__":
    A = [[0,1,1,0],
         [0,1,1,0],
         [0,0,0,1]]
    B = [[0,1,1,0,1,1,1,1],
         [0,1,1,0,1,0,1,0],
         [0,1,1,0,1,0,1,0],
         [0,1,1,0,1,0,1,0],
         [0,1,1,0,1,0,1,0],
         [0,1,1,0,1,0,1,0],
         [0,1,1,0,1,0,1,0],
         [0,1,1,0,1,0,1,0]]
    print(Solution().longestLine(A))
    

class Solution1(object):
    def longestLine(self, M):
        if not M: return 0
        res = 0 
        for i in range(len(M)): #行
            cnt = 0
            for j in range(len(M[0])):
                if M[i][j] == 1:
                    cnt += 1
                    res = max(res, cnt)
                else:
                    cnt = 0
        for j in range(len(M[0])): #行
            cnt = 0
            for i in range(len(M)):
                if M[i][j] == 1:
                    cnt += 1
                    res = max(res, cnt)
                else:
                    cnt = 0
        
        for i in range(len(M) + len(M[0]) - 1):#%%%%%%%%%%%%%%%%%%%%%重点
            cnt1 = 0
            cnt2 = 0
            for j in range(i, -1, -1):#%%%%%%%%%%%%%%%%%%%%%重点
                if i - j < len(M) and j < len(M[0]):
                    if M[i-j][j] == 1: # 从右上到左下
                        cnt1 += 1
                        res = max(res, cnt1)
                    else:
                        cnt1 = 0
                t = len(M) - 1 - i + j
                if t >= 0 and t < len(M) and j < len(M[0]):
                    if M[t][j] == 1: # 从坐上到右下
                        cnt2 += 1
                        res = max(res, cnt2)
                    else:
                        cnt2 = 0
        return res
    
    
    
    
    
    
    
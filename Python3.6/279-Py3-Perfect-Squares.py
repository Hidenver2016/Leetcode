# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 14:08:55 2018

@author: hjiang
"""
"""
Given a positive integer n, 
find the least number of perfect square numbers 
(for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
https://blog.csdn.net/happyaaaaaaaaaaa/article/details/51584790
http://yucoding.blogspot.com/2016/12/leetcode-question-perfect-square.html
如图所示，红色部分表示平方数，所有的完美平方数都可以看做一个普通数加上一个完美平方数，
那么递推式就变为了：dp[i + j * j] = Math.min(dp[i] + 1, dp[i + j * j])，

此题用第0中方法会超时，
"""

class Solution0:#超时
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [n] * (n+1)
        for i in range(n):
            if i*i <= n:
                dp[i*i] = 1
        
        for i in range(1, n+1):
            for j in range(i):
                if i + j*j <=n:
                    dp[i + j*j] = min(dp[i]+1, dp[i+j*j])
                    
        return dp[n]


#纯数学方法，也很快，考试还是用这个算了，不强求dp
def numSquares(n):
    if not n:
        return 0
    while n % 4 == 0:
        n /= 4
    if n % 8 == 7:
        return 4
    a = 0
    while (a ** 2) <= n:
        b = int((n - a ** 2)**0.5)
        if ((a**2) + (b**2)) == n:
            if a == 0:
                return 1
            else:
                return 2
        a += 1
    return 3


#下面这个方法比较好，看不懂
#https://leetcode.com/problems/perfect-squares/discuss/71512/Static-DP-C%2B%2B-12-ms-Python-172-ms-Ruby-384-ms
# Time:  O(n * sqrt(n))
# Space: O(n)
        
    
class Solution2(object):#此方法也超时了
    def numSquares(self, n):
        ## len(dp) = n+1 is the final
        dp = [0]
        while len(dp) <= n:
            ## x: number to be examined; dp[x] to be filled
            x = len(dp) 
            y = float('inf')
            for k in range(1, int(x**0.5 + 1)):
                ## k*k is a square-num
                substract_num = x - k * k 
                if dp[substract_num] + 1 < y:
                    y = dp[substract_num] + 1
            dp.append(y)
        return(dp[n])
        

class Solution1(object):
    _num = [0]
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = self._num
        while len(num) <= n:
            num += min(num[-i*i] for i in range(1, int(len(num)**0.5+1))) + 1,
        return num[n]

if __name__ == "__main__":
    for i in range(1, 100):
        print(Solution1().numSquares(i) == Solution0().numSquares(i))
#    print(Solution2().numSquares(13))











                  
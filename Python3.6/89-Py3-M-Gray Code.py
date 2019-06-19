# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 12:19:26 2019

@author: hjiang
"""

"""
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, 
print the sequence of gray code. A gray code sequence must begin with 0.

Example 1:

Input: 2
Output: [0,1,3,2]
Explanation:
00 - 0
01 - 1
11 - 3
10 - 2

For a given n, a gray code sequence may not be uniquely defined.
For example, [0,2,3,1] is also a valid gray code sequence.

00 - 0
10 - 2
11 - 3
01 - 1
Example 2:

Input: 0
Output: [0]
Explanation: We define the gray code sequence to begin with 0.
             A gray code sequence of n has size = 2n, which for n = 0 the size is 20 = 1.
             Therefore, for n = 0 the gray code sequence is [0].
求n位的格雷码序列。格雷码是指相邻的两个数字的二进制只会有一位不同。

简言之就是递归。第（n+1）位的格雷码序列=（‘0’+第n位的正序） + （‘1’+第n位的逆序）

题目中说了n是非负数，当n=0的时候，返回[0]即可。

所以循环版本：
"""

class Solution(object):
    def grayCode(self, n):#循环
        """
        :type n: int
        :rtype: List[int]
        """
        grays = dict()
        grays[0] = ['0']
        grays[1] = ['0', '1']
        for i in range(2, n + 1):
            n_gray = []
            for pre in grays[i - 1]:
                n_gray.append('0' + pre)
            for pre in grays[i - 1][::-1]:
                n_gray.append('1' + pre)
            grays[i] = n_gray
        return map(lambda x: int(x, 2), grays[n])#2进制


class Solution1(object):#递归
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return map(lambda x: int(x, 2), self.bit_gray(n))
    
    def bit_gray(self, n):
        ans = None
        if n == 0:
            ans = ['0']
        elif n == 1:
            ans = ['0', '1']
        else:
            pre_gray = self.bit_gray(n - 1)
            ans = ['0' + x for x in pre_gray] + ['1' + x for x in pre_gray[::-1]]
        return ans
    
if __name__ == "__main__":
    print(Solution().grayCode(2))

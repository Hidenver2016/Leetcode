# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 21:26:17 2019

@author: hjiang
"""

"""
Your task is to calculate ab mod 1337 where a is a positive integer and b 
is an extremely large positive integer given in the form of an array.

Example 1:

Input: a = 2, b = [3]
Output: 8
Example 2:

Input: a = 2, b = [1,0]
Output: 1024
https://blog.csdn.net/fuxuemingzhu/article/details/82961114
http://www.cnblogs.com/grandyang/p/5651982.html
结合50题记忆，尤其是求幂那部分
题的难点在于，如何求数组表示的超级大的数字b次幂。原来是求幂也可以做展开，
比如求223，相当于求(2^2)^10 * (2^3).也就是说把前面以求的结果求一次10次幂，然后再去求后面的幂。
"""
class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        res = 1
        for x in b:
            res = self.pow(res, 10) * self.pow(a, x) % 1337
        return res
        
    def pow(self, a, b):
        if b == 0 or a == 1: return 1
        if b % 2:
            return a * self.pow(a, b - 1) % 1337
        return self.pow((a * a) % 1337, b / 2) % 1337
    
    
#https://leetcode.com/problems/super-pow/discuss/84475/Fermat-and-Chinese-Remainder
def superPow(self, a, b):#中国余数定理
    def mod(p):
        return pow(a, reduce(lambda e, d: (10*e + d) % (p-1), b, 0), p) if a%p else 0
    return (764 * mod(7) + 574 * mod(191)) % 1337

if __name__ == "__main__":
#    print(Solution().superPow(2, [3]))
    print(Solution().superPow(2, [1,0]))
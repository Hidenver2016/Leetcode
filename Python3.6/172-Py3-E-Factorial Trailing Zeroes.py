# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 22:45:11 2019

@author: hjiang
"""

"""
Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Note: Your solution should be in logarithmic time complexity.



10 is the product of 2 and 5. In n!, we need to know how many 2 and 5, 
and the number of zeros is the minimum of the number of 2 and the number of 5.

Since multiple of 2 is more than multiple of 5, the number of zeros is dominant by the number of 5.
https://www.cnblogs.com/grandyang/p/4219878.html
求一个数的阶乘末尾0的个数，也就是要找乘数中 10 的个数，而 10 可分解为2和5，而2的数量又远大于5的数量（比如1到 10 中有2个5，5个2），
那么此题即便为找出5的个数。仍需注意的一点就是，像25,125，这样的不只含有一个5的数字需要考虑进去。
代码如下：
"""

class Solution:
    def trailingZeroes(self, n):
        return 0 if n == 0 else n // 5 + self.trailingZeroes(n // 5)

if __name__ == "__main__":
    print(Solution().trailingZeroes(40))
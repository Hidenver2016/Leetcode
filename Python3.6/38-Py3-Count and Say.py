# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 15:53:24 2019

@author: hjiang
"""

"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

 

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
这个东西的输入只是一个index，实际上是找数列的规律，数列就在上面
开始为1，第1个数就是1个1，即11，第2个数就是2个1，即21，第3个数是1个2,1个1，即1211.
第4个数是1个1,1个2，2个1，即111221。每次后面的数都是对前面一个数的“数”和“说”。现在让你求第n个数是什么？
https://leetcode.com/problems/count-and-say/discuss/16044/Simple-Python-Solution
"""
class Solution(object):
    
    def countAndSay(self, n):
        result = '1'
        for _ in range(n-1):
            prev = result#承接上一次计算的值
            result = ''
            j = 0
            while j < len(prev):
                cur = prev[j]
                cnt = 1
                j += 1
                while j < len(prev) and prev[j] == cur:
                    cnt += 1 #当前数计数
                    j += 1 #总体向后偏移
                result += str(cnt) + str(cur)
        return result

if __name__ == "__main__":
    print(Solution().countAndSay(20))
    
    
    
    
    
    
    
    
    
    
    
    
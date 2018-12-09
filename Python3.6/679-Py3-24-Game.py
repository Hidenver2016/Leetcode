# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 11:34:39 2018

@author: hjiang
"""

"""
You have 4 cards each containing a number from 1 to 9. 
You need to judge whether they could operated through *, /, +, -, (, ) to get the value of 24.

Example 1:
Input: [4, 1, 8, 7]
Output: True
Explanation: (8-4) * (7-1) = 24
Example 2:
Input: [1, 2, 1, 2]
Output: False
Note:
The division operator / represents real division, not integer division. For example, 4 / (1 - 2/3) = 12.
Every operation done is between two numbers. In particular, we cannot use - as a unary operator. 
For example, with [1, 1, 1, 1] as input, the expression -1 - 1 - 1 - 1 is not allowed.
You cannot concatenate numbers together. For example, if the input is [1, 2, 1, 2], 
we cannot write this as 12 + 12.
"""
    
from operator import add, sub, mul, truediv
#from fractions import Fraction

#http://www.cnblogs.com/grandyang/p/8395062.html  可以考虑如何把所有的等式都列出来
# Time:  O(n^3 * 4^n) = O(1), n = 4
# Space: O(n^2) = O(1)
class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return abs(nums[0]-24) < 1e-6
        ops = [add, sub, mul, truediv]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:#一样的跳过
                    continue
                next_nums = [nums[k] for k in range(len(nums)) if i != k != j]#取两个
                for op in ops:# 注意第一个条件是因为饿加法和乘法有交换律，只需要算j<i的情况就可以了，第二个是不能除零
                    if ((op is add or op is mul) and j > i) or (op == truediv and nums[j] == 0):
                        continue
                    next_nums.append(op(nums[i], nums[j]))
                    if self.judgePoint24(next_nums): #每次DP都会少一个数,最后就是看next_nums[0]是不是等于24
                        return True
                    next_nums.pop()#计算不对的数要弹出
        return False
    

    
if __name__ == "__main__":
    print(Solution().judgePoint24([4,1,8,7]))
    
    
    
    
    
    
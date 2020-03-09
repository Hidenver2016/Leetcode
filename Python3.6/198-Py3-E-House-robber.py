# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 11:12:04 2019

@author: hjiang
"""

"""
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, the only constraint stopping you 
from robbing each of them is that adjacent houses have security system connected 
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, 
determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.

×××××××××××××××××××××斐波那契×××××××××××××××××××××××××××
×××××××××××××××××××××方法一×××××××××××××××××××××××××××××
             
def Fibonacci_Loop(n):
    result_list = []
    a, b = 0, 1
    while n > 0:
        result_list.append(b)
        a, b = b, a + b
        n -= 1
    return result_list
————————————————
版权声明：本文为CSDN博主「Font Tian」的原创文章，遵循 CC 4.0 BY-NC-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/FontThrone/article/details/78429771
××××××××××××××××××××方法二×××××××××××××××××××××××××××××××
def Fibonacci_Yield_tool(n):
    a, b = 0, 1
    while n > 0:
        yield b
        a, b = b, a + b
        n -= 1


def Fibonacci_Yield(n):
    # return [f for i, f in enumerate(Fibonacci_Yield_tool(n))]
    return list(Fibonacci_Yield_tool(n))
————————————————
版权声明：本文为CSDN博主「Font Tian」的原创文章，遵循 CC 4.0 BY-NC-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/FontThrone/article/details/78429771             
"""
# Time:  O(n)
# Space: O(1)

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last, now = 0, 0
        for i in nums:
            last, now = now, max(last + i, now)#这一句非常精华，只能记住
        return now

# Time:  O(n)
# Space: O(n)
    
class Solution1(object):#这个思路比较清楚
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) <= 2:
            return max(nums[0], nums[-1])
        dp = [0]*len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])# 关键递推关系在这里，当前的要不就采用并且和i-2一起（nums[i]+dp[i-2]），要不就是dp[i-1]
        return dp[-1]
    
    
    
    
    
    
    
    
    
    
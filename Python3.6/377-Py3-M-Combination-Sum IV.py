# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 16:45:00 2019

@author: hjiang
"""

"""
Given an integer array with all positive numbers and no duplicates, 
find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.
https://blog.csdn.net/fuxuemingzhu/article/details/79343825
https://zxi.mytechroad.com/blog/dynamic-programming/leetcode-377-combination-sum-iv/
http://www.cnblogs.com/grandyang/p/5705750.html
对于每一个数i，遍历nums数组，如果i>=x, dp[i] += dp[i - x]。
这个也很好理解，比如说对于[1,2,3] 4，这个例子，
当我们在计算dp[3]的时候，3可以拆分为1+x，而x即为dp[2]，3也可以拆分为2+x，
此时x为dp[1]，3同样可以拆为3+x，此时x为dp[0]，我们把所有的情况加起来就是组成3的所有情况了

[1,2,3] 4，
1. 取1，然后用[1,2,3] 组成3
2. 取2，然后用[1,2,3] 组成2
3. 取3，然后用[1,2,3] 组成1
最后把这些情况全部加起来！之所以不算前面取的1，2，3的组合，是因为算了就重复了！
"""

class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
        return dp[-1]

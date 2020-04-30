# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 11:50:46 2019

@author: hjiang
"""

"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""





"""
https://leetcode.com/problems/longest-consecutive-sequence/discuss/41057/Simple-O(n)-with-Explanation-Just-walk-each-streak
First turn the input into a set of numbers. That takes O(n) and then we can ask in O(1) whether we have a certain number.

Then go through the numbers. If the number x is the start of a streak (i.e., x-1 is not in the set), 
then test y = x+1, x+2, x+3, ... and stop at the first number y not in the set. 
The length of the streak is then simply y-x and we update our global best with that. 
Since we check each streak only once, this is overall O(n). 
This ran in 44 ms on the OJ, one of the fastest Python submission
"""

"""
本题复盘， 第一变成set，节省查找时间
第二，那个x-1和y+1的技巧
"""

def longestConsecutive(self, nums):#看这个
    nums = set(nums)
    best = 0
    for x in nums:
        if x - 1 not in nums:
            y = x + 1
            while y in nums:#这个是亮点，只要是y在，就不停的数
                y += 1
            best = max(best, y - x)#可能有好多组连续的数，这里是选择最长的那一组
    return best

def longestConsecutive1(self, nums):#类似的想法，remove能过，那估计就是O(1)
    res, left = 0, set(nums)
    while left:
        l = r = left.pop()
        while l - 1 in left: left.remove(l - 1); l -= 1;
        while r + 1 in left: left.remove(r + 1); r += 1;
        res = max(res, r - l + 1)
    return res
















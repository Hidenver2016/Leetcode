# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 00:54:28 2020

@author: hjiang
"""

"""
Given an array nums sorted in ascending order, return true if and only if you 
can split it into 1 or more subsequences such that each subsequence consists of 
consecutive integers and has length at least 3.

 

Example 1:

Input: [1,2,3,3,4,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3
3, 4, 5

Example 2:

Input: [1,2,3,3,4,4,5,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3, 4, 5
3, 4, 5

Example 3:

Input: [1,2,3,4,4,5]
Output: False

思路
I used a greedy algorithm.
left is a hashmap, left[i] counts the number of i that I haven't placed yet.
end is a hashmap, end[i] counts the number of consecutive subsequences that ends at number i
Then I tried to split the nums one by one.
If I could neither add a number to the end of a existing consecutive subsequence nor find two following number in the left, I returned False
"""
import collections
class Solution:
    def isPossible(self, nums):
            left = collections.Counter(nums)#表示有多少数字没放置
            end = collections.Counter()#表示有多少数字以i结束
            for i in nums:
                if not left[i]: continue
                left[i] -= 1# 试图把i放在某一个队列里面
                if end[i - 1] > 0:#寻找是否有队列有i-1的可以放置  
                    end[i - 1] -= 1#放置了之后，以i-1为终点的队列减少一个
                    end[i] += 1
                elif left[i + 1] and left[i + 2]:#看看本队列还有没有可能
                    left[i + 1] -= 1#如果可以，那么用掉的两个数字都要减1
                    left[i + 2] -= 1
                    end[i + 2] += 1#此处就要增加一个以i+2结尾的队列
                else:
                    return False
            return True
        
        
        
        
        
        
        
        
        
        
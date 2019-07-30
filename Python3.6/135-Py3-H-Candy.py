# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 17:11:42 2018

@author: hjiang
"""
"""
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

Example 1:

Input: [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
             The third child gets 1 candy because it satisfies the above two conditions
             
"""

# Time:  O(n)
# Space: O(n)

#import operator
# 需要正序和逆序都来一遍主要是考虑到第一个或者最后一个会不对
class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        candies = [1 for _ in range(len(ratings))]# 先每人给一个
        for i in range(1, len(ratings)): # 顺序来一遍
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        print ("First time", candies)
        for i in reversed(range(1, len(ratings))): # 逆序来一遍
            if ratings[i - 1] > ratings[i] and candies[i - 1] <= candies[i]: #非常重要，都要满足
                candies[i - 1] = candies[i] + 1
        print ("Second time", candies)
#        return reduce(operator.add, candies)
        return sum(candies)
        
if __name__ == "__main__":
    print(Solution().candy([1,0,2]))
    print(Solution().candy([1,2,2]))
    
    
    
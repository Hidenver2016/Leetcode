# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 17:57:33 2019

@author: hjiang
"""

"""
Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Different from the previous question where weight is increasing from root to leaf, 
now the weight is defined from bottom up. i.e., the leaf level integers have weight 1, 
and the root level integers have the largest weight.

Example 1:

Input: [[1,1],2,[1,1]]
Output: 8 
Explanation: Four 1's at depth 1, one 2 at depth 2.
Example 2:

Input: [1,[4,[6]]]
Output: 17 
Explanation: One 1 at depth 3, one 4 at depth 2, and one 6 at depth 1; 1*3 + 4*2 + 6*1 = 17.
"""
"""
#https://leetcode.com/problems/nested-list-weight-sum-ii/discuss/83643/Python-solution-with-detailed-explanation
#这个想法很奇妙，就是反着来，先从最外层开始剥，bfs加level sum多次循环，那么最外层到最里层有多少个括号，最外层就被加了多少次。
#这个方法虽然没有用乘法，一样实现了目的，实际上就是把乘法变成了累加
"""
class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        total_sum, level_sum = 0, 0
        while len(nestedList):
            next_level_list = []
            for x in nestedList:
                if x.isInteger():
                    level_sum += x.getInteger()#注意这里，虽然是一层层去掉括号的，但是level_sum一直在累加给total_sum,那么就是第一层的1会被加很多次，省掉了乘法
                else:
                    for y in x.getList():
                        next_level_list.append(y)
            total_sum += level_sum#注意，level_sum不清0， 所以之前的一直在累加
            nestedList = next_level_list
        return total_sum
"""
Two Pass Solution

In the first pass, get the maximum depth of the nested list. 
The recursion is obvious - traverse the list and if there is any nestedList, find its depth. 
The final depth is the maximum depth from any nestedList.
In the second pass, compute the sum using the same method as used in in the previous problem 
https://leetcode.com/problems/nested-list-weight-sum/
"""    
class Solution1(object):
    def depth(self, nestedList):
        curr_depth = 1
        for x in nestedList:
            if x.isInteger() == False:
                curr_depth = max(curr_depth, 1+self.depth(x.getList()))
        return curr_depth
    
    def helper(self, nestedList, level, max_depth):
        for x in nestedList:
            if x.isInteger():
                self.d_sum = self.d_sum + x.getInteger()*(max_depth-level+1)
            else:
                self.helper(x.getList(), level+1, max_depth)
        return
    
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        max_depth = self.depth(nestedList)
        self.d_sum = 0
        self.helper(nestedList, 1, max_depth)
        return self.d_sum
    
    
    
    
    
    
    
    
    
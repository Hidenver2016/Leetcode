# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 17:45:56 2019

@author: hjiang
"""

"""
Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:

Input: [[1,1],2,[1,1]]
Output: 10 
Explanation: Four 1's at depth 2, one 2 at depth 1.
Example 2:

Input: [1,[4,[6]]]
Output: 27 
Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4*2 + 6*3 = 27.
"""
#https://leetcode.com/problems/nested-list-weight-sum/discuss/215802/Best-Python-Solution-(DFS-and-BFS)
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
# 

class Solution(object):
    #DFS(Depth-First-Search)
	#Efficiency: O(N), Space: O(D).
	#N is the total element of the nestedList, D is the depth.
    def depthSum(self, nestedList, weight=1):
        counter = 0
        for e in nestedList:
            if e.isInteger():
                counter+=(e.getInteger()*weight)
            else:
                counter+=self.depthSum(e.getList(), weight+1)
        return counter
    
    #BFS(Breadth-First-Search)
	#Efficiency: O(N), Space: O(N).
    def depthSum1(self, nestedList):
        counter = 0                                              #第一个1是权重，第二个1是用来一级级相加的
        queue = [(1, e) for e in nestedList]# 假设a=[1, [2, [3]]]，queue = [(1, 1), (1, [2, [3]])]
        while queue:
            weight, e = queue.pop(0)
            if e.isInteger():
                counter += e.getInteger()*weight
            else:
                for child_list in e.getList():
                    queue.append((weight+1, child_list))
                
        return counter
    
def depthSum(nestedList):
    res = 0
    stack = []
    weight = 1
    for e in nestedList:
        if e.isdigit():
            res += int(e) * weight
        else:
            if e == ',': continue
            stack.append(e)
            if len(stack) >= 2 and e == ']':
                stack.pop()
                stack.pop()
            weight = len(stack) + 1
    return res

a = '[1,1],2,[1,1]'
b = '1,[4,[6]]'
print(depthSum(a))
            
        








    
    
    
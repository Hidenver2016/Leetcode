# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 21:13:56 2019

@author: hjiang
"""

"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.


110和104类似
"""

class Solution:#自己写的，比较复杂，但时间很快
    # @param {TreeNode} root
    # @return {integer}
    def maxDepth(self, root):
        if not root: return 0
        self.res = float("-inf")
        self.helper(root, 1)
        return self.res

    def helper(self, root, depth):
        if root.left == None and root.right == None and depth > self.res:
            self.res = depth
            return
        if root.left:
            self.helper(root.left, depth + 1)
        if root.right:
            self.helper(root.right, depth + 1)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxDepth(self, root):
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
#https://leetcode.com/problems/balanced-binary-tree/discuss/157645/Python-Tree-tm  
#这个要看一下！！！        
class Solution1(object):
    def maxDepth_gd(self, root):#看这个 和110题没有区别
        '''bugfree'''
        if not root: return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1
    

# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 17:38:40 2019

@author: hjiang
"""

"""
For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.

A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.

Write a function that determines whether two binary trees are flip equivalent.  The trees are given by root nodes root1 and root2.

 

Example 1:

Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
Output: true
Explanation: We flipped at nodes with values 1, 3, and 5.
Flipped Trees Diagram
 

Note:

Each tree will have at most 100 nodes.
Each value in each tree will be a unique integer in the range [0, 99].
和87题是一样的
https://blog.csdn.net/fuxuemingzhu/article/details/84728645
https://leetcode.com/articles/flip-equivalent-binary-trees/
Time：O(min(N_1,N_2))
Space: O(min(H_1,H_2))
 
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if not root1 and not root2: return True
        if not root1 and root2: return False
        if root1 and not root2: return False
        if root1.val != root2.val: return False
        return (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)) or \
                (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right))

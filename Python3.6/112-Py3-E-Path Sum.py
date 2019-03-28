# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 14:38:09 2019

@author: hjiang
"""

"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all 
the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

此题和257一模一样
"""
class Solution(object):#recur
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root: return False
        if not root.left and not root.right:
            return sum == root.val
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)


class Solution1(object):#iter
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        myStack = []
        myStack.append((root, 0))
        while myStack:
            node, path = myStack.pop()
            if not node: continue
            path += node.val
            if not node.left and not node.right and path == sum:
                return True
            if node.left:
                myStack.append((node.left, path))
            if node.right:
                myStack.append((node.right, path))
        return False

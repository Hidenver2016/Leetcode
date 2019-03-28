# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 14:37:26 2019

@author: hjiang
"""

"""
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
https://blog.csdn.net/fuxuemingzhu/article/details/71249429

257和112一模一样
"""

class Solution(object):#recursive
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        res = []
        self.dfs(root, res, '' + str(root.val))
        return res
        
    def dfs(self, root, res, path):
        if root.left == None and root.right == None:
            res.append(path)
        if root.left != None:
            self.dfs(root.left, res, path + '->' + str(root.left.val))
        if root.right != None:
            self.dfs(root.right, res, path + '->' + str(root.right.val))
            
class Solution1(object):#iterative
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        stack = []
        res = []
        stack.append((root, str(root.val)))
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                res.append(path)
            if node.left:
                stack.append((node.left, path + "->" + str(node.left.val)))
            if node.right:
                stack.append((node.right, path + "->" + str(node.right.val)))
        return res


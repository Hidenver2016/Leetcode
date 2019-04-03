# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 21:17:27 2019

@author: hjiang
"""

"""

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
https://blog.csdn.net/fuxuemingzhu/article/details/79533462
http://www.cnblogs.com/grandyang/p/4296193.html
105，106， 297一起
"""
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder: return None
        val = postorder[-1]
        root = TreeNode(val)
        index = inorder.index(val)
        root.left = self.buildTree(inorder[:index], postorder[:index])
        root.right = self.buildTree(inorder[index+1:], postorder[index:-1])
        return root

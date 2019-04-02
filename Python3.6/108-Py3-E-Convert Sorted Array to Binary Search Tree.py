# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 20:53:10 2019

@author: hjiang
"""
"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree 
in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
因为BST的中序遍历是有序的，所以有序数组的中间的数字是根节点，序列中间节点左边是根节点的左子树，右边是根节点的右子树，以此类推。
此题要和109一起做
https://blog.csdn.net/fuxuemingzhu/article/details/70665213
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums: return None
        _len = len(nums)
        mid = _len // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root

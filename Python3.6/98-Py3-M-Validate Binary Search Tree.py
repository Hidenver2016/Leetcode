# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 14:46:58 2019

@author: hjiang
"""

"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:

Input:
    2
   / \
  1   3
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.
https://www.youtube.com/watch?v=Jq0Wk9xeQ0U

"""

class Solution(object):#看这个，简单
    def isValidBST(self, root, lessThan = float('inf'), largerThan = float('-inf')):
        if not root:
            return True
        if root.val <= largerThan or root.val >= lessThan:
            return False #向左子节点走，最大值要小于本节点； 向右, 最小值要大于本节点
        return self.isValidBST(root.left, min(lessThan, root.val), largerThan) and self.isValidBST(root.right, lessThan, max(root.val, largerThan))
               
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time:  O(n)
# Space: O(h)递归的深度
class Solution1:
    def isValidBST(self,root):
        return self.ValidBST(root,float("-inf"),float("inf"))
        
    def ValidBST(self,root,min,max):
        if not root:
            return True
        if root.val <= min or root.val >= max:
            return False
        
        return self.ValidBST(root.left,min,root.val) and self.ValidBST(root.right, root.val,max) 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

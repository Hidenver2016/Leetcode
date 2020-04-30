# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 21:15:08 2019

@author: hjiang
"""

"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to 
any node in the tree along the parent-child connections. The path must contain at least 
one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42

此题和687以及543是一样的
花花讲过

此题要理解： 一条边只能经过一次
"""

# Time:  O(n)
# Space: O(h), h is height of binary tree

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxPathSum(self, root):
        self.maxSum = float("-inf")
        self.helper(root)
        return self.maxSum

    def helper(self, root):
        if root is None:
            return 0
        left = max(0, self.helper(root.left))# 0放在这就是说下面子节点上的负数就不用加上来了
        right = max(0, self.helper(root.right))
        self.maxSum = max(self.maxSum, root.val + left + right)# 这里返回的是self.maxSum的答案
        return root.val + max(left, right)#这里返回的是递归函数helper的答案， 只要一条边就行了
    
    
    
    
    
    
    
    
    
    
    
    
    

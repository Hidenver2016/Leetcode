# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 21:12:06 2019

@author: hjiang
"""

"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
https://blog.csdn.net/fuxuemingzhu/article/details/48519035
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if not left:
            return right + 1
        if not right:
            return left + 1
        return 1 + min(left, right)
    
    def minDepth1(self, root):# 这个和上面那个一样，自己改的，比较好理解，这个应该是dfs,因为到底了
        if not root: return 0
        if not root.left: return self.minDepth(root.right) + 1 # 左边没有就找右边
        if not root.right: return self.minDepth(root.left) + 1 # 右边没有就找左边
        return 1 + min(self.minDepth(root.right), self.minDepth(root.left)) # 两边都有就取最小值
    
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    print (Solution().minDepth(root))
    
    
    
    
    
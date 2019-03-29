# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 21:17:47 2019

@author: hjiang
"""

"""
Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.

Example :

Input:  root = [5,1,5,5,5,null,5]

              5
             / \
            1   5
           / \   \
          5   5   5

Output: 4


1st subtree: 5(root) 5(right child of root) 5(right child of right child of root) 这个不算
2nd subtree: 5(right child of root) 5(right child of right child of root)
3rd subtree: 5 (right child of right child of root)
4th subtree: 5 (left child of 1)
5th subtree: 5 (right child of 1)

看下面自己写的例子：
子树不能包括根节点，而且子树必须完整，不能搞一个枝的左半或右半。但是叶子，和往上的父节点可以算两个子树。
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countUnivalSubtrees(self, root):
        self.ans = 0
        def recurse(node, parent):
            if not node:
                return True
            left = recurse(node.left, node.val)
            right = recurse(node.right, node.val)
            if left and right:
                self.ans += 1
            return left and right and node.val == parent# 最后这一个条件就是要左边和右边都要等于parent，才能够返回子树
        recurse(root, None)
        return self.ans
    
if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(6)
    root.right = TreeNode(3)
    root.left.left = TreeNode(7)
    root.left.right = TreeNode(6)
    root.right.right = TreeNode(6)
    print (Solution().countUnivalSubtrees(root))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 21:17:23 2019

@author: hjiang
"""

"""
Given a binary tree where all the right nodes are either leaf nodes with a sibling 
(a left node that shares the same parent node) or empty, flip it upside down and turn 
it into a tree where the original right nodes turned into left leaf nodes. Return the new root.

Example:

Input: [1,2,3,4,5]

    1
   / \
  2   3
 / \
4   5

Output: return the root of the binary tree [4,5,2,#,#,3,1]

   4
  / \
 5   2
    / \
   3   1  
Clarification:

Confused what [4,5,2,#,#,3,1] means? Read more below on how binary tree is serialized on OJ.

The serialization of a binary tree follows a level order traversal, where '#' signifies a path terminator where no node exists below.

Here's an example:

   1
  / \
 2   3
    /
   4
    \
     5
The above binary tree is serialized as [1,2,3,#,#,4,#,#,5].

http://www.cnblogs.com/grandyang/p/5172838.html
https://leetcode.com/problems/binary-tree-upside-down/discuss/49410/Explain-the-question-and-my-solution-Python
仔细观察，所有位置都顺时针移动一个位置
这个题目有点无语
                         Root                   L
                         /  \                  /  \
                        L    R                R   Root
"""
class Solution:
    def upsideDownBinaryTree(self, root):#有人改进过的
        if root and root.left :
            res = self.upsideDownBinaryTree(root.left)
            root.left.right=root
            if root.right :
                root.left.left=root.right
            root.left =None
            root.right=None
            return res
        else:
            return root
        
    def upsideDownBinaryTree1(self, root):#原始解法
        if not root or not root.left:
            return root
        lRoot = self.upsideDownBinaryTree(root.left)
        rMost = lRoot
        while rMost.right:
            rMost = rMost.right
        root, rMost.left, rMost.right = lRoot, root.right, TreeNode(root.val)
        return root        
        
        
        
        
        
        
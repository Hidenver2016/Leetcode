# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 20:53:12 2019

@author: hjiang
"""
"""
Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

The successor of a node p is the node with the smallest key greater than p.val.

 

Example 1:


Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.
Example 2:


Input: root = [5,3,6,2,4,null,null,1], p = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.
 

Note:

If the given node has no in-order successor in the tree, return null.
It's guaranteed that the values of the tree are unique.
https://leetcode.com/problems/inorder-successor-in-bst/discuss/72656/JavaPython-solution-O(h)-time-and-O(1)-space-iterative
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:#iter，看这个好了,比较容易懂
    def inorderSuccessor(self, root, p):
        succ = None
        while root:
            if p.val < root.val:
                succ = root#只有这里有，因为是successor,不小于的话，不会赋值
                root = root.left
            else:
                root = root.right
        return succ
#https://leetcode.com/problems/inorder-successor-in-bst/discuss/72723/Python-Short-Recursive-solution-4-lines
class Solution1:
    def inorderSuccessor(self, root, p):#recur 两个一样快
        if not root: return None
        if root.val>p.val: return self.inorderSuccessor(root.left,p) or root 
        return self.inorderSuccessor(root.right,p)

if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)
    root.left.left.right = TreeNode(2.1)
    print(Solution1().inorderSuccessor(root,TreeNode(2.5)).val)

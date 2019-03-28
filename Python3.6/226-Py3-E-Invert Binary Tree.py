# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 14:08:18 2019

@author: hjiang
"""

"""
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew), 
but you can’t invert a binary tree on a whiteboard so f*** off.
https://blog.csdn.net/fuxuemingzhu/article/details/51284488
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):# recursive
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return None
        root.left, root.right = root.right, root.left#这一句是连带着底下的枝叶，全部都换了！！！！！！！！！
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

#使用迭代方法。众所周知，把递归改成迭代需要一个栈，这个题使用迭代基本就是套个模板就好了，关键步骤只有一行，那就是把两个子树进行翻转。
class Solution1(object):# iterative
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        myStack = []
        myStack.append(root)
        while myStack:
            node = myStack.pop()
            if not node:
                continue
            node.left, node.right = node.right, node.left
            myStack.append(node.left)
            myStack.append(node.right)
        return root
    
if __name__ == "__main__":
    root = TreeNode(4)
#    root.val = 4
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    print(root.val, root.left.val, root.right.val, root.left.left.val, root.left.right.val, root.right.left.val, root.right.right.val)
    root.left, root.right = root.right, root.left
    print(root.val, root.left.val, root.right.val, root.left.left.val, root.left.right.val, root.right.left.val, root.right.right.val)

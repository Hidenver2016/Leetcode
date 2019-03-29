# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 21:14:41 2019

@author: hjiang
"""

"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.


110和104类似

下面这种方法更快速，因为只要发现不是均衡的就直接返回-1了
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):#这个方法较优
    def isBalanced(self, root):
            
        def check(root):
            if root is None:
                return 0
            left  = check(root.left)
            right = check(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:#因为这个地方会返回-1，所以会出现left, right 等于 -1的情况
                return -1
            return 1 + max(left, right) #这个计算高度是从叶子开始往上加，所以只要发现最后面的相差大于1就可以不做了
        
        return check(root) != -1
"""
#https://leetcode.com/problems/balanced-binary-tree/discuss/157645/Python-Tree-tm
#110和104类似 中文解答
#注意这个地方有时间复杂度的详细分析，下面这个解法是暴力解法，注意最后一行的return, 他会穷尽所有的树枝。这样的话，对于每一个分支，都是/2的复杂度
可以理解成每一层都是n,而二叉树的深度是logn,所以是nlogn

"""
class Solution1(object):
    def isBalanced(self, root):
        if not root: return True
        left = self.get_height(root.left)
        right = self.get_height(root.right)
        if abs(left - right) > 1: 
            return False  
        return self.isBalanced(root.left) and self.isBalanced(root.right)

        
    def get_height(self, root):
        if not root: return 0
        left = self.get_height(root.left)
        right = self.get_height(root.right)
        return max(left, right) + 1


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    print (Solution1().isBalanced(root))
















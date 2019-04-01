# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 14:53:58 2019

@author: hjiang
"""

"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. 
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/discuss/33834/Python-simple-BFS
这个题目和107很像，还有之前的366， 102,建议一起看
"""

    
class Solution1(object):
    def zigzagLevelOrder(self, root):# 自己写的迭代，注意一下
        if root == None: return []
        myQueue = []
        ans = []
        node = root
        flag = 1
        myQueue.append(node)
        while myQueue:
            level = []
            for i in range(len(myQueue)):
                node = myQueue.pop(0)
                level.append(node.val)
                if node.left: myQueue.append(node.left)
                if node.right: myQueue.append(node.right)
            ans.append(level[::flag])
            flag *= -1
        return ans
    
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        res, temp, stack, flag=[], [], [root], 1
        while stack:
            for i in range(len(stack)):
                node=stack.pop(0)
                temp+=[node.val]
                if node.left: stack+=[node.left]
                if node.right: stack+=[node.right]
            res+=[temp[::flag]]
            temp=[]
            flag*=-1
        return res
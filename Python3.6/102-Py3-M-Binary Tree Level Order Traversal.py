# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 23:40:41 2019

@author: hjiang
"""

"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
https://blog.csdn.net/fuxuemingzhu/article/details/79616156
这个题要和144， 94， 145， 102一起做
"""
class Solution1(object):
    def levelOrder(self, root):# 自己写的迭代，注意一下
        if root == None: return []
        myQueue = []
        ans = []
        node = root
        myQueue.append(node)
        while myQueue:
            level = []#如果下面也写成while myQueue： 那么答案就是[[3,9,20,15,7]]，就是不分层了，全部一起输出
            for i in range(len(myQueue)):#之后的变长对于这个是没有影响的，固定死了，所以一次是一层！！！
                node = myQueue.pop(0)
                level.append(node.val)
                if node.left: myQueue.append(node.left)
                if node.right: myQueue.append(node.right)
            ans.append(level)
        return ans

import collections
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root: return res
        queue = collections.deque()
        queue.append(root)
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res
    
    def BFS(self, root):#标准BFS
        """利用队列实现树的层次遍历"""
        if root == None:
            return
        myQueue = []
        node = root
        myQueue.append(node)
        while myQueue:
            node = myQueue.pop(0)
            print (node.value)
            if node.lch != None:
                myQueue.append(node.lch)
            if node.rch != None:
                myQueue.append(node.rch)
    
    

    
    
    
    
    
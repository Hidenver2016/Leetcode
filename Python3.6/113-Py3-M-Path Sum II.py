# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 14:39:19 2019

@author: hjiang
"""

"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""
#https://blog.csdn.net/fuxuemingzhu/article/details/80779723
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root: return []
        res = []
        self.dfs(root, sum, res, [root.val])
        return res

    def dfs(self, root, target, res, path):
        if not root: return
        if sum(path) == target and not root.left and not root.right:
            res.append(path)
            return
        if root.left:
            self.dfs(root.left, target, res, path + [root.left.val])
        if root.right:
            self.dfs(root.right, target, res, path + [root.right.val])



#https://leetcode.com/problems/path-sum-ii/discuss/36829/Python-solutions-(Recursively-BFS%2Bqueue-DFS%2Bstack)
            
"""
这个是递归，迭代，BFS都有
"""

def pathSum(self, root, sum):
    if not root:
        return []
    res = []
    self.dfs(root, sum, [], res)
    return res
    
def dfs(self, root, sum, ls, res):
    if not root.left and not root.right and sum == root.val:
        ls.append(root.val)
        res.append(ls)
    if root.left:
        self.dfs(root.left, sum-root.val, ls+[root.val], res)
    if root.right:
        self.dfs(root.right, sum-root.val, ls+[root.val], res)
        
def pathSum2(self, root, sum):
    if not root:
        return []
    if not root.left and not root.right and sum == root.val:
        return [[root.val]]
    tmp = self.pathSum(root.left, sum-root.val) + self.pathSum(root.right, sum-root.val)
    return [[root.val]+i for i in tmp]

# BFS + queue    
def pathSum3(self, root, sum): 
    if not root:
        return []
    res = []
    queue = [(root, root.val, [root.val])]
    while queue:
        curr, val, ls = queue.pop(0)
        if not curr.left and not curr.right and val == sum:
            res.append(ls)
        if curr.left:
            queue.append((curr.left, val+curr.left.val, ls+[curr.left.val]))
        if curr.right:
            queue.append((curr.right, val+curr.right.val, ls+[curr.right.val]))
    return res
    
# DFS + stack I  
def pathSum4(self, root, sum): 
    if not root:
        return []
    res = []
    stack = [(root, sum-root.val, [root.val])]
    while stack:
        curr, val, ls = stack.pop()
        if not curr.left and not curr.right and val == 0:
            res.append(ls)
        if curr.right:
            stack.append((curr.right, val-curr.right.val, ls+[curr.right.val]))
        if curr.left:
            stack.append((curr.left, val-curr.left.val, ls+[curr.left.val]))
    return res 

# DFS + stack II   
def pathSum5(self, root, s): 
    if not root:
        return []
    res = []
    stack = [(root, [root.val])]
    while stack:
        curr, ls = stack.pop()
        if not curr.left and not curr.right and sum(ls) == s:
            res.append(ls)
        if curr.right:
            stack.append((curr.right, ls+[curr.right.val]))
        if curr.left:
            stack.append((curr.left, ls+[curr.left.val]))
    return res
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 14:54:40 2019

@author: hjiang
"""

"""
Given a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
本题与102， 103， 107, 199都很像
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):# 自己写的迭代，注意一下
        if root == None: return []
        myQueue = []
        ans = []
        node = root
        myQueue.append(node)
        while myQueue:
            ans.append(myQueue[-1].val)
            for i in range(len(myQueue)):
                node = myQueue.pop(0)
                if node.left: myQueue.append(node.left)
                if node.right: myQueue.append(node.right)
        return ans
    
#或者还可以直接使用102等题的代码，然后每一层都取最后一个即可.测试时间居然和上面一样！！！明显多了一个循环！！！
class Solution1(object):
    def rightSideView(self, root):# 自己写的迭代，注意一下
        if root == None: return []
        myQueue = []
        ans = []
        node = root
        myQueue.append(node)
        while myQueue:
            level = []
            for i in range(len(myQueue)):
                node = myQueue.pop(0)
                level.append(node.val)
                if node.left: myQueue.append(node.left)
                if node.right: myQueue.append(node.right)
            ans.append(level)
        ans1 = []
        for item in ans:
            ans1.append(item[-1])
        return ans1



class Solution2(object):#iter,快很多！！！
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root: return res
        queue = collections.deque()
        queue.append(root)
        while queue:
            res.append(queue[-1].val)
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res

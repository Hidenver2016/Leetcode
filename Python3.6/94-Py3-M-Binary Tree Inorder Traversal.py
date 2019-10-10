# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 23:40:29 2019

@author: hjiang
"""

"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
https://blog.csdn.net/fuxuemingzhu/article/details/79294461
这个题要和144， 94， 145， 102一起做
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

            
class Solution2:
    def inorderTraversal(self, root):#自己写的递归
        if root == None: return
        ans = []
        if root.left != None:
            ans.extend(self.inorderTraversal(root.left))
        ans.append(root.val)
        if root.right != None:
            ans.extend(self.inorderTraversal(root. right))
        return ans
    
class Solution3:
    def inorderTraversal(self, root):#自己写的迭代
        if root == None: return []
        myStack = []
        ans = []
        node = root
        while node or myStack:
            while node:
                myStack.append(node)
                node = node.left
            node = myStack.pop()
            ans.append(node.val)
            node = node.right
        return ans
    
class Solution(object):
    def inorderTraversal(self, root): #递归
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        answer = []
        def inorder(root):
            if root == None:
                return None
            if root.left != None:
                inorder(root.left)
            answer.append(root.val)
            if root.right != None:
                inorder(root.right)
        inorder(root)
        return answer


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1(object):
    def inorderTraversal(self, root):#迭代
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        answer = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return answer
            root = stack.pop()
            answer.append(root.val)
            root = root.right
            
            
            
            
            
            
            
            
            
            
            
            

# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 20:53:11 2019

@author: hjiang
"""

"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

 

Example:



BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false
 

Note:

next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.

只保留左节点
下面的做法的空间复杂度是O(h)，做法是每次保存要遍历的节点的所有左孩子。这样，每次最多也就是H个节点被保存，
当遍历了这个节点之后，需要把该节点的右孩子的所有左孩子放到栈里，这就是个中序遍历的过程。
https://blog.csdn.net/fuxuemingzhu/article/details/79436947
https://leetcode.com/problems/binary-search-tree-iterator/discuss/52642/Two-Python-solutions-stack-and-generator
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):#
        self.stack = []#stack 是降序排列，最小的在最后
        while root:
            self.stack.append(root)
            root = root.left
    
    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return len(self.stack) > 0
    
    # @return an integer, the next smallest number
    def next(self):
        node = self.stack.pop()#先弹出小的，再补充右边大的
        x = node.right# 注意这个，不要漏掉下面右侧较大的点
        while x:#重复前面的
            self.stack.append(x)
            x = x.left
        return node.val
    
    
# Time:  O(1)
# Space: O(h), h is height of binary tree


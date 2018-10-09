# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 14:10:54 2018

@author: hjiang
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right =  None

class solution1(object):
    list_head = None
    def flatten(self, root):
        if root != None:
            self.flatten(root.right)
            self.flatten(root.left)
            root.right = self.list_head
            root.left = None
            self.list_head = root
            return root
        
if __name__=="__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(5)
    root.right.right = TreeNode(6)
    result = solution1().flatten(root)
    print ("{0} - > {1} - > {2} - > {3} - > {4} - > {5} ".format(
            result.val, 
            result.right.val, 
            result.right.right.val, 
            result.right.right.right.val, 
            result.right.right.right.right.val,
            result.right.right.right.right.right.val
           ))
#            
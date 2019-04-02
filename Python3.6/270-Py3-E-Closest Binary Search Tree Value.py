# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 20:53:14 2019

@author: hjiang
"""

"""
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4
230和270可以一起做
"""
#https://leetcode.com/problems/closest-binary-search-tree-value/discuss/70321/Clean-python-code
class Solution(object):
    def closestValue(self, root, target):
        r = root.val
        while root:
            if abs(root.val - target) < abs(r - target):
                r = root.val
            root = root.left if target < root.val else root.right
        return r
#https://leetcode.com/problems/closest-binary-search-tree-value/discuss/70327/4-7-lines-recursiveiterative-RubyC%2B%2BJavaPython    
def closestValue(self, root, target):#o(1) space
    closest = root.val
    while root:
        closest = min((root.val, closest), key=lambda x: abs(target - x))
        root = root.left if target < root.val else root.right
    return closest
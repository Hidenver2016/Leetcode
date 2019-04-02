# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 20:53:12 2019

@author: hjiang
"""

"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? 
How would you optimize the kthSmallest routine?
https://blog.csdn.net/fuxuemingzhu/article/details/69947495
https://leetcode.com/problems/kth-smallest-element-in-a-bst/discuss/63829/Python-Easy-Iterative-and-Recursive-Solution
230和270可以一起做
"""
class Solution:#recur
    def kthSmallest(self, root, k):
        self.k = k
        self.res = None
        self.helper(root)
        return self.res

    def helper(self, node):
        if not node:
            return
        self.helper(node.left)
        self.k -= 1
        if self.k == 0:
            self.res = node.val
            return
        self.helper(node.right)
        
class Solution1:#iter 快！！！
    def kthSmallest(self, root, k):
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
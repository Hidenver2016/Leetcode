# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 21:17:25 2019

@author: hjiang
"""

"""
Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), 
where largest means subtree with largest number of nodes in it.

Note:
A subtree must include all of its descendants.

Example:

Input: [10,5,15,1,8,null,7]

   10 
   / \ 
  5  15 
 / \   \ 
1   8   7

Output: 3
Explanation: The Largest BST Subtree in this case is the highlighted one.
             The return value is the subtree's size, which is 3.
Follow up:
Can you figure out ways to solve it with O(n) time complexity?
https://leetcode.com/problems/largest-bst-subtree/discuss/78895/Short-Python-solution
http://www.cnblogs.com/grandyang/p/5188938.html
"""

class Solution(object):
    def largestBSTSubtree(self, root):#就看这个吧
        self.res = 0
        def find(node):
            if not node: return float('inf'), float('-inf'), 0#没有节点 return回一个这样的数据，可以确保不再往下面计算节点数了
            lmin, lmax, lnum = find(node.left)
            rmin, rmax, rnum = find(node.right)
            n = float('-inf')
            if node.val > lmax and node.val < rmin:#大于左边最大，小于右边最小，即可把左右子树的节点数相加，再加上本节点一个
                n = lnum + rnum + 1
                self.res = max(n, self.res)
            return min(node.val, lmin), max(node.val, rmax), n# 这个地方返回的是一棵树的最小值和最大值，然后还有他包含的节点数
        find(root)
        return self.res
    
class Solution1(object):#稍微快一点
    def largestBSTSubtree(self, root):
        def solve(root, maxval):
            if not root: return 0, float('inf'), -float('inf')
            left,  minvl, maxvl = solve(root.left, maxval)
            right, minvr, maxvr = solve(root.right, maxval)
            if left == -1 or right == -1 or not maxvl < root.val < minvr:
                return -1, 0, 0
            maxval[0] = max(maxval[0], 1 + left + right)
            return 1 + left + right, min(root.val, minvl, minvr), max(root.val, maxvr, maxvl)
        
        maxval = [0]
        solve(root, maxval)
        return maxval[0]
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
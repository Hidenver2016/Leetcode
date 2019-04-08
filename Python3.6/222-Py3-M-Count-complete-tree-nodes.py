# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 17:39:19 2018

@author: hjiang
"""

"""
Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, 
and all nodes in the last level are as far left as possible. 
It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6

关键：如果单纯用dfs,肯定超时了，注意考虑complete binary tree的特点，第三种解法比较好
"""
# 最原始的解法
class Node(object):
    def __init__(self, value = -1):
        self.value = value
        self.left = None
        self.right = None
        
class Solution0(object):
    def __init__(self):
        self.root = Node()
        self.count = 0
        
    def pre_recur(self, root):
        if root == None:
            return 0
        self.count += 1
        self.pre_recur(root.left)
        self.pre_recur(root.right)
    
    def countNodes(self, root):
        self.pre_recur(root)
        return self.count
    
# 写的简洁一点：
class Solution1:#这个是通用算法，不快
    def countNodes(self, root):
        if root is None:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)        
#高级算法 
#compare the depth between left sub tree and right sub tree.
#A, If it is equal, it means the left sub tree is a full binary tree
#B, It it is not , it means the right sub tree is a full binary tree
#Time: O(lgn * lgn)
#Spce: O(2*lgn)
class Solution2: #优，这个是比较好的，看这个
        # @param {TreeNode} root
        # @return {integer}
        def countNodes(self, root):
            if not root:
                return 0
            leftDepth = self.getDepth(root.left)
            rightDepth = self.getDepth(root.right)
            if leftDepth == rightDepth:
                return pow(2, leftDepth) + self.countNodes(root.right)
            else:
                return pow(2, rightDepth) + self.countNodes(root.left)
    
        def getDepth(self, root):
            if not root:
                return 0
            return 1 + self.getDepth(root.left)

    
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    print(Solution0().countNodes(root))
    
        
        

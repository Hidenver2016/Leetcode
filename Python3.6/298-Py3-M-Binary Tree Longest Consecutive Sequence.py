# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 14:39:59 2019

@author: hjiang
"""

"""
Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. 
The longest consecutive path need to be from parent to child (cannot be the reverse).

Example 1:

Input:

   1
    \
     3
    / \
   2   4
        \
         5

Output: 3

Explanation: Longest consecutive sequence path is 3-4-5, so return 3.
Example 2:

Input:

   2
    \
     3
    / 
   2    
  / 
 1

Output: 2 

Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.
"""
# Time:  O(n)
# Space: O(h)
#https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/discuss/74576/13-lines-of-Python-DFS-solution
from collections import deque
class Solution:#iter dfs
    def longestConsecutive(self, root):
        if not root:
            return 0

        ret = 0
        stack = [(root, 1)]
        while stack:
            node, cnt = stack.pop()
            if node.left:
                stack.append((node.left, cnt+1 if node.left.val == node.val + 1 else 1))
            if node.right:
                stack.append((node.right, cnt+1 if node.right.val == node.val + 1 else 1))
            ret = max(ret, cnt)

        return ret
    
class Solution1(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        self.result = 0
        self.helper(root, 1)

        return self.result

    def helper(self, root, curLen):
        self.result = curLen if curLen > self.result else self.result
        if root.left:
                self.helper(root.left, curLen + 1 if root.left.val == root.val + 1 else 1)
        if root.right:
                self.helper(root.right, curLen + 1 if root.right.val == root.val + 1 else 1)

    
#https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/discuss/74513/Two-simple-iterative-solutions-BFS-and-DFS
    def longestConsecutive1(self, root):#iter dfs
        if not root:
            return 0
        ans, stack = 0, [[root, 1]]
        while stack:
            node, length = stack.pop()
            ans = max(ans, length)
            for child in [node.left, node.right]:
                if child:
                    l = length + 1 if child.val == node.val + 1 else 1
                    stack.append([child, l])
        return ans
    

    
    def longestConsecutive2(self, root):#iter bfs
        if not root:
            return 0
        ans, dq = 0, deque([[root, 1]])
        while dq:
            node, length = dq.popleft()
            ans = max(ans, length)
            for child in [node.left, node.right]:
                if child:
                    l = length + 1 if child.val == node.val + 1 else 1
                    dq.append([child, l])
        return ans
    
    

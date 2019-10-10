# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 23:40:39 2019

@author: hjiang
"""

"""
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?

自己看一下之前的总结
这个题要和144， 94， 145， 102一起做
"""

# Time:  O(n)
# Space: O(h)
# Stack Solution
    
class Solution1:
    def postorderTraversal(self, root):#自己写的递归
        if root == None: return []
        ans = []
        if root.left != None:
            ans.extend(self.postorderTraversal(root.left))
        if root.right != None:
            ans.extend(self.postorderTraversal(root.right))
        ans.append(root.val)
        return ans
    
    
class Solution2:#自己写的迭代, 这个是先按照中右左压栈，然后弹栈就是左右中，正好是后序。只有后序是这样，前序和中序都不是
    def postorderTraversal(self, root):
        res, myStack = [], [(root, False)]
        while myStack:
            root, visited = myStack.pop()
            if root == None: continue
            if visited: res.append(root.val)
            else:
                myStack.append((root, True))
                myStack.append((root.right, False))
                myStack.append((root.left, False))
        return res
            
    
class Solution(object):#这个貌似比总结的更加简单，这个是先按照中右左压栈，然后弹栈就是左右中，正好是后序
    def postorderTraversal(self, root):
        result, stack = [], [(root, False)]
        while stack:
            root, is_visited = stack.pop()
            if root is None:
                continue
            if is_visited:
                result.append(root.val)
            else:
                stack.append((root, True))
                stack.append((root.right, False))
                stack.append((root.left, False))
        return result
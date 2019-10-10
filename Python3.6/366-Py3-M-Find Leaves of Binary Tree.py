# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 21:18:57 2019

@author: hjiang
"""

"""
Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.

 

Example:

Input: [1,2,3,4,5]
  
          1
         / \
        2   3
       / \     
      4   5    

Output: [[4,5,3],[2],[1]]
 

Explanation:

1. Removing the leaves [4,5,3] would result in this tree:

          1
         / 
        2          
 

2. Now removing the leaf [2] would result in this tree:

          1          
 

3. Now removing the leaf [1] would result in the empty tree:

          [] 
          
          
http://www.cnblogs.com/grandyang/p/5616158.html
思路是这样的，每一个节点从左子节点和右子节点分开走可以得到两个深度，由于成为叶节点的条件是左右子节点都为空，
所以我们取左右子节点中较大值加1为当前节点的深度值，知道了深度值就可以将节点值加入到结果res中的正确位置了，
求深度见104题
这个题目和107很像
"""
# Time:  O(n)
# Space: O(h)

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def findLeaves(self, root):#看这个，根据下面的答案写成自己熟悉的形式
        if not root: return []
        self.res = []
        self.helper(root, self.res)
        return self.res
    
    def helper(self, node, res):
        if not node: return -1
        level = 1 + max(self.helper(node.left, res), self.helper(node.right, res))#当前深度,叶子是0，向上逐级递增
        if len(res) < level + 1: res.append([])#左右子节点中较大值加1为当前节点的深度值
        res[level].append(node.val)
        return level#注意，这个level很重要，是从叶子开始为0，然后逐渐向上加的，所以正好是叶子为0开始

class Solution1(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def findLeavesHelper(node, result):
            if not node:
                return -1
            level = 1 + max(findLeavesHelper(node.left, result), findLeavesHelper(node.right, result))#当前深度,叶子是0，向上逐级递增
            if len(result) < level + 1:#左右子节点中较大值加1为当前节点的深度值
                result.append([])
            result[level].append(node.val)
            return level #注意，这个level很重要，是从叶子开始为0，然后逐渐向上加的，所以正好是叶子为0开始

        result = []
        findLeavesHelper(root, result)
        return result
    

        
        
    
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
#    root.right.right = TreeNode(3)
    print (Solution1().findLeaves(root))
    
    
    
    
    
    
    
    
    
    
    
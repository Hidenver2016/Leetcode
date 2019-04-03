# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 21:17:22 2019

@author: hjiang
"""

"""
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
Example 2:

Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
Follow up:

A solution using O(n) space is pretty straight forward.
Could you devise a constant space solution?
同学们，看到BST就想什么？对，中序遍历是有序的。

那么，如果其中两个被交换了，那么中序遍历的结果一定也就不对了。比如：

[1, 2, 3, 4, 5, 6]  ==>  [1, 5, 3, 4, 2, 6]
1
那么，可以看出5这个数字比后面的3大，说明他被打乱了；另外2这个数字，比前面的数字4小，所以他也被打乱了。

所以，可以通过先进行中序遍历得到所有的，然后再查找哪些乱了，再复原，时间复杂度O(n)。

但是，中序遍历的操作不需要完全完成。在中序遍历的过程中，用一个指针保存上个节点，那么当前节点值应该小于前一个节点的值。否则就存在乱序。

第一个乱序的数字是pre，第二个乱序的数字是root，所以用两个指针分别保存。

代码：
--------------------- 

原文：https://blog.csdn.net/fuxuemingzhu/article/details/79672901 

"""
# space O(1)
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.pre, self.first, self.second = None, None, None
        self.inOrder(root)
        self.first.val, self.second.val = self.second.val, self.first.val

    def inOrder(self, root):
        if not root: return
        self.inOrder(root.left)#不停的找左边，直到找到最下面，再逐级向上比较
        if self.pre and self.pre.val > root.val:#看看是不是左边大于中间，如果大于，就记下来。最后替换
            if not self.first:
                self.first = self.pre
            self.second = root #这个不停的更新，可以直接换到最上面（最后面）那个
        self.pre = root#不停的把root赋值给pre, 上面就是不停的找左边,直到找到最下面。
        self.inOrder(root.right)
        
        
#http://www.cnblogs.com/grandyang/p/4298069.html
#https://leetcode.com/problems/recover-binary-search-tree/discuss/32539/Tree-Deserializer-and-Visualizer-for-Python
#Space O(1)
class Solution1:#这个符合题意
    def recoverTree(self, root):
        swap = [None, None]
        self.prev = TreeNode(float('-inf'))
        def dfs(node):
            if node:
                dfs(node.left)
                if node.val < self.prev.val:
                    if not swap[0]: swap[0] = self.prev
                    swap[1] = node
                self.prev = node
                dfs(node.right)
        dfs(root)
        swap[0].val, swap[1].val = swap[1].val, swap[0].val


        
        
        
        
        
        
        
        
        
        
        
        
        
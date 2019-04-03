# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 14:10:54 2018

@author: hjiang
"""

"""
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right =  None
        
#https://blog.csdn.net/fuxuemingzhu/article/details/70241424
"""
最简单的方法就是使用列表保存先序遍历的每个节点，然后在列表中完成操作。即，使得列表中每个元素的左孩子为空，右孩子都是下一个节点。

这个方法很简单，不过需要O(N)的空间复杂度。

python代码如下：
"""
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        res = []
        self.preOrder(root, res)
        for i in range(len(res) - 1):
            res[i].left = None
            res[i].right = res[i + 1]
    
    def preOrder(self, root, res):
        if not root: return
        res.append(root)
        self.preOrder(root.left, res)
        self.preOrder(root.right, res) 
        
"""
递归一定要明白递归函数的意义，我觉得如果不清楚的弄明白递归函数的输入和输出是什么，那么不可能写出正确的代码。

这里的flatten(root)的输入是一个树的根节点，这个函数将使得该根节点下的所有孩子按照先序遍历的顺序放到其右侧。
返回是空，但是这个函数运行结束后，root的指向仍然是原来的位置，即树的根节点。

所以，递归的思路就有了：把左右子树分别flatten形成两个链表，然后把根节点的左孩子放到根节点的右孩子上。把原先的根节点的右孩子拼到当前根节点链表的结尾。

图形化说明：
     1
    / \
   2   5
  / \   \
 3   4   6
 
      1
      \
   2   5
    \   \
 3   4   6
 
      1
      \
   2   5
    \   \
     3   6
      \   
       4  
    1
      \   
       2   
        \   
         3   
          \   
           4    
            \
             5
              \
               6

--------------------- 

原文：https://blog.csdn.net/fuxuemingzhu/article/details/70241424 

""" 
class Solution2(object):#recur 这个和上面那个都非常快，看这个符合题意！！！
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root: return
        left = root.left
        right = root.right
        root.left = None #不断循环切断左边的连接
        self.flatten(left)
        self.flatten(right)
        root.right = left # 把左边连接到右边
        while root.right:
            root = root.right
        root.right = right #把右边连接在最后
     

class solution1(object):#z这个在leetcode里面不符合题意
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
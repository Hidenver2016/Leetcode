# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 21:17:26 2019

@author: hjiang
"""

"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
Accepted
https://blog.csdn.net/fuxuemingzhu/article/details/80775173
http://www.cnblogs.com/grandyang/p/4296500.html
简单分析一下，先序遍历的开头第一个元素是根元素，找到其在中序遍历中的位置，分割出左右子树。再根据左右子树的长度在先序遍历中划分。
105，106， 297一起
如果没有中序，只有前序和后序，二叉树是不固定的

我们下面来看一个例子, 某一二叉树的前序和中序遍历分别为：

Preorder:　  　5　　4　　11　　8　　13　　9

Inorder:　　 　11　　4　　5　　13　　8　　9

 

5　　4　　11　　8　　13　　9　　　　　　=>　　　　　　　　　 5

11　　4　　5　　13　　8　　9　　　　　　　　　　　　　　　　/　　\

 

4　　11　　 　　8　　 13　　9　　　　　　=>　　　　　　　　　5

11　　4　　　　 13　　8　　9　　 　　　　　　　　　　　　　  /　　\

　　　　　　　　　　　　　　　　　　　　　　　　　　　　　4　　　8

 

11　　　　 　　13　　　　9　　　　　　　　=>　　　　　　　　　5

11　　　　　　 13　　　　9　　　　 　　　　　　　　　　　　   /　　\

　　　　　　　　　　　　　　　　　　　　　　　　　　　　　4　　　8

　　　　　　　　　　　　　　　　　　　　　　　　　　　　/　　　 /     \

　　　　　　　　　　　　　　　　　　　　　　　　　　　11　　  13　　  9
"""
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:index+1], inorder[:index])#这里再把前序分开preorder[1:index+1]，只是要找inorder[:index]里面的根节点
        root.right = self.buildTree(preorder[index+1:], inorder[index+1:])
        return root













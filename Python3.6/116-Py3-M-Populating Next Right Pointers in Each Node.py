# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 21:03:33 2019

@author: hjiang
"""

"""
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. 
The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Example:

图看不出来，参考这里：
http://www.cnblogs.com/grandyang/p/4288151.html
Given the following perfect binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7


After calling your function, the tree should look like:

         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
--------------------- 

原文：https://blog.csdn.net/fuxuemingzhu/article/details/79559645 


Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer 
to point to its next right node, just like in Figure B.
 

Note:

You may only use constant extra space.
Recursive approach is fine, implicit stack space does not count as extra space for this problem.
"""
# Definition for binary tree with next pointer.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution0:        
    def connect1(self, root):#看这个把，答案和117题一样    ,   还是看这个比较稳定
        while root:
            cur = tmp = TreeNode(0)
            while root:
                if root.left:
                    cur.next = root.left# tmp.next也指向2，第二层第一个,然后就又指向第三层第一个，如果没有左子树的话，就是在下面完成的
                    cur = root.left
                if root.right:
                    cur.next = root.right
                    cur = root.right
                root = root.next#在这里如果root没有了就相当于在末尾加上了none
            root = tmp.next#换行

class Solution:#dfs， recur
    # @param root, a tree link node
    # @return nothing
    def connect(self, root): #看这个把，突然开窍了，感觉不难懂
        if not root: return
        if root.right:
            root.left.next = root.right#这里就是把上图的5连接到了6
            if root.next:
                root.right.next = root.next.left#这就是没想通的地方，如果2—>3, 那么5 ->6就是 root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)

class Solution1(object):#iter
    def connect(self, root):# 自己写的迭代，注意一下
        if root == None: return
        myQueue = []
#        ans = []
        node = root
        myQueue.append(node)
        myQueue.append(None)
        while myQueue:
#            level = []
#            for i in range(len(myQueue)):
            node = myQueue.pop(0)
            if node != None:#如果node == None, 那么就是说上一层的已经处理完毕
                node.next = myQueue[0]
#            level.append(node.val)
                if node.left: myQueue.append(node.left)
                if node.right: myQueue.append(node.right)
            else:
                if len(myQueue) > 0: myQueue.append(None)# 在上一层处理完毕之后这一层需要在尾巴上加None
#            ans.append(level)
        return root
    
class Solution2:#这个是符合题意的O(1) space
    def connect(self, root):
        while root and root.left:
            next = root.left
            while root:
                root.left.next = root.right
                root.right.next = root.next and root.next.left
                root = root.next
            root = next
        return root

                
class Solution3(object):#这个是数的bfs,不是这个题的答案
    def levelOrder(self, root):# 自己写的迭代，注意一下
        if root == None: return []
        myQueue = []
        ans = []
        node = root
        myQueue.append(node)
        while myQueue:
            level = []
            for i in range(len(myQueue)):
                node = myQueue.pop(0)
                level.append(node.val)
                if node.left: myQueue.append(node.left)
                if node.right: myQueue.append(node.right)
            ans.append(level)
        return ans
    
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print (Solution1().connect(root))
    
    
    
    
    
    
    
    
    
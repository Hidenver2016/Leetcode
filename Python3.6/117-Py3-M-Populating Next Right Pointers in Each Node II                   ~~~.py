# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 21:03:33 2019

@author: hjiang
"""

"""
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Example:



Input: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},
"next":null,"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},
    "next":null,"right":{"$id":"5","left":null,"next":null,"right":{"$id":"6","left":null,
    "next":null,"right":null,"val":7},"val":3},"val":1}

Output: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,
"next":{"$id":"4","left":null,"next":{"$id":"5","left":null,"next":null,"right":null,"val":7},
"right":null,"val":5},"right":null,"val":4},"next":{"$id":"6","left":null,"next":null,
"right":{"$ref":"5"},"val":3},"right":{"$ref":"4"},"val":2},"next":null,"right":{"$ref":"6"},"val":1}

Explanation: Given the above binary tree (Figure A), your function should populate each next pointer 
to point to its next right node, just like in Figure B.
 

Note:

You may only use constant extra space.
Recursive approach is fine, implicit stack space does not count as extra space for this problem.


"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution(object):#iter
    def connect(self, root):# 自己写的迭代，注意一下，这个地方O(n) 不满足
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

"""
The algorithm is a BFS or level order traversal. We go through the tree level by level. node is the pointer in the parent level, 
tail is the tail pointer in the child level.
The parent level can be view as a singly linked list or queue, which we can traversal easily with a pointer.
Connect the tail with every one of the possible nodes in child level, update it only if the connected node is not nil.
Do this one level by one level. The whole thing is quite straightforward.



hc2629
0
March 18, 2019 2:20 PM

Read More
@Allenkk Thx. Finally, I get how it works besed on your explanation. 
It means that dummy is like a dupicate of tail and it records the route where tail walks in a level. 
Therefore, the first element of dummy must be 0 and second element must be the leftmost node in 
a level which can be set as the first parent node of next level, right?



Read More
Short answer:not node.next --> end of a level, dummy is to track the path of tail that goes to the child level of current parent. 
So dummy.next gets your next level, and tail = dummy is just for exploration of next level of childs.

More explainations: remember we have three pointers, dummy, tail and node. 
I highly suggest you draw a simple treenodes like 1,2,3 see how it goes. node points to 1, 
tail points to 2 then 3 after tail moves over 0 then 2, and dummy points to the whole path that tail walked(0,2,3). 
Once node.next is null, that means a level is done, so we use dummy to let tail go back the original start of current path 
and node gets assigned to 2(i.e the next level). Now begin our next level of exploration.

Given the following binary tree,

         1
       /  \
      2    3
     / \    \
    4   5    7

After calling your function, the tree should look like:

         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
    
https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/discuss/37824/AC-Python-O(1)-space-solution-12-lines-and-easy-to-understand
这个题目的难点在于，dummy.next这个变量是在每次while node循环开始的时候自动付给不为None的tail.next. 所以不论如何，dummy.next总是自动指向下一层第一个非None的数字
"""
class Solution1:
    def connect(self, node):
        root = node # 保存head
        tail = dummy = TreeNode(0)# 开辟两个空节点 node表示父节点，tail表示子节点,或者说现在处理的节点
        while node:
            tail.next = node.left# 此处dummy.next也指向2，第二层第一个
            if tail.next:
                tail = tail.next# 每次在此处时tail.next其实指向None;tail.val变成了曾经的tail.next.val
            tail.next = node.right
            if tail.next:
                tail = tail.next
            node = node.next#一层已经走完了
            if not node:
                tail = dummy
                node = dummy.next#指向2，第二层第一个
        return root
            
            
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
#    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print (Solution1().connect(root))            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
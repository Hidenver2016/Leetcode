# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 21:25:24 2019

@author: hjiang
"""

"""
Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

Note:

Given target value is a floating point.
You may assume k is always valid, that is: k ≤ total nodes.
You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286, and k = 2

    4
   / \
  2   5
 / \
1   3

Output: [4,3]
Follow up:
Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?
https://www.cnblogs.com/grandyang/p/5247398.html

https://nb4799.neu.edu/wordpress/?p=878

这个操作是用两个stack，分别从前后来找target（一种是中序，另一个是逆中序，下面会有详细解释）
这样两个stack都是终止于target,一个是升序一个是降序
然后这两个相互比较，找出距离target最近的k个值
"""
class Solution(object):#看这个简单易懂
    def closestKValues(self, root, target, k):
        stk1 = [] # ascending (left->root->right), 结束于target，就是都比target小
        stk2 = [] # descending (right->root->left)，结束于target,就是都比target 大
        self.inorder(root, False, target, stk1)
        self.inorder(root, True, target, stk2)
        
        res = []
        for _ in range(k):#这里就是寻找最近的k个值了
            if not stk1:
                res.append(stk2.pop())
            elif not stk2:
                res.append(stk1.pop())
            else:
                if abs(stk1[len(stk1)-1] - target) < abs(stk2[len(stk2)-1] - target):
                    res.append(stk1.pop())
                else:
                    res.append(stk2.pop())
        return res
        
    def inorder(self, root, reverse, target, stk):#这个双向inorder简直就是666！！！
        if root is None:
            return 
        self.inorder(root.right, reverse, target, stk) if reverse else self.inorder(root.left, reverse, target, stk)
        # The first inequality is less than or equal, the second inequality must be larger than (without equal).
        # Or the first is less than, the second is larger than or equal to
        if not reverse and target <= root.val:
            return
        if reverse and target > root.val:
            return
        stk.append(root.val)
        self.inorder(root.left, reverse, target, stk) if reverse else self.inorder(root.right, reverse, target, stk)











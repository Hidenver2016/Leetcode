# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 11:11:56 2019

@author: hjiang
"""

"""
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
这个题目难在构造出来。一般构造树都需要递归。从1–n中任意选择一个数当做根节点，所以其左边的数字构成其左子树，右边的数字当做右子树。
因为要求出所有的子树，所以当左子树固定的时候，把所有可能的右子树都构成，然后再变换左子树。

这个代码难理解的地方在于left_nodes 和 right_nodes的求法，这个一定要结合递归的终止条件去看，当选择的根节点的值i比left小的时候，那么其实左子树就是空了。
如果把这个理解了，那么下面的对左右子树的遍历应该也不难理解。
--------------------- 
 
原文：https://blog.csdn.net/fuxuemingzhu/article/details/80778651 

"""
# Time:  O(4^n / n^(3/2)) ~= Catalan numbers
# Space: O(4^n / n^(3/2)) ~= Catalan numbers

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        if self:
            serial = []
            queue = [self]

            while queue:
                cur = queue[0]

                if cur:
                    serial.append(cur.val)
                    queue.append(cur.left)
                    queue.append(cur.right)
                else:
                    serial.append("#")

                queue = queue[1:]

            while serial[-1] == "#":
                serial.pop()

            return repr(serial)

        else:
            return None

class Solution(object):
    # @return a list of tree node
    def generateTrees(self, n):
        if n == 0: return []
        return self.generateTreesRecu(1, n)

    def generateTreesRecu(self, low, high):
        result = []
        if low > high:
            result.append(None)
        for i in range(low, high + 1):
            left = self.generateTreesRecu(low, i - 1)
            right = self.generateTreesRecu(i + 1, high)
            for j in left:
                for k in right:
                    cur = TreeNode(i)
                    cur.left = j
                    cur.right = k
                    result.append(cur)
        return result
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 14:46:40 2019

@author: hjiang
"""

"""
The thief has found himself a new place for his thievery again. 
There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. 
After a tour, the smart thief realized that "all houses in this place forms a binary tree". 
It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

Output: 7 
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:

Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \ 
 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.

本题的做法，就是求本节点+孙子更深节点vs儿子节点+重孙更深的节点的比较。

道理能想明白，代码有点难写。用了dfs函数，虽然递归是自顶向下的，但是因为是不断的return，所以真正求值是从底向上的。
用到了一个有两个元素的列表，分别保存了之前层的，不取节点和取节点的情况。然后遍历左右子树，求出当前节点取和不取能得到的值，
再返回给上一层。注意这个里面的robcurr是当前节点能达到的最大值，所以最后返回结果的时候试试返回的root节点robcurr的值。

--------------------- 
https://blog.csdn.net/fuxuemingzhu/article/details/80779068
https://leetcode.com/problems/house-robber-iii/discuss/79437/C%2B%2B-JAVA-PYTHON-and-explanation
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            # from bottom to top
            if not root: return [0, 0] # before layer, no robcurr, robcurr
            robleft = dfs(root.left)
            robright = dfs(root.right)
            norobcurr = robleft[1] + robright[1] #不带root
            robcurr = max(root.val + robleft[0] + robright[0], norobcurr)# 带root的情况
            return [norobcurr, robcurr]# 大的是后面这个robcurr
        return dfs(root)[1]#返回大的
    
if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(1)
    print(Solution().rob(root))
    











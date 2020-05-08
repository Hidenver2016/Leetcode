# -*- coding: utf-8 -*-
"""
Created on Mon May  4 11:13:47 2020

@author: hjiang
"""

"""
Given a binary tree, determine if it is a complete binary tree.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, 
and all nodes in the last level are as far left as possible. 
It can have between 1 and 2h nodes inclusive at the last level h.

 

Example 1:



Input: [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), 
and all nodes in the last level ({4, 5, 6}) are as far left as possible.
Example 2:



Input: [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.
 
Note:

The tree will have between 1 and 100 nodes.

看题目的描述： 尤其注意最后一行的描述
例子1， 执行到最后应该是[1,2,3,4,5,6,None,None,None,None，None, None, None], 
        程序的i最后在第一个None的位置，后面全是None,所以any(bfs[i:])返回 False,题目返回True
例子2， [1,2,3,4,5,None,7,None, None, None, None], 程序最后停在第一个None的位置，
        any(bfs[i:])返回True,因为第一个None后面有一个7，题目最后返回False
"""

    def isCompleteTree(self, root):
        bfs = [root]
        i = 0
        while bfs[i]:
            bfs.append(bfs[i].left)
            bfs.append(bfs[i].right)
            i += 1
        return not any(bfs[i:])
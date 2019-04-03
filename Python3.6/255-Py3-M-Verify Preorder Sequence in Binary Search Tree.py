# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 21:17:24 2019

@author: hjiang
"""

"""
Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.

You may assume each number in the sequence is unique.

Consider the following binary search tree: 

     5
    / \
   2   6
  / \
 1   3
Example 1:

Input: [5,2,6,1,3]
Output: false
Example 2:

Input: [5,2,1,3,6]
Output: true
Follow up:
Could you do it using only constant space complexity?
https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/discuss/68197/AC-Python-O(n)-time-O(1)-extra-space
http://www.cnblogs.com/grandyang/p/5327635.html
根据二叉搜索树的性质，当前节点的值一定大于其左子树中任何一个节点值，而且其右子树中的任何一个节点值都不能小于当前节点值，
那么我们可以用这个性质来验证，举个例子，比如下面这棵二叉搜索树：

     5
    / \
   2   6
  / \
 1   3
其先序遍历的结果是{5, 2, 1, 3, 6}, 我们先设一个最小值low，然后遍历数组，如果当前值小于这个最小值low，
返回false，对于根节点，我们将其压入栈中，然后往后遍历，如果遇到的数字比栈顶元素小，说明是其左子树的点，
继续压入栈中，直到遇到的数字比栈顶元素大，那么就是右边的值了，我们需要找到是哪个节点的右子树，
所以我们更新low值并删掉栈顶元素，然后继续和下一个栈顶元素比较，如果还是大于，则继续更新low值和删掉栈顶，
直到栈为空或者当前栈顶元素大于当前值停止，压入当前值，这样如果遍历完整个数组之前都没有返回false的话，
最后返回true即可，参见代码如下：
"""
class Solution:
    # O(n),O(n)
    def verifyPreorder(self, preorder):#这个比较容易懂，但是需要place O(n)
        stack = []
        lower = -1 << 31
        for x in preorder:
            if x < lower:#如果新来的比lower还小，那么证明搞错了
                return False
            while stack and x > stack[-1]:#这个时候遇到右边的值了，持续弹出最后一个，更新lower
                lower = stack.pop()
            stack.append(x)  #遇到左边的节点就持续压入，就是小于的话一直持续压入
        return True
    
    # O(n),O(1)
    def verifyPreorder1(self, preorder):#这种inplace的比较难理解，但是符合题意
        # stack = preorder[:i], reuse preorder as stack
        lower = -1 << 31
        i = 0
        for x in preorder:
            if x < lower:
                return False
            while i > 0 and x > preorder[i - 1]:#循环耗尽大的数字
                lower = preorder[i - 1]
                i -= 1
            preorder[i] = x
            i += 1
        return True
    
if __name__ == "__main__":
    print(Solution().verifyPreorder1([5,2,1,3,6]))














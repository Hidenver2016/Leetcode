# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 15:48:41 2019

@author: hjiang
"""

"""
Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

Example 1:

Input: s1 = "great", s2 = "rgeat"
Output: true
Example 2:

Input: s1 = "abcde", s2 = "caebd"
Output: false
这个题某种意义上来说就是让我们来判断两棵二叉树是否能够通过翻转某些子树而互相得到，
也就是951. Flip Equivalent Binary Trees翻转二叉树子节点的题目。这个题不过是把树变成了字符串而已。

这个题的重点之一就是要合理的划分字符串从而形成两棵不同的左右子树，进而对左右子树递归。
因为事先不知道在哪里进行分割，所以直接对每个可以划分的位置进行遍历分割。判断是否两个子串能否通过翻转变成相等的时候，
需要保证传给函数的子串长度是相同的。因此：

第一：s1的[0:i]和s2[0:i]作为左子树，s1[i:N]和s2[i:N]作为右子树
第二：s1的[0:i]和s2[N - i:N]作为左子树，s1的[i:N]和s2[0:N-i]作为右子树

其中左子树的两个字符串的长度都是i,右子树的两个字符串的长度都是N - i.如果上面两种情况有一种能够成立，
则源字符串s1能够变成s2。

由于使用了递归，所以终止条件一定要写，很简单的对长度是0、长度是1、两个字符串排序之后是否相等进行判断。

原文：https://blog.csdn.net/fuxuemingzhu/article/details/84950326
951. Flip Equivalent Binary Trees翻转二叉树子节点的题目 
关于dfs或者recursive的题目还是需要仔细学习一下
"""

class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        N = len(s1)
        if N == 0: return True
        if N == 1: return s1 == s2
        if sorted(s1) != sorted(s2):
            return False
        for i in range(1, N):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):#这里的gr, rg
                return True
            elif self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):#跑到这里反过来了，变成 gg, rr. 
                return True #比较s1前面i个数和s2后面i个数，以及s1后面n-i个数和s2前面n-i个数
        return False
    
if __name__ =="__main__":
    print(Solution().isScramble("great","rgeat"))


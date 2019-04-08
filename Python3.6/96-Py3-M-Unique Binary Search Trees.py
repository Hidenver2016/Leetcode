# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 11:13:48 2019

@author: hjiang
"""

"""
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
https://blog.csdn.net/fuxuemingzhu/article/details/79367789
记忆化递归
思路：从1...n中找出一个i作为根节点，比i小的数1...i-1作为左子树，比i大的数i+1...n作为右子树，左子树的排列和右子树的排列的乘积是此时的数目。

因为直接递归会超时，所以加上了记忆化搜索的方法，这样就快的多了。
"""
class Solution(object):
    def __init__(self):
        self.dp = dict()
    
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in self.dp:
            return self.dp[n]
        if n == 0 or n == 1:
            return 1
        ans = 0
        for i in range(1, n + 1):
            ans += self.numTrees(i - 1) * self.numTrees(n - i)
        self.dp[n] = ans
        return ans

"""
动态规划
同样是上面的思路，如果使用动态规划去做，可以设dp[i]是i个节点的二叉树有多少种组合。
那么，很明显和上面解法一样的，dp[i]等于左子树有0个节点，左子树有1个节点，左子树有2个节点……等等情况下的和。
对于左右子树的组合方式是独立事件，所以总的组合数是左右子树相乘的关系。

给定一个数n，求1到n这些数可以构成多少棵二叉树。
给定一个序列1.....n，为了构造所有二叉树，我们可以使用1......n中的每一个数i作为根节点，自然1......(i-1)必然位于树的左子树中，(i+1).....n位于树的右子树中。然后可以递归来构建左右子树，由于根节点是唯一的，所以可以保证构建的二叉树都是唯一的。

使用两个状态来记录：

G(n)：长度为n的序列的所有唯一的二叉树。

F(i,n)，1<=i<=n：以i作为根节点的二叉树的数量。

G(n)就是我们要求解的答案，G(n)可以由F(i,n)计算而来。

G(n)=F(1,n)+F(2,n)+...+F(n,n)                           (1)

G(0)=1,G(1)=1

对于给定的一个序列1.....n，我们取i作为它的根节点，那么以i作为根节点的二叉树的数量F(i)可以由下面的公式计算而来：

F(i,n)=G(i-1)*G(n-i) 1<=i<=n                            (2)

综合公式（1）和公式（2），可以看出：

G(n) = G(0) * G(n-1) + G(1) * G(n-2) + … + G(n-1) * G(0)

这就是上面这个问题的答案。
--------------------- 

原文：https://blog.csdn.net/fuxuemingzhu/article/details/79367789 

"""

# Time:  O(n)
# Space: O(1)

class Solution1(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1

        def combination(n, k):
            count = 1
            # C(n, k) = (n) / 1 * (n - 1) / 2 ... * (n - k + 1) / k
            for i in range(1, k + 1):
                count = count * (n - i + 1) / i;
            return count

        return combination(2 * n, n) - combination(2 * n, n - 1)
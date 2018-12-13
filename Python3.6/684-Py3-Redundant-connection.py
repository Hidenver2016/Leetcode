# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 16:58:44 2018

@author: hjiang
"""

"""
In this problem, a tree is an undirected graph that is connected and has no cycles.

The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), 
with one additional edge added. The added edge has two different vertices chosen from 1 to N, 
and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] with u < v, 
that represents an undirected edge connecting nodes u and v.

Return an edge that can be removed so that the resulting graph is a tree of N nodes. 
If there are multiple answers, return the answer that occurs last in the given 2D-array. 
The answer edge [u, v] should be in the same format, with u < v.

Example 1:
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given undirected graph will be like this:
  1
 / \
2 - 3
Example 2:
Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
Output: [1,4]
Explanation: The given undirected graph will be like this:
5 - 1 - 2
    |   |
    4 - 3
Note:
The size of the input 2D-array will be between 3 and 1000.
Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.

注意：在solution中间定义函数，直接的定义需要参数self, 间接的不需要，注意此题的两个版本的写法。
貌似定义在里面（前面一种）还会快一些
此题的知识点是并查集，union-find algorithms
"""
# Time:  O(nlog*n) ~= O(n), n is the length of the positions
# Space: O(n)

class Solution0:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        tree = [-1] * (len(edges) + 1)
        
        def findRoot(x, tree):#并查集，寻找root
            if tree[x] == -1: return x
            else:
                root = findRoot(tree[x], tree)#路径压缩
                tree[x] = root #逐个把路径修改了，全都改成一个集合的代表数字
                return root

        for edge in edges: #找一条边的两个端点的root
            a = findRoot(edge[0], tree)
            b = findRoot(edge[1], tree)
            if a != b:
                tree[a] = b#都找到最大或者最后出现的数字为代表一个集合的数字，或者是root
            else:
                return edge


class UnionFind(object):
    def __init__(self, n):
        self.set = range(n)
        self.count = n

    def find_set(self, x):
        if self.set[x] != x:
            self.set[x] = self.find_set(self.set[x])  # path compression.
        return self.set[x]

    def union_set(self, x, y):
        x_root, y_root = map(self.find_set, (x, y))
        if x_root == y_root:
            return False
        self.set[min(x_root, y_root)] = max(x_root, y_root)
        self.count -= 1
        return True


class Solution1(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        union_find = UnionFind(len(edges)+1)
        for edge in edges:
            if not union_find.union_set(*edge):
                return edge
        return []

if __name__ == "__main__":
#    print(Solution0().findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]]))
    print(Solution0().findRedundantConnection([[1,2], [2,3], [1,3]]))
    
    
#class Solution:
#    def findRedundantConnection(self, edges):
#        """
#        :type edges: List[List[int]]
#        :rtype: List[int]
#        """
#        tree = [-1] * (len(edges) + 1)
#        for edge in edges:
#            a = self.findRoot(edge[0], tree)
#            b = self.findRoot(edge[1], tree)
#            if a != b:
#                tree[a] = b
#            else:
#                return edge
#
#
#    def findRoot(self, x, tree):
#        if tree[x] == -1: return x
#        else:
#            root = self.findRoot(tree[x], tree)
#            tree[x] = root
#            return root
    
    
    
    
    
    
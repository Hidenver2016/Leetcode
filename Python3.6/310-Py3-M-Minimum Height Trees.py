# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 15:08:15 2019

@author: hjiang
"""
"""
For an undirected graph with tree characteristics, we can choose any node as the root. 
The result graph is then a rooted tree. Among all possible rooted trees, 
those with minimum height are called minimum height trees (MHTs). 
Given such a graph, write a function to find all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n 
and a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, 
[0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example 1 :

Input: n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3 

Output: [1]
Example 2 :

Input: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5 

Output: [3, 4]
Note:

According to the definition of tree on Wikipedia: “a tree is an undirected graph in which any two vertices 
are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.”
The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

https://leetcode.com/problems/minimum-height-trees/discuss/76055/Share-some-thoughts
思路，从最外面开始bfs，一层层往里面剥
https://leetcode.com/problems/minimum-height-trees/discuss/76132/Iterative-remove-leaves-Python-solution
"""
import collections
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        d = collections.defaultdict(set)
        for u, v in edges:
            d[u].add(v)
            d[v].add(u)
        s = set(range(n))
        while len(s) > 2:
            leaves = set(i for i in s if len(d[i]) == 1)#每次都找连接点为1的，这样肯定是叶子
            s -= leaves
            for i in leaves:#接下来就是移除leaves
                for j in d[i]:
                    d[j].remove(i)
        return list(s)
    
if __name__ == "__main__":
    print(Solution().findMinHeightTrees(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]))
    
    
    
    
    
    
    
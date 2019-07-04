# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 14:42:40 2019

@author: hjiang
"""

"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes),
 write a function to find the number of connected components in an undirected graph.

Example 1:

Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4 

Output: 2
Example 2:

Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

     0           4
     |           |
     1 --- 2 --- 3

Output:  1
Note:
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, 
[0, 1] is the same as [1, 0] and thus will not appear together in edges.
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/discuss/77638/Python-DFS-BFS-Union-Find-solutions
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/discuss/77625/Short-Union-Find-in-Python-Ruby-C%2B%2B

找出有几个枝
"""
class Solution:#这个union-find最快
    def countComponents(self, n, edges):
        p = [i for i in range(n)]#python 2 此处可以写 p = range(n), 但是python3不行
        def find(v):
            if p[v] != v:
                p[v] = find(p[v])
            return p[v]
        for v, w in edges:
            p[find(v)] = find(w)
#            print(p)
#        print(list(map(find,p)))
        return len(set(map(find, p)))
    
    
if __name__ == "__main__":
    edges = [[0, 1], [1, 2], [3, 4]]
    print(Solution().countComponents(5,edges))
    
    
    
    
    
    
    
    
    
    
    
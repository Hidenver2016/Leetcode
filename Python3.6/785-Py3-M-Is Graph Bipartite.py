# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 00:55:33 2020

@author: hjiang
"""

"""
Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split it's set of nodes into 
two independent subsets A and B such that every edge in the graph has one node in A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes 
j for which the edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.  
There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.

Example 1:
Input: [[1,3], [0,2], [1,3], [0,2]]
顶点0和顶点1，3相连，顶点1和顶点0，2相连，顶点2和结点1，3相连，顶点3和顶点0，2相连。
Output: true
Explanation: 
The graph looks like this:
0----1
|    |
|    |
3----2
We can divide the vertices into two groups: {0, 2} and {1, 3}.
Example 2:
Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
Output: false
Explanation: 
The graph looks like this:
0----1
| \  |
|  \ |
3----2
We cannot find a way to divide the set of nodes into two independent subsets.
 

Note:

graph will have length in range [1, 100].
graph[i] will contain integers in range [0, graph.length - 1].
graph[i] will not contain i or duplicate values.
The graph is undirected: if any element j is in graph[i], then i will be in graph[j].
"""
"""
    2nd approach: recursive DFS + nodes coloring

    Time    O(V+E)
    Space   O(V+E)
    164 ms, faster than 40.67%
"""


class Solution(object):
    def isBipartite(self, graph):# 实测 dfs快，看这个
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        seen = {}
        # we need to check every node because it is possible that graph[0] doesn't have any vertices connected
        for i in range(len(graph)):
            if i not in seen:
                if self.check(graph, i, 1, seen) == False:
                    return False
        return True

    def check(self, graph, node, color, seen):
        if node in seen:
            if seen[node] != color:
                return False
            return True
        seen[node] = color
        vertices = graph[node]
        for v in vertices:
            if self.check(graph, v, -color, seen) == False:
                return False
        return True

"""
    1st approach: BFS + nodes coloring

    Time    O(V+E)
    Space   O(V+E)
    156 ms, faster than 62.09%
"""


class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        seen = {}
        # we need to check every node because it is possible that graph[0] doesn't have any vertices connected
        for i in range(len(graph)):
            if i not in seen:
                if self.check(graph, i, seen) == False:
                    return False
        return True

    def check(self, graph, start, seen):
        q = [(start, 1)]
        while len(q) > 0:
            pop, color = q.pop(0)
            if pop in seen:
                if seen[pop] != color:
                    return False
                continue
            seen[pop] = color
            vertices = graph[pop]
            for v in vertices:
                q.append((v, -color))
        return True



    
    
    
    
    
    
    
    
    
    
    
    
    
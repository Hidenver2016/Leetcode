# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 14:21:59 2019

@author: hjiang
"""

"""
Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), 
write a function to check whether these edges make up a valid tree.

Example 1:

Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true
Example 2:

Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false
Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, 
[0,1] is the same as [1,0] and thus will not appear together in edges.
找出树是不是valid


其实还有BFS和DFS
我们再来看Union Find的方法，这种方法对于解决连通图的问题很有效，思想是我们遍历节点，
如果两个节点相连，我们将其roots值连上，这样可以帮助我们找到环，
我们初始化roots数组为-1，然后对于一个pair的两个节点分别调用find函数，得到的值如果相同的话，则说明环存在，返回false，
不同的话，我们将其roots值union上，参见代码如下：


此题在重做的时候还要写BFS和DFS
"""

    
class Solution:#这个union-find最快, 自己写的，优先看，和323一模一样
    def validTree(self, n, edges):
        p = [i for i in range(n)]#python 2 此处可以写 p = range(n), 但是python3不行
        def find(v):
            if p[v] != v:
                p[v] = find(p[v])
            return p[v]
        for v, w in edges:
            p[find(v)] = find(w)
#            print(p)
#        print(list(map(find,p)))
        if len(set(map(find, p))) == 1 and len(edges) == n -1: return True
        else:
            return False
        
class Solution1:
    def validTree(self, n, edges):
        parent = [i for i in range(n)]
        def find(x):#这里的find(x)实际上是指找到x最后的自己节点
            return x if parent[x] == x else find(parent[x])
        for e in edges:
            x, y = map(find, e)
            if x == y:
                return False
            parent[x] = y# x是y的root
        return len(edges) == n - 1
        

if __name__ == "__main__":
    edges = [[0,1], [0,2], [0,3], [1,2]]
    n = 5
    print(Solution().validTree(n, edges))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 19:38:42 2018

@author: hjiang
"""

"""
Equations are given in the format A / B = k, where A and B are variables represented as strings, 
and k is a real number (floating point number). Given some queries, return the answers. 
If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0. 
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? . 
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, 
vector<pair<string, string>> queries , where equations.size() == values.size(), 
and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
The input is always valid. You may assume that evaluating the queries will result 
in no division by zero and there is no contradiction.

Space: O(e+q*e)
Time: O(e)

此题是图加上DFS，尤其注意中间变量的处理
"""

#https://zxi.mytechroad.com/blog/graph/leetcode-399-evaluate-division/

import collections
class Solution:
  def calcEquation(self, equations, values, queries):
    def divide(x, y, visited):#这个函数的意思就是从g[x]中寻找中间变脸n,让n与y相连。如果n，不行，那么继续寻找g[n]中的中间变量，让其与y相连
      if x == y: 
          return 1.0
      visited.add(x) # 记住访问过的
      for n in g[x]: # n就是中间变量
        if n in visited: #避免自己除以自己，形成无限循环
            continue
        visited.add(n)
        d = divide(n, y, visited)
        if d > 0: 
            return d * g[x][n]
      return -1.0
#defaultdict(<class 'dict'>, {'a': {'b': 2.0}, 'b': {'a': 0.5, 'c': 3.0}, 'c': {'b': 0.3333333333333333}})    
    g = collections.defaultdict(dict)
    for (x, y), v in zip(equations, values):      
      g[x][y] = v
      g[y][x] = 1.0 / v
    ans = []
    for x, y in queries:
        if x in g and y in g:
            ans.append(divide(x, y, set()))
        else:
            ans.append( -1)
    return ans
    
#    ans = [divide(x, y, set()) if x in g and y in g else -1 for x, y in queries]
#    return ans

if __name__ == "__main__":
    print(Solution().calcEquation([ ["a", "b"], ["b", "c"] ], [2.0, 3.0], 
          [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]))
    
    
    
    
    
    
    
    
    
    
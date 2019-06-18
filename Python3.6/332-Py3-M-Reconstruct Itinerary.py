# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 16:24:48 2019

@author: hjiang
"""

"""
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to],
 reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. 
 Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that has 
the smallest lexical order when read as a single string. For example, 
the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.
"""
#https://blog.csdn.net/fuxuemingzhu/article/details/83551204
#https://www.youtube.com/watch?v=4udFSOWQpdg
"""
这道题目比较难，就是把带环的有向图变成数，用贪心加后序遍历访问，访问过的边就删除
详细过程需要参考花花的讲义



最坏时间复杂度是O(VlogV)，空间复杂度是O(E).
"""


import collections

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = collections.defaultdict(list)
        for frm, to in tickets:
            graph[frm].append(to)
        for frm, tos in graph.items():
            tos.sort(reverse=True)#在这里先反向，因为后面是后序查找，找出来也是反向的，最后才能保证是正向的（看花花的图）
        res = []
        self.dfs(graph, "JFK", res)
        return res[::-1]#最后，因为是后序遍历，所以结果要反一下，才是正确的

    def dfs(self, graph, source, res):
        while graph[source]:
            v = graph[source].pop()
            self.dfs(graph, v, res)
        res.append(source)


if __name__ == "__main__":
    Input = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    print(Solution().findItinerary(Input))











# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 16:06:04 2018

@author: hjiang
"""

"""
We have a list of bus routes. Each routes[i] is a bus route that the i-th bus repeats forever. 
For example if routes[0] = [1, 5, 7], this means that the first bus (0-th indexed) 
travels in the sequence 1->5->7->1->5->7->1->... forever.

We start at bus stop S (initially not on a bus), and we want to go to bus stop T. 
Travelling by buses only, what is the least number of buses we must take to reach our destination? 
Return -1 if it is not possible.

Example:
Input: 
routes = [[1, 2, 7], [3, 6, 7]]
S = 1
T = 6
Output: 2
Explanation: 
The best strategy is take the first bus to the bus stop 7, 
then take the second bus to the bus stop 6.
Note:

1 <= routes.length <= 500.
1 <= routes[i].length <= 500.
0 <= routes[i][j] < 10 ^ 6.

关键：这种图形的题目都比较死板，先开始建立图形，然后搜索就可以了
Time： O(m*n)
Space： O(m*n)
"""
# Reference: https://leetcode.com/problems/bus-routes/discuss/122712/Simple-Java-Solution-using-BFS
from collections import deque
class Solution0:
    # This is a very good BFS problem.
    # In BFS, we need to traverse all positions in each level firstly, and then go to the next level.
    # Our task is to figure out:
    # 1. What is the level in this problem?
    # 2. What is the position we want in this problem?
    # 3. How to traverse all positions in a level?
    # 
    # For this problem:
    # 1. The level is each time to take bus.
    # 2. The position is all of the stops you can reach for taking one time of bus.
    # 3. Using a queue to record all of the stops can be arrived for each time you take buses.
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        # You already at the terminal, so you needn't take any bus.
        if S == T: return 0
        
        # You need to record all the buses you can take at each stop so that you can find out all
        # of the stops you can reach when you take one time of bus.
        # the key is stop and the value is all of the buses you can take at this stop.
        stopBoard = {} #{1: [0], 2: [0], 7: [0, 1], 3: [1], 6: [1]}
        for bus, stops in enumerate(routes):
            for stop in stops:
                if stop not in stopBoard:
                    stopBoard[stop] = [bus]
                else:
                    stopBoard[stop].append(bus)
        
        # The queue is to record all of the stops you can reach when you take one time of bus.
        queue = deque([S])
        # Using visited to record the buses that have been taken before, because you needn't to take them again.
        visited = set()

        res = 0
        while queue:
            # take one time of bus.
            res += 1
            # In order to traverse all of the stops you can reach for this time, you have to traverse
            # all of the stops you can reach in last time.
            pre_num_stops = len(queue)
            for _ in range(pre_num_stops):
                curStop = queue.popleft()
                # Each stop you can take at least one bus, you need to traverse all of the buses at this stop
                # in order to get all of the stops can be reach at this time.
                for bus in stopBoard[curStop]:#{1: [0], 2: [0], 7: [0, 1], 3: [1], 6: [1]}
                    # if the bus you have taken before, you needn't take it again.
                    if bus in visited: continue
                    visited.add(bus)
                    for stop in routes[bus]:
                        if stop == T: return res
                        queue.append(stop)
        return -1
"""
The first part loop on routes and record stop to routes mapping in to_route.
The second part is general bfs. Take a stop from queue and find all connected route.
The set seen record all stops visted and we won't check a stop for twice.
We can also use a set to record all routes visted , or just clear a route after visit.
"""
   
import collections    
class Solution1:
    def numBusesToDestination(self, routes, S, T):
        to_routes = collections.defaultdict(set) #defaultdict(<class 'set'>, {1: {0}, 2: {0}, 7: {0, 1}, 3: {1}, 6: {1}})
        for i,route in enumerate(routes):
            for j in route: to_routes[j].add(i)
        bfs = [(S,0)]
        seen = set([S])# all stops visited
        for stop, bus in bfs:
            if stop == T: return bus
            for route_i in to_routes[stop]:
                for next_stop in routes[route_i]:
                    if next_stop not in seen:
                        bfs.append((next_stop, bus+1))
                        seen.add(next_stop)
                routes[route_i] = [] # clear after visit
        return -1
    
if __name__ == "__main__":
    print(Solution0().numBusesToDestination([[1, 2, 7], [3, 6, 7]], 1, 6))
    
    
   
    
    
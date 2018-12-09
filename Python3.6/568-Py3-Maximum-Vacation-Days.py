# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 16:21:49 2018

@author: hjiang
"""

"""
LeetCode wants to give one of its best employees the option to travel among N cities 
to collect algorithm problems. But all work and no play makes Jack a dull boy, 
\you could take vacations in some particular cities and weeks. Your job is to schedule 
the traveling to maximize the number of vacation days you could take, 
but there are certain rules and restrictions you need to follow.

Rules and restrictions:
You can only travel among N cities, represented by indexes from 0 to N-1. 
Initially, you are in the city indexed 0 on Monday.
The cities are connected by flights. The flights are represented as 
a N*N matrix (not necessary symmetrical), called flights representing the airline status 
from the city i to the city j. If there is no flight from the city i to the city j, 
flights[i][j] = 0; Otherwise, flights[i][j] = 1. Also, flights[i][i] = 0 for all i.
You totally have K weeks (each week has 7 days) to travel. You can only take flights 
at most once per day and can only take flights on each week's Monday morning. 
Since flight time is so short, we don't consider the impact of flight time.
For each city, you can only have restricted vacation days in different weeks, 
given an N*K matrix called days representing this relationship. For the value of days[i][j], 
it represents the maximum days you could take vacation in the city i in the week j.
You're given the flights matrix and days matrix, and you need to output 
the maximum vacation days you could take during K weeks.

Example 1:
Input:flights = [[0,1,1],[1,0,1],[1,1,0]], days = [[1,3,1],[6,0,3],[3,3,3]]
Output: 12
Explanation: 
Ans = 6 + 3 + 3 = 12. 

One of the best strategies is:
1st week : fly from city 0 to city 1 on Monday, and play 6 days and work 1 day. 
(Although you start at city 0, we could also fly to and start at other cities since it is Monday.) 
2nd week : fly from city 1 to city 2 on Monday, and play 3 days and work 4 days.
3rd week : stay at city 2, and play 3 days and work 4 days.
Example 2:
Input:flights = [[0,0,0],[0,0,0],[0,0,0]], days = [[1,1,1],[7,7,7],[7,7,7]]
Output: 3
Explanation: 
Ans = 1 + 1 + 1 = 3. 

Since there is no flights enable you to move to another city, you have to stay at city 0 for the whole 3 weeks. 
For each week, you only have one day to play and six days to work. 
So the maximum number of vacation days is 3.
Example 3:
Input:flights = [[0,1,1],[1,0,1],[1,1,0]], days = [[7,0,0],[0,7,0],[0,0,7]]
Output: 21
Explanation:
Ans = 7 + 7 + 7 = 21

One of the best strategies is:
1st week : stay at city 0, and play 7 days. 
2nd week : fly from city 0 to city 1 on Monday, and play 7 days.
3rd week : fly from city 1 to city 2 on Monday, and play 7 days.
Note:
N and K are positive integers, which are in the range of [1, 100].
In the matrix flights, all the values are integers in the range of [0, 1].
In the matrix days, all the values are integers in the range [0, 7].
You could stay at a city beyond the number of vacation days, but you should work on the extra days, 
which won't be counted as vacation days.
If you fly from the city A to the city B and take the vacation on that day, 
the deduction towards vacation days will count towards the vacation days of city B in that week.
We don't consider the impact of flight hours towards the calculation of vacation days.
"""

"""
Let's maintain best[i], the most vacation days you can have ending in city i on week t. 
At the end, we simply want max(best), the best answer for any ending city.

For every flight i -> j (including staying in the same city, when i == j), 
we have a candidate answer best[j] = best[i] + days[j][t], and we want the best answer of those.

When the graph is sparse, we can precompute flights_available[i] = [j for j, adj in enumerate(flights[i]) if adj or i == j] 
instead to save some time, but this is not required.
"""

#http://www.cnblogs.com/grandyang/p/6919389.html
#https://leetcode.com/problems/maximum-vacation-days/discuss/102680/Python-Simple-with-Explanation
# Time:  O(n^2 * k)
# Space: O(k)
"""
下面这种方法优化了空间复杂度，只用了一个一维的DP数组，其中dp[i]表示在当前周，在城市i时已经获得的最大假期数，
并且除了第一个数初始化为0，其余均初始化为整型最小值，然后我们从第一周往后遍历，我们新建一个临时数组t，
初始化为整型最小值，然后遍历每一个城市，对于每一个城市，我们遍历其他所有城市，看是否有飞机能直达当前城市，
或者就是当前的城市，我们用dp[p] + days[i][j]来更更新dp[i]，当每个城市都遍历完了之后，我们将t整个赋值给dp，
然后进行下一周的更新，最后只要在dp数组中找出最大值返回即可，这种写法不但省空间，而且也相对简洁一些，很赞啊～
"""

class Solution(object):
    def maxVacationDays(self, flights, days):
        """
        :type flights: List[List[int]]
        :type days: List[List[int]]
        :rtype: int
        """
        N, K = len(days), len(days[0])# N cities, K weeks
        dp = [0] + [-1] * (N - 1)#dp[i]表示在当前周，在城市i时已经获得的最大假期数
        for w in range(K):
            ndp = [x for x in dp]
#            ndp = [float('-inf') for _ in range(N)]
            for sc in range(N):#遍历所有城市
                if dp[sc] < 0: 
                    continue
                for tc in range(N):
                    if sc == tc or flights[sc][tc]:# 只有航班存在或者不动，才可以更新
                        ndp[tc] = max(ndp[tc], dp[sc] + days[tc][w])
            dp = ndp#下一周的更新
        return max(dp)
    

class Solution1(object):
    def maxVacationDays(self, flights, days):
        """
        :type flights: List[List[int]]
        :type days: List[List[int]]
        :rtype: int
        """
        n, k = len(days), len(days[0]) # n cities, k weeks
        max_vacation = [0] + [float('-inf') for _ in range(n-1)]

        for week in range(k):
            curr = [float('-inf') for _ in range(n)]

            for dep_city in range(n):
                for arr_city, flight_exists in enumerate(flights[dep_city]):
                    if flight_exists or dep_city == arr_city:
                        curr[arr_city] = max(curr[arr_city], max_vacation[dep_city] + days[arr_city][week])

            max_vacation = curr

        return max(max_vacation)

if __name__ == "__main__":
    print(Solution().maxVacationDays([[0,1,1],[1,0,1],[1,1,0]], [[1,3,1],[6,0,3],[3,3,3]]))


















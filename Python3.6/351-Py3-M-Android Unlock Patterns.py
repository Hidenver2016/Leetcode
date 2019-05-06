# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 18:01:14 2019

@author: hjiang
"""

"""
Given an Android 3x3 key lock screen and two integers m and n, where 1 ≤ m ≤ n ≤ 9, 
count the total number of unlock patterns of the Android lock screen, 
which consist of minimum of m keys and maximum n keys.

 

Rules for a valid pattern:

Each pattern must connect at least m keys and at most n keys.
All the keys must be distinct.
If the line connecting two consecutive keys in the pattern passes through any other keys, 
the other keys must have previously selected in the pattern. No jumps through non selected key is allowed.
The order of keys used matters.

Explanation:

| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |
Invalid move: 4 - 1 - 3 - 6 
Line 1 - 3 passes through key 2 which had not been selected in the pattern.

Invalid move: 4 - 1 - 9 - 2
Line 1 - 9 passes through key 5 which had not been selected in the pattern.

Valid move: 2 - 4 - 1 - 3 - 6
Line 1 - 3 is valid because it passes through key 2, which had been selected in the pattern

Valid move: 6 - 5 - 4 - 1 - 9 - 2
Line 1 - 9 is valid because it passes through key 5, which had been selected in the pattern.

 

Example:

Input: m = 1, n = 1
Output: 9
"""

#https://leetcode.com/problems/android-unlock-patterns/discuss/82460/Python-BFS-solution-short-easy-to-understand
class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        skip = {}
        
        skip[(1,7)] = 4
        skip[(1,3)] = 2
        skip[(1,9)] = 5
        skip[(2,8)] = 5
        skip[(3,7)] = 5
        skip[(3,9)] = 6
        skip[(4,6)] = 5
        skip[(7,9)] = 8
        self.res = 0
        def helper(used, last):
            if len(used) >= m:
                self.res += 1
            if len(used) == n:
                return
            for j in range(1, 10):
                if j not in used:   # if j is not used
                    # Sort the vertices of the edge to search in skip
                    edge = (min(last, j), max(last, j))#去掉重复的edge
                    if edge not in skip or skip[edge] in used: #used的点只过一次
                        helper(used + [j], j)
        for i in range(1, 10):
            helper([i], i)
        return self.res
    
#https://leetcode.com/problems/android-unlock-patterns/discuss/131737/Python-easy-readable-DFS-solution-with-clear-explaination
"""
The basic idea is starting from an arbitrary digit (prev), search all the valid next digit. 
Use a set/dict (visited) to store all the visited digits. What is the invalid combination? Only two cases.

if prev in {1, 3, 7, 9} and next in {1, 3, 7, 9}, however, (prev + next)/2 not in visited. e.g. 1 -> 7 and 4 not visited.
if prev in {2, 4, 6, 8} and next == 10 - prev, however, 5 is not in visited. e.g. 2->8 and 5 not visited.
"""        
class Solution1(object):#看这个把，这个需要记住，太不好搞了
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        visited = {}
        self.res = 0
        self.corner = {1,3,7,9}
        self.mid = {2,4,6,8}
        for i in range(1, 10):
            visited[i] = 1#表示访问过了，因为接下来马上就会访问
            self.dfsHelper(visited, 1, m, n, i)
            del visited[i]#用过之后对于新的密码，删除表示没有访问过
        return self.res
        
    def dfsHelper(self, visited, index, m, n, prev):
        if m <= index <= n:
            self.res += 1
        if index == n:
            return
        for next in range(1, 10):
            if next not in visited:
                if prev in self.corner and next in self.corner and (prev + next)/2 not in visited:
                    continue
                elif prev in self.mid and next == (10 - prev) and 5 not in visited:
                    continue
                visited[next] = 1
                self.dfsHelper(visited, index + 1, m, n, next)
                del visited[next]
    
    
if __name__ == "__main__":
    print(Solution().numberOfPatterns(1,2))    
    
    
    
    
    
    
    
    
    
    
    
    
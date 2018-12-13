# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 17:22:20 2018

@author: hjiang
"""

"""
Given the running logs of n functions that are executed in a nonpreemptive single threaded CPU, 
find the exclusive time of these functions.

Each function has a unique id, start from 0 to n-1. 
A function may be called recursively or by another function.

A log is a string has this format : function_id:start_or_end:timestamp. 
For example, "0:start:0" means function 0 starts from the very beginning of time 0. 
"0:end:0" means function 0 ends to the very end of time 0.

Exclusive time of a function is defined as the time spent within this function, 
the time spent by calling other functions should not be considered as this function's exclusive time. 
You should return the exclusive time of each function sorted by their function id.

Example 1:
Input:
n = 2
logs = 
["0:start:0",
 "1:start:2",
 "1:end:5",
 "0:end:6"]
Output:[3, 4]
Explanation:
Function 0 starts at time 0, then it executes 2 units of time and reaches the end of time 1. 
Now function 0 calls function 1, function 1 starts at time 2, executes 4 units of time and end at time 5.
Function 0 is running again at time 6, and also end at the time 6, thus executes 1 unit of time. 
So function 0 totally execute 2 + 1 = 3 units of time, and function 1 totally execute 4 units of time.
Note:
Input logs will be sorted by timestamp, NOT log id.
Your output should be sorted by function id, which means the 0th element of your 
output corresponds to the exclusive time of function 0.
Two functions won't start or end at the same time.
Functions could be called recursively, and will always end.
1 <= n <= 100

关键：这个题目很直接，直接用stack保存程序的开始时间，然后在结束的时候逐个弹出就可以了。
主要原因是因为是单进程，所以程序必须是最后开始的程序最先结束
"""

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        result = [0] * n
        stk, prev = [], 0
        for log in logs:
            tokens = log.split(":")
            if tokens[1] == "start":#因为是单进程，所以遇到start,之前的程序就挂起
                if stk:#如果里面有其他进程就计算时间
                    result[stk[-1]] += int(tokens[2]) - prev
                stk.append(int(tokens[0]))
                prev = int(tokens[2])#一直保持最新程序的开始时间，因为是单进程，所以最先结束的就是最迟开始的进程。
            else:
                result[stk.pop()] += int(tokens[2]) - prev + 1#把stk里面最后的进程弹出，然后计算时间，注意要+1（遇到end要+1）
                prev = int(tokens[2]) + 1#前一个进程的结束时间，也要+1
        return result
        
if __name__ == "__main__":
    n = 2
    logs = ["0:start:0",
            "1:start:2",
            "1:end:5",
            "0:end:6"]
    print(Solution().exclusiveTime(n,logs))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
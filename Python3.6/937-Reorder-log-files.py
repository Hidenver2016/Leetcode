# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 00:11:04 2018

@author: hjiang
"""

"""
You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs. 
It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  
The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  
The digit-logs should be put in their original order.

Return the final order of the logs.

Example 1:

Input: ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]

Note:

0 <= logs.length <= 100
3 <= logs[i].length <= 100
logs[i] is guaranteed to have an identifier, and a word after the identifier.

"""

# time 3n 第一个循环是n, 中间排序是小于nlogn, 最后两个循环之和是n
# space 2n 前两个之和是n,outputs也是n

class solution(object):
    def reorder_log_files(self, inputs):
        output_dig = []
        output_let = []
        outputs = []
        for i in inputs:
            temp = i.split()
            if temp[1].isdigit():
                output_dig.append(i)
            else:
                output_let.append(temp)
                
        output_let.sort(key = lambda x:x[1:])
        for l in output_let:
            temp1 = ' '.join(l)
            outputs.append(temp1)
        for j in output_dig:
            outputs.append(j)
        return outputs
            
            
if __name__ == "__main__":
    print(solution().reorder_log_files(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]))
                






















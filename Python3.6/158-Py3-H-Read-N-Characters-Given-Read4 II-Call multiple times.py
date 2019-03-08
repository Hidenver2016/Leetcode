# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 21:04:41 2018

@author: hjiang
"""
"""
The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

Note:
The read function may be called multiple times.

Example 1: 

Given buf = "abc"
read("abc", 1) // returns "a"
read("abc", 2); // returns "bc"
read("abc", 1); // returns ""
Example 2: 

Given buf = "abc"
read("abc", 4) // returns "abc"
read("abc", 1); // returns ""

"""

# Time:  O(n)
# Space: O(1)

def read4(buf):
    global file_content
    i = 0
    while i < len(file_content) and i < 4:
        buf[i] = file_content[i]
        i += 1

    if len(file_content) > 4:
        file_content = file_content[4:]
    else:
        file_content = ""
    return i

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

#class Solution(object):
#    def __init__(self):
#        self.__buf4 = [''] * 4
#        self.__i4 = 0
#        self.__n4 = 0
#
#    def read(self, buf, n):
#        """
#        :type buf: Destination buffer (List[str])
#        :type n: Maximum number of characters to read (int)
#        :rtype: The number of characters read (int)
#        """
#        i = 0
#        while i < n:
#            if self.__i4 < self.__n4:  # Any characters in buf4.
#                buf[i] = self.__buf4[self.__i4]
#                i += 1
#                self.__i4 += 1
#            else:
#                self.__n4 = read4(self.__buf4)  # Read more characters.
#                if self.__n4:
#                    self.__i4 = 0
#                else:  # Buffer has been empty.
#                    break
#
#        return i
#https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/discuss/49599/My-python-40ms-solution    
class Solution: #看这个，这个比157题增加难度是需要一个self.queue作为中间变量来实现读取一个删除一个
# @param buf, Destination buffer (a list of characters)
# @param n,   Maximum number of characters to read (an integer)
# @return     The number of characters read (an integer)
    def __init__(self):
        self.queue = []#加上这个作为中间变量
    
    def read(self, buf, n):
        idx = 0
        while True:
            buf4 = [""]*4
            l = read4(buf4)#
            self.queue.extend(buf4) #中间变量读入
            curr = min(len(self.queue), n-idx)
            for i in range(curr):
                buf[idx] = self.queue.pop(0)#每次读取都从中间变量中弹出最前面的，第二次读取的话就没有了
                idx+=1
            if curr == 0:
                break 
        return idx
    
if __name__ == "__main__":
    global file_content
    sol = Solution()
    buf = ['' for _ in range(100)]
    file_content = "abcde"
    print (buf[:sol.read(buf, 5)])
    print (buf[:sol.read(buf, 2)])    
    
    
    
    
    
    
    
    
    
    
    
    
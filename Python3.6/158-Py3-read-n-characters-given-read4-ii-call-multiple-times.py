# Time:  O(n)
# Space: O(1)
"""
 The API: int read4(char *buf) reads 4 characters at a time from a file.
 
 The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.
 
 By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.
 
 Note:
 The read function may be called multiple times.


 The read4 API is already defined for you.
 @param buf, a list of characters
 @return an integer

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
# Time:  O(n)
# Space: O(1)

class Solution(object):
    def __init__(self):
        self.__buf4 = [''] * 4 # 一个临时的寄存器用来存放读过的东西
        self.__i4 = 0
        self.__n4 = 0 # 临时寄存器读出的数字，4的整数倍除非 len(file_count)<4
        
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        i = 0
        while i < n:
            if self.__i4 < self.__n4:  # Any characters in buf4.
                buf[i] = self.__buf4[self.__i4] # 读出来的东西在self._Solution__buf4里面
                i += 1 #这两行都是按顺序来读，让指针向后指
                self.__i4 += 1
            else:
                self.__n4 = read4(self.__buf4)  # Read more characters.
                if self.__n4:
                    self.__i4 = 0
                else:  # Buffer has been empty.
                    break
        
        return i

if __name__ == "__main__":
    global file_content
    sol = Solution()
    buf = ['' for _ in range(100)]
    file_content = "abcde"
    print (buf[:sol.read(buf, 5)])
    print (buf[:sol.read(buf, 2)])    

"""
Given a file and assume that you can only read the file using a given method read4, implement a method to read n characters.

 

Method read4:

The API read4 reads 4 consecutive characters from the file, then writes those characters into the buffer array buf.

The return value is the number of actual characters read.

Note that read4() has its own file pointer, much like FILE *fp in C.

Definition of read4:

    Parameter:  char[] buf
    Returns:    int

Note: buf[] is destination not source, the results from read4 will be copied to buf[]
Below is a high level example of how read4 works:

File file("abcdefghijk"); // File is "abcdefghijk", initially file pointer (fp) points to 'a'
char[] buf = new char[4]; // Create buffer with enough space to store characters
read4(buf); // read4 returns 4. Now buf = "abcd", fp points to 'e'
read4(buf); // read4 returns 4. Now buf = "efgh", fp points to 'i'
read4(buf); // read4 returns 3. Now buf = "ijk", fp points to end of file
 

Method read:

By using the read4 method, implement the method read that reads n characters from the file and store it in the buffer array buf. 
Consider that you cannot manipulate the file directly.

The return value is the number of actual characters read.

Definition of read:

    Parameters:	char[] buf, int n
    Returns:	int

Note: buf[] is destination not source, you will need to write the results to buf[]
 

Example 1:

Input: file = "abc", n = 4
Output: 3
Explanation: After calling your read method, buf should contain "abc". We read a total of 3 characters from the file, so return 3. 
Note that "abc" is the file's content, not buf. buf is the destination buffer that you will have to write the results to.
Example 2:

Input: file = "abcde", n = 5
Output: 5
Explanation: After calling your read method, buf should contain "abcde". We read a total of 5 characters from the file, so return 5.
Example 3:

Input: file = "abcdABCD1234", n = 12
Output: 12
Explanation: After calling your read method, buf should contain "abcdABCD1234". We read a total of 12 characters from the file, so return 12.
Example 4:

Input: file = "leetcode", n = 5
Output: 5
Explanation: After calling your read method, buf should contain "leetc". We read a total of 5 characters from the file, so return 5.
 

Note:

Consider that you cannot manipulate the file directly, the file is only accesible for read4 but not for read.
The read function will only be called once for each test case.
You may assume the destination buffer array, buf, is guaranteed to have enough space for storing n characters.

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file

"""




# Time:  O(n)
# Space: O(1)
#
# The API: int read4(char *buf) reads 4 characters at a time from a file.
# 
# The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.
# 
# By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.
# 
# Note:
# The read function will only be called once for each test case.
#

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
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
        
class Solution(object):
#    def read(self, buf, n):
#        """
#        :type buf: Destination buffer (List[str])
#        :type n: Maximum number of characters to read (int)
#        :rtype: The number of characters read (int)
#        """
#        read_bytes = 0
#        buffer = [''] * 4
#        for i in range(n // 4 + 1):
#            size = read4(buffer)
#            if size:
#                buf[read_bytes:read_bytes+size] = buffer
#                read_bytes += size
#            else:
#                break
#        return min(read_bytes, n)
#https://leetcode.com/problems/read-n-characters-given-read4/discuss/49520/Python-solution-with-explainations-and-comments
#这个题目细节比较绕，但是总体就是如何用4个的函数read4来读取任意n个字符    
    def read1(self, buf, n):#看这个
        idx = 0
        while n > 0:
            # read file to buf4
            buf4 = [""]*4
            l = read4(buf4)
            # if no more char in file, return
            if not l: return idx
            # write buf4 into buf directly
            for i in range(min(l, n)):#这里开始是做4的循环（假设需要读的值大于4）,如果小于4,那么表示读到最后了，还是取最小的
                buf[idx] = buf4[i]
                idx += 1
                n -= 1
        return idx

if __name__ == "__main__":
    global file_content
    buf = ['' for _ in range(100)]
#    file_content = "a"
#    print (buf[:Solution().read(buf, 9)])    
    file_content = "abcdefghijk"
#    set_number = Solution().read(buf, 9)
#    print (buf[:set_number])
    print (buf[:Solution().read(buf, 1)])
#    print (buf[:Solution().read(buf, 2)])
    
    
    
    


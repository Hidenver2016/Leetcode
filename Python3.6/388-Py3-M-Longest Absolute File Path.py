# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 16:04:55 2019

@author: hjiang
"""

"""
Suppose we abstract our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
The directory dir contains two sub-directories subdir1 and subdir2. subdir1 
contains a file file1.ext and an empty second-level sub-directory subsubdir1. 
subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path 
to a file within our file system. For example, in the second example above, 
the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the 
length of the longest absolute path to file in the abstracted file system. 
If there is no file in the system, return 0.

Note:
The name of a file contains at least a . and an extension.
The name of a directory or sub-directory will not contain a ..
Time complexity required: O(n) where n is the size of the input string.

Notice that a/aa/aaa/file1.txt is not the longest file path, if there is 
another path aaaaaaaaaaaaaaaaaaaaa/sth.png.
https://blog.csdn.net/fuxuemingzhu/article/details/82841402
题目意思是计算所有目录中，最长的目录是多长
目录： 目录名长度+1
文件： 文件名长度
用栈的思想，一个是目录深度，一个是总长度。每次把新的目录或者文件放在栈的最后，不停的更新也是最后
把一样深或者浅的目录都弹出，这样才能不停保存更深的目录和文件
最后用max不停更新最大值（最大长度）
"""
class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        stack = [(-1, 0)] # 目录的深度，当前总的字符串长度
        max_len = 0
        for p in input.split("\n"):
            depth = p.count('\t')
            p = p.replace('\t', '')#消去空格\t
            while stack and depth <= stack[-1][0]: # 一样深，或者当前目录更浅
                stack.pop()
            if '.' not in p: # 目录
                stack.append((depth, len(p) + stack[-1][1] + 1))#len(p)连点都计算了，是多少个字符
            else: # 文件
                max_len = max(max_len, len(p) + stack[-1][1])
        return max_len
    
class Solution1(object):#这个方法快很多，思路是类似的
    def lengthLongestPath(self, input):
        maxlen = 0
        pathlen = {0: 0}#建立字典，key是深度，value是总长度
        for line in input.splitlines():#和split("\n")是一样的
            name = line.lstrip('\t')
            depth = len(line) - len(name)#对于不同等级的目录，前面的\t不一样，有几个\t就表示深度是几
            if '.' in name:
                maxlen = max(maxlen, pathlen[depth] + len(name))
            else:#这个字典里面的key就是深度
                pathlen[depth + 1] = pathlen[depth] + len(name) + 1#这里采取的是覆盖的方法，不用再弹出了，直接把新的目录长度覆盖就可以了
        return maxlen

if __name__ == "__main__":
    Input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    print(Solution1().lengthLongestPath(Input))
    
    
    
    

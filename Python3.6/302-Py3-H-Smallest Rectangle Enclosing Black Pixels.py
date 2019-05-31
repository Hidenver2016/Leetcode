# -*- coding: utf-8 -*-
"""
Created on Wed May 29 22:54:44 2019

@author: hjiang
"""

"""
An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel. 
The black pixels are connected, i.e., there is only one black region. 
Pixels are connected horizontally and vertically. Given the location (x, y) of one of the black pixels, 
return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.

Example:

Input:
[
  "0010",
  "0110",
  "0100"
]
and x = 0, y = 2

Output: 6
"""
class Solution:
    def minArea(self, image, x, y):
        left, right = y, y
        up, down = x, x
        for i in range(len(image)):
            for j in range(len(image[0])):
                if image[i][j] == '1':
                    left = min(left, j)
                    right = max(right, j)
                    up = min(up, i)
                    down = max(down, i)
                    
        return (down - up + 1) * (right - left + 1)
    
    

    
    
class Solution2:
    def minArea(self, image, x, y):
        l, r, u, d, m, n = [y], [y], [x], [x], len(image), len(image[0])#用list传递是一个方法
        def dfs(i, j):
            if i < u[0]: u[0] = i
            elif i > d[0]: d[0] = i
            if j < l[0]: l[0] = j
            elif j > r[0]: r[0] = j
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and image[x][y] == "1":
                    image[x][y] = "0"
                    dfs(x, y)
        dfs(x, y)
        return (r[0] - l[0] + 1) * (d[0] - u[0] + 1)
    
class Solution3:# 重点要看看值是怎么传递的在dfs里面

    def minArea(self, image, x, y):
        left, right = [y], [y]
        up, down = [x], [x]
        visited = [[False for _ in range(len(image[0]))] for _ in range(len(image))]

        
        self.helper(image, x, y, left, right, up, down, visited)
        return (down[0] - up[0] + 1) * (right[0] - left[0] + 1)
    
    def helper(self, image, x, y, left, right, up, down, visited):#这样子的话，值传递不出来
        if (x < 0 or x >= len(image) or y < 0 or y >= len(image[0]) or visited[x][y] or image[x][y] == '0'): 
            return
#        left = min(left, y)
#        right = max(right, y)
#        up = min(up, x)
#        down = max(down, x)
        if y < left[0]: left[0] = y
        elif y > right[0]: right[0] = y
        if x < up[0]: up[0] = x
        elif x > down[0]: down[0] = x
        visited[x][y] = True
        self.helper(image, x + 1, y, left, right, up, down, visited)
        self.helper(image, x - 1, y, left, right, up, down, visited)
        self.helper(image, x, y + 1, left, right, up, down, visited)
        self.helper(image, x, y - 1, left, right, up, down, visited)


        
if __name__ == "__main__":
    Input = [
              "0010",
              "0110",
              "0100"]
    print(Solution3().minArea(Input, 0, 2))
    
    
#class Solution1:# 重点要看看值是怎么传递的在dfs里面
#
#    def minArea(self, image, x, y):
#        left, right = y, y
#        up, down = x, x
#        visited = [[False for _ in range(len(image[0]))] for _ in range(len(image))]
#        def helper(self, image, x, y, left, right, up, down, visited):#这样子的话，值传递不出来
#            if (x < 0 or x >= len(image) or y < 0 or y >= len(image[0]) or visited[x][y] or image[x][y] == '0'): 
#                return
#            left = min(left, y)
#            right = max(right, y)
#            up = min(up, x)
#            down = max(down, x)
#            visited[x][y] = True
#            self.helper(image, x + 1, y, left, right, up, down, visited)
#            self.helper(image, x - 1, y, left, right, up, down, visited)
#            self.helper(image, x, y + 1, left, right, up, down, visited)
#            self.helper(image, x, y - 1, left, right, up, down, visited)
#        
#        self.helper(image, x, y, left, right, up, down, visited)
#        return (down - up + 1) * (right - left + 1)
    
    
    
    
    
    

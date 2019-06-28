# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 15:16:45 2019

@author: hjiang
"""

"""
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area

Example:

Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
Output: 45
Note:

Assume that the total area is never beyond the maximum possible value of int.
拿到两个矩形的问题，我一般都会先对坐标进行排序，这样的好处是可以使两者的位置相对固定，按照相对顺序的模式求解。
排序的方式就是按照四个坐标对应关系去排。因为总的只有两个矩形，排序这步速度很快。

但是这个题并不需要排序也可以，因为求公共面积使用了最小最大值关系，所以没必要排序。
事实上，排不排序这一步对时间没有影响，都是56ms，因此我建议还是排序。

公共面积等于(min(C, G) - max(A, E)) × (min(D, H) - max(B, F))，从图中很容易看出来。
就不讲了。需要注意的是不能把两个直接相乘，因为当两个矩形不想交的时候，这两个部分可能都是负值，
相乘得到了正值，误以为相交了，其实没有。所以需要一个判断。

时间复杂度是O(1)，空间复杂度是O(1)。
--------------------- 
 
原文：https://blog.csdn.net/fuxuemingzhu/article/details/82973125 
、
"""
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        points = [((A, B), (C, D)), ((E, F), (G, H))]#注意这里加了括号，实际上就是在比较两个方形的最左边的点，比较A和E
        points.sort()
        ((A, B), (C, D)), ((E, F), (G, H)) = points
        area1 = (D - B) * (C - A)
        area2 = (H - F) * (G - E)
        x, y = (min(C, G) - max(A, E)), (min(D, H) - max(B, F))#两个右上取最小的减去两个左下取最大的
        area = 0
        if x > 0 and y > 0:
            area = x * y
        return area1 + area2 - area
    
if __name__ == "__main__":
    A = -3; B = 0; C = 3; D = 4; E = 0; F = -1; G = 9; H = 2
    print(Solution().computeArea(A, B, C, D, E, F, G, H))







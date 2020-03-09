# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 16:19:53 2019

@author: hjiang
"""

"""
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. 
Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Figure A),
 write a program to output the skyline formed by these buildings collectively (Figure B).

Buildings  Skyline Contour
The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi],
 where Li and Ri are the x coordinates of the left and right edge of the ith building, respectively, 
 and Hi is its height. It is guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0. 
 You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as: 
    [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .

The output is a list of "key points" (red dots in Figure B) in the format of 
[ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. 
A key point is the left endpoint of a horizontal line segment. 
Note that the last key point, where the rightmost building ends, 
is merely used to mark the termination of the skyline, and always has zero height. 
Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as:
    [ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].

Notes:

The number of buildings in any input list is guaranteed to be in the range [0, 10000].
The input list is already sorted in ascending order by the left x position Li.
The output list must be sorted by the x position.
There must be no consecutive horizontal lines of equal height in the output skyline. 
For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable; 
the three lines of height 5 should be merged into one in the final output as such: [...[2 3], [4 5], [12 7], ...]
核心： 对于楼的（左侧，高度）和（-高度，右侧）建立两个list, 分别是res和hp; 其中（-高度，右侧）是一个heapq,自动把当前最大高度 放在最前
每次弹出event（左侧，-高度，右侧）， 当当前扫描的楼的左侧大于目前最大高度的右侧时（-高度，右侧）， 自动在hp中弹出。
while l >= hp[0][1]:
    heapq.heappop(hp)
而存储是，保存当前的左侧l, 以及最大高度
if res[-1][1] != -hp[0][0]:# res[-1][1] 记录的是当前的最高值，既有上升也有下降，所以不能简单的用大于或者小于
    res.append([l, -hp[0][0]])
"""
import heapq
class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        首先， 把H写成-H就是考虑到要用heapq, 这样最大高度就会被自动排到第一个
        同时对第一个position（左边坐标）与右边左边同时排序，注意程序中的技巧，建立了两个数组
        """

        # 所以, event 不仅需要按第一个元素 position 排序, 在 position 相同时, 第二个元素 h 也是必须有序的
#        events = sorted([(l, -h, r) for l, r, h in buildings] + list({(r, 0, 0) for l, r, h in buildings}))
        events = [(L, -H, R) for L, R, H in buildings]
        events += list({(R, 0, 0) for _, R, _ in buildings})# 这里是为了加上结束的条件，要不是楼就不知道什么时候结束了
        events.sort()
        

        """
        这里，res = [[左边的位置，高度]]； hp = [(高度，终止位置（右坐标）)]
        """
        res, hp = [[0, 0]], [(0, float('inf'))]# 最右边放置的一个地面，作为终结

        for l, neg_h, r in events:
            while l >= hp[0][1]: #如果左坐标大于右坐标，那么右边的建筑（在hp里面）可以弹出了。
                heapq.heappop(hp)#这里需要注意的是hp是一个堆，那么第0个值就是最小值，对应最大高度
            
            # 如果是有高度，自动添加
            if neg_h:
                heapq.heappush(hp, (neg_h, r))#每一个楼的右边边界
            
            """
            这个地方，由于hp中自动记住最大高度-hp[0][0], 相同位置的最大高度会被记录
            同时，由于前面的heappop, 那些过界的高度也会被丢弃，这样矮的高度也会被添加进来
            """
#            if res[-1][1] != -hp[0][0]:
            if res[-1][1] != -hp[0][0]:# res[-1][1] 记录的是当前的最高值，既有上升也有下降，所以不能简单的用大于或者小于
                res.append([l, -hp[0][0]])
        
        return res[1:]
    
if __name__ == "__main__":
    buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]] 
    print(Solution().getSkyline(buildings))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    